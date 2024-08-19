import os
import re
import lmfit
import numpy as np
import matplotlib as pl
from matplotlib import ticker
from scipy.integrate import cumtrapz, simps
from scipy.interpolate import interp1d
from scipy.stats import mode


def combination(list_of_lists):
    """ 
    Recursive function, that returns the possible combinations which
    contain one element from each list. The output lists preserve the order
    of the input lists. Nested lists do not have to be the same shape.
    
    Parameters
    ----------
    list_of_lists: list
        A list that contains the possible lists to choose an element from.
    
    Returns
    -------
    output: list
        A list that contains all possible combinations that contain a single
        element from every list that was in the input

    Examples
    --------
    >>> combination([['1','2'],
    >>>              ['A','B'],
    >>>              ['i','ii']])
    [['1', 'A', 'i'],
     ['1', 'A', 'ii'],
     ['1', 'B', 'i'],
     ['1', 'B', 'ii'],
     ['2', 'A', 'i'],
     ['2', 'A', 'ii'],
     ['2', 'B', 'i'],
     ['2', 'B', 'ii']]
    """

    output=[]

    if len(list_of_lists)==1:
        return list_of_lists[0]

    for item in list_of_lists[0]:
        for next_set_item in combination(list_of_lists[1:]):
            joining = [item]
            if type(next_set_item)==list:
                joining.extend(next_set_item)
            else:
                joining.extend([next_set_item])
            output.append(joining)

    return output

def rebinning(xnew, x, y, axis=None):
    '''changed on 20230525, so that nans are accepted. Another change on 20230625
    for smooth boundaries when the new range is wider than the original range'''

    if axis is None or np.ndim(y)==1:
        nan_bool_array = np.isnan(x)
        y_remove_nans = np.copy(y)
        nans_indices = np.where(np.isnan(y))[0]
        y_remove_nans[nans_indices]=0#y_remove_nans[nans_indices-1]

        y_integral = cumtrapz(y_remove_nans, x=x, initial=0)
        y_interpolate = interp1d(x, y_integral, kind='linear')

        ynew_integral = np.zeros(shape=np.shape(xnew))
        xnew_in = (np.min(x)<=xnew) * (xnew<=np.max(x))
        xnew_out_right = np.max(x) < xnew

        ynew_integral[xnew<np.min(x)] = y_interpolate(xnew[xnew_in][0])
        ynew_integral[xnew_in] = y_interpolate(xnew[xnew_in])
        ynew_integral[xnew_out_right] = ynew_integral[xnew_in][-1]

        ynew = np.gradient(ynew_integral, xnew)

        for i, is_nan in zip(range(len(xnew)-1), nan_bool_array):
            if not is_nan:
                continue
            x_loc = x[i]
            x_lo, x_hi = xnew[i], xnew[i+1]
            crit_nan =  (x_lo<=x_loc)*(x_loc<x_hi)
            ynew[crit_nan] = np.nan

    else:
        transpose_order = np.arange(np.ndim(y))
        if axis!=0:
            transpose_order[0]=axis
            transpose_order[axis]=0

        y_transpose = np.transpose(y, axes=transpose_order)
        y_shape = np.array(np.shape(y))
        new_y_shape = y_shape[transpose_order]
        new_y_shape[0]=len(xnew)

        nan_bool_array = np.isnan(y_transpose)
        y_remove_nans = np.copy(y_transpose)
        y_remove_nans[np.isnan(y_transpose)]=0

        y_integral = cumtrapz(y_remove_nans, x=x, initial=0, axis=0)
        y_interpolate = interp1d(x, y_integral, kind='linear',axis=0)

        ynew_integral = np.zeros(shape=new_y_shape)
        xnew_in = (np.min(x)<=xnew) * (xnew<=np.max(x))
        xnew_out_right = np.max(x) < xnew

        ynew_integral[xnew<np.min(x)] = y_interpolate(xnew[xnew_in][0])
        ynew_integral[xnew_in] = y_interpolate(xnew[xnew_in])
        ynew_integral[xnew_out_right] = ynew_integral[xnew_in][-1]

        ynew = np.gradient(ynew_integral, xnew, axis=0)

        for i, is_nan in zip(range(len(xnew)-1), nan_bool_array):
            if np.sum(is_nan)==0:
                continue
            x_loc = x[i]
            x_lo, x_hi = xnew[i], xnew[i+1]
            crit_nan =  (x_lo<=xnew)*(xnew<x_hi)
            ynew[:,is_nan][crit_nan] = np.nan

        ynew = np.transpose(ynew, axes=transpose_order)  # revert transposition


    return ynew


def convolve_with_gaussian(convolution_width, x, y):

    if convolution_width is None:
        return y

    gaussian_width = convolution_width

    dx = x[1]-x[0]
    s = np.roll(np.arange(-len(x)//2,len(x)//2), shift=int(len(x)//2))*dx

    convolving_array = 1/(gaussian_width*np.sqrt(2*np.pi)) * np.exp(-(s/(np.sqrt(2)*gaussian_width))**2)*dx

    convolution = np.real(np.fft.ifft(np.fft.fft(convolving_array) * np.fft.fft(y)))

    return convolution


def findiff_coefficients(m,n):
    """
    Generates the finite difference coefficients for the specified
    derivative and error order.
    
    Parameters
    ----------
    m : int
        Order of the derivative.
    n : int
        Order of the error.
    """

    p=(m+n-1)//2

    if p==0:
        return np.zeros(1), np.zeros(1)
    elif p<0:
        raise Exception('Condition: (m+n-1)//2>=0  (currently {})'.format(p))

    N = 2*p+1

    system = np.zeros(shape=(N,N), dtype=np.float64)
    p_row = np.arange(-p,p+1)

    for i in np.arange(N):
        system[i] = p_row**i

    rhs = np.zeros(N)
    rhs[m] = np.math.factorial(m)

    coefficients = np.linalg.solve(system, rhs)
    offsets = np.array(p_row, dtype=np.int)

    return coefficients, offsets


def derivative_matrix(r, deriv=1, order_acc=3):
    dr=r[1]-r[0]
    Nr = len(r)

    diff_matrix = np.zeros(shape=(Nr,Nr))
    lindiff_coeff, coeff_pos = findiff_coefficients(m=deriv, n=order_acc)

    for coeff, pos in np.transpose([lindiff_coeff, coeff_pos]):
        coeff_diag = np.zeros(Nr-int(np.abs(pos))) + coeff
        diff_matrix += np.diag(coeff_diag, k=int(pos))

    deriv_matrix = diff_matrix/dr**(deriv)
    deriv_matrix[:int(len(lindiff_coeff)//2)]=0
    deriv_matrix[-int(len(lindiff_coeff)//2):]=0

    if deriv==0:
        return np.eye(Nr)

    return deriv_matrix

def adjust_ylim(xlim, xdata, ydata):
    ''' Adjust the ylim based on the xlim '''
    x_crit = (xdata>=xlim[0]) * (xdata<xlim[1])
    ymin, ymax = np.min(ydata[x_crit]), np.max(ydata[x_crit])
    ylim = (ymin - 0.1*(ymax-ymin), ymax+0.1*(ymax-ymin))
    return ylim

def get_colour(i):
    ''' Cycles through the default matplotlib colours '''
    colours = pl.rcParams['axes.prop_cycle'].by_key()['color']
    Ncolours = len(colours)
    return colours[i%Ncolours]


def residuals(params, model, x, y):
    ''' scipy will square this for their least-squares fit '''
    return y-model(params, x)

def weighted_residuals(params, model, xdata, ydata, yerr):
    ''' scipy squares this for its residuals, hence the square root for the error here '''
    return 1/yerr*(ydata-model(params, xdata))

def tof_mq_calibration(peaks=None, constants=None):
    """
    Formulas are: m/q = C * (t-T0)^2, d(m/q) = C * 2 (t-T0) dt

    # m/q = C * (t-T0)^2
    # d(m/q) = C * 2 (t-T0) dt
    Alternate names:
        m/q = mq
        t = tof
        C = propconst (proportionality constant)
        T0 = timezero

    Parameters
    ----------
    peaks : array, optional
        Must have form:
            [[tof1, mq1],
             [tof2, mq2],
             ...
             [tofn, mqn]]. 
            The default is None.
    constants : TYPE, optional
        Must have form:
            [T0, C]. 
            The default is None.

    Raises
    ------
    Exception
        DESCRIPTION.

    Returns
    -------
    mq_coordinate_func : func
        Conversion function for TOF -> m/q coordinates. Input can be either a number or an array
    mq_jacobian_func : func
        Jacobian correction when converting TOF -> m/q coordinates.
    tof_coordinate_func : func
        Conversion function for m/q -> TOF coordinates. Input can be either a number or an array
    tof_jacobian_func : func
        Jacobian correction when converting m/q -> TOF coordinates.
    """

    if peaks is constants is None:
        raise AssertionError("Either keyword 'peaks' or 'constants' must be used; no defaults!")

    if constants is not None:
        try:
            length = len(constants)
        except TypeError:
            raise AssertionError(f"keyword 'constants' ({constants}) must be of form (T0, C)")
        if length != 2:
            raise AssertionError(f"keyword 'constants' length ({len(constants)}) must have length 2")
        timezero, propconst = constants
    elif peaks is not None:
        if np.ndim(peaks) != 2:
            raise AssertionError(f"keyword 'peaks' dimension ({np.ndim(peaks)}) must have dimension 2")

        tof_peaks, mq_peaks = np.transpose(peaks)
        if len(peaks)==1:
            (tof1), (mq1) = tof_peaks, mq_peaks
            timezero = 0
            propconst = mq1/tof1**2

        elif len(peaks)==2:
            (tof1, tof2), (mq1, mq2) = tof_peaks, mq_peaks
            timezero = (tof2*np.sqrt(mq1) - tof1*np.sqrt(mq2)) / (np.sqrt(mq1)-np.sqrt(mq2))
            propconst = ((np.sqrt(mq1)-np.sqrt(mq2))/(tof1-tof2))**2

        elif len(peaks)>2:
            def mq_fit_model(params, tof):
                # C = params['C']
                # T0 = params['T0']
                # mq = C * (tof - T0)**2

                C = params['C']
                T0 = params['T0']
                sqrt_mq = np.sqrt(C) * (tof - T0)
                return sqrt_mq

            (tof1, tof2, *_), (mq1, mq2, *_) = tof_peaks, mq_peaks
            timezero_guess = (tof2*np.sqrt(mq1) - tof1*np.sqrt(mq2)) / (np.sqrt(mq1)-np.sqrt(mq2))
            propconst_guess = ((np.sqrt(mq1)-np.sqrt(mq2))/(tof1-tof2))**2

            initial_params = lmfit.Parameters()
            initial_params.add_many(
                    ('C', propconst_guess, True, 0, None),
                    ('T0', timezero_guess, True, None, np.max(tof_peaks)),
                    )

            fit_results = lmfit.minimize(residuals, initial_params,
                                         args=(mq_fit_model, tof_peaks, np.sqrt(mq_peaks)))
            fit_params = fit_results.params
            propconst = fit_params['C'].value
            timezero = fit_params['T0'].value

    def mq_coordinate_func(tof_in):
        mq_coordinate = tof_in*np.nan
        mq_coordinate[tof_in>=timezero] = propconst * (tof_in[tof_in>=timezero]-timezero)**2
        return mq_coordinate

    def mq_jacobian_func(tof_in):
        # |dT/dmq_in|
        jacobian = tof_in*np.nan
        jacobian[tof_in>timezero] = 1/(propconst*2*(tof_in[tof_in>timezero]-timezero))
        return jacobian

    def tof_coordinate_func(mq_in):
        tof_in = np.sqrt(mq_in/propconst) + timezero
        tof_in[mq_in<0] = np.nan
        return tof_in

    def tof_jacobian_func(mq_in):
        # |dmq_in/dT|
        jacobian = (propconst*2*(tof_coordinate_func(mq_in)-timezero))
        jacobian[mq_in<0] = np.nan
        return jacobian

    calibration_dict = {
            'tof_to_mq_coor' : mq_coordinate_func,
            'tof_to_mq_jaco' : mq_jacobian_func,
            'mq_to_tof_coor' : tof_coordinate_func,
            'mq_to_tof_jaco' : tof_jacobian_func,
            'constants' : {'C':propconst, 'timezero':timezero},
            }

    constants_dict = calibration_dict['constants']
    if np.nan in list(calibration_dict['constants'].values()):
        raise ValueError(f'nan found in calibration constants {constants_dict}')

    return calibration_dict

def tof_ke_calibration(peaks=None, constants=None):
    """
    Formulas are: ke = 1 / (C*(t-T0)^2) + ke0, d(ke) = -2 / (C*(t-T0)^3) dt

    To put ke0 (i.e. retardation potential) as a peak, use the pair (t=large number, ke=ke0).

    Alternate names:
        ke = energy
        t = tof
        C = propconst (proportionality constant)
        T0 = timezero

    Parameters
    ----------
    peaks : array, optional
        Must have form:
            [[tof1, ke1],
             [tof2, ke2],
             ...
             [tofn, ken]]. 
            The default is None.
    constants : TYPE, optional
        Must have form:
            [T0, C]. 
            The default is None.

    Raises
    ------
    Exception
        DESCRIPTION.

    Returns
    -------
    ke_coordinate_func : func
        Conversion function for TOF -> KE coordinates. Input can be either a number or an array
    ke_jacobian_func : func
        Jacobian correction when converting TOF -> KE coordinates.
    tof_coordinate_func : func
        Conversion function for KE -> TOF coordinates. Input can be either a number or an array
    tof_jacobian_func : func
        Jacobian correction when converting KE -> TOF coordinates.
    """

    if peaks is constants is None:
        raise AssertionError("Either keyword 'peaks' or 'constants' must be used; no defaults!")

    if constants is not None:
        try:
            length = len(constants)
        except TypeError:
            raise AssertionError(f"keyword 'constants' ({constants}) must be of form (T0, C, KE0)")
        if length != 3:
            raise AssertionError(f"keyword 'constants' length ({len(constants)}) must have length 3")
        timezero, propconst, ke0 = constants
    elif peaks is not None:
        if np.ndim(peaks) != 2:
            raise AssertionError(f"keyword 'peaks' dimension ({np.ndim(peaks)}) must have dimension 2")
        _peaks = list(peaks)

        tof_peaks, ke_peaks = np.transpose(_peaks)
        timezero = None
        ke0 = None

        if np.inf in tof_peaks:
            tof_inf_index = np.where(tof_peaks==np.inf)[0][0]
            ke0 = ke_peaks[tof_inf_index]
            _peaks.pop(tof_inf_index)
            tof_peaks, ke_peaks = np.transpose(peaks)
        if np.inf in ke_peaks:
            ke_inf_index = np.where(ke_peaks==np.inf)[0][0]
            timezero = tof_peaks[ke_inf_index]
            _peaks.pop(ke_inf_index)
            tof_peaks, ke_peaks = np.transpose(_peaks) 

        tof_peaks, ke_peaks = np.transpose(_peaks)

        if len(_peaks)==1:
            if timezero is None:
                timezero = 0
            if ke0 is None:
                ke0 = 0
            (tof1,), (ke1,) = tof_peaks - timezero, ke_peaks - ke0
            propconst = 1/(ke1 * tof1**2)

        elif (len(_peaks)==2) and (timezero is None):
            if ke0 is None:
                ke0 = 0
            if timezero is None:
                timezero = 0
            (tof1, tof2), (ke1, ke2) = tof_peaks - timezero, ke_peaks - ke0
            timezero = (tof2*np.sqrt(ke2) - tof1*np.sqrt(ke1)) / (np.sqrt(ke2) - np.sqrt(ke1))
            propconst = 1/(ke1*ke2/(np.sqrt(ke2)-np.sqrt(ke1))**2 * (tof1-tof2)**2)
        elif (len(_peaks)==2) and (timezero is not None):
            (tof1, tof2), (ke1, ke2) = tof_peaks - timezero, ke_peaks - ke0
            ke0 = (ke2*tof2**2 - ke1*tof1**2) / (tof2**2 - tof1**2)
            propconst = (tof2**2 - tof1**2) / ((ke1-ke2) * tof1**2 * tof2**2)

        # elif len(_peaks)==3:
        #     (tof1, tof2, tof3), (ke1, ke2, ke3) = tof_peaks, ke_peaks
        #     raise NotImplementedError('did not implement this yet, waiting for my mathematica license')

        elif len(_peaks)>2:
            def ke_fit_model(params, tof):
                C = params['C']
                T0 = params['T0']
                KE0 = params['KE0']

                ke = 1 / (C * (tof - T0)**2) + KE0
                return ke
            min_tof_i = np.where(tof_peaks == np.min(tof_peaks))[0][0]
            max_tof_i = np.where(tof_peaks == np.max(tof_peaks))[0][0]

            (tof1, tof2) = np.array([tof_peaks[min_tof_i], tof_peaks[max_tof_i]])
            (ke1, ke2) = np.array([ke_peaks[min_tof_i], ke_peaks[max_tof_i]])

            if timezero is None:
                timezero_guess = (tof2*np.sqrt(ke2) - tof1*np.sqrt(ke1)) / (np.sqrt(ke2) - np.sqrt(ke1))
                vary_timezero = True
            else:
                timezero_guess = timezero
                vary_timezero = False
            if ke0 is None:
                ke0_guess = 0
                vary_ke0 = True
            else:
                ke0_guess = ke0
                vary_ke0 = False

            propconst_guess = 1/(ke1*ke2/(np.sqrt(ke2)-np.sqrt(ke1))**2 * (tof1-tof2)**2)

            initial_params = lmfit.Parameters()
            initial_params.add_many(
                    ('C', propconst_guess, True, 0, None),
                    ('T0', timezero_guess, vary_timezero, None, np.min(tof_peaks)),
                    ('KE0', ke0_guess, vary_ke0, 0, None),
                    )

            fit_results = lmfit.minimize(residuals, initial_params,
                                         args=(ke_fit_model, tof_peaks, ke_peaks))
            fit_params = fit_results.params
            propconst = fit_params['C'].value
            timezero = fit_params['T0'].value
            ke0 = fit_params['KE0'].value

    def ke_coordinate_func(tof_in):
        ke_coordinate = tof_in*np.nan
        ke_coordinate[tof_in>timezero] = 1/propconst / (tof_in[tof_in>timezero] - timezero+0.)**2 + ke0
        return ke_coordinate

    def ke_jacobian_func(tof_in):
        # |dT/dke_in|
        jacobian = tof_in*np.nan
        jacobian[tof_in>timezero] = (tof_in[tof_in>timezero] - timezero+0.)**3 / (-2 * 1/propconst)

        return jacobian

    def tof_coordinate_func(ke_in):
        tof_in = ke_in*np.nan
        tof_in[ke_in>ke0] = np.sqrt(1/propconst / (ke_in[ke_in>ke0] - ke0+0.)) + timezero
        return tof_in

    def tof_jacobian_func(ke_in):
        # |dke_in/dT|
        jacobian = (-2 * 1/propconst) / (tof_coordinate_func(ke_in) - timezero+0.)**3
        return jacobian

    calibration_dict = {
            'tof_to_ke_coor' : ke_coordinate_func,
            'tof_to_ke_jaco' : ke_jacobian_func,
            'ke_to_tof_coor' : tof_coordinate_func,
            'ke_to_tof_jaco' : tof_jacobian_func,
            'constants' : {'KE0':ke0,'C':propconst, 'timezero':timezero},
            }

    constants_dict = calibration_dict['constants']
    if np.nan in list(calibration_dict['constants'].values()):
        raise ValueError(f'nan found in calibration constants {constants_dict}')

    return calibration_dict

def single_pass_moment_sums(generator1, generator2=None, filter1=None, filter2=None, _weight=1):
    """
    Calculate the covariance. For "self"-covariance, only generator1 is needed.

    IMPORTANT: if only looking at a subset of the total covariance, both filter1
    and filter2 keywords are necessary; only having filter1 does NOT mean
    filter2 will also select a subset in the case of "self"-covariance; these
    are independent!
       

    Parameters
    ----------
    generator1 : generator
        Generator that outputs a "sample" array each time it is called.
    generator2 : generator, optional
        Analogous to generator1. If intended to be the same as generator1, keep
        as None. The default is None.
    filter1 : function, optional
        Function that acts on the array returned by generator1. Intended to
        shrink the size of the overall covariance matrix. Can also be used to
        average parts of the data e.g. return values of the sum over specific
        ranges. The default is None.
    filter2 : function, optional
        Analogous functionality of filter1, now acting on generator2. The
        default is None.

    Returns
    -------
    AnalysisDict : dict
        Dictionary containing the covariance matrix, mean_values, and the number
        of samples.
        
    """

    if generator2 is None:
        self_covariance = True
        generator2 = __import__("itertools").count()  # infinite generator
    else:
        self_covariance = False
    if filter1 is None:
        filter1 = lambda x: x
    if filter2 is None:
        filter2 = lambda x: x

    mean_x = 0
    mean_y = 0
    current_cn = 0
    n = 0
    for item1, item2 in zip(generator1, generator2):
        if self_covariance:
            item2 = item1
        next_x = filter1(item1)
        next_y = filter2(item2)

        n += 1

        next_mean_x = mean_x + (next_x - mean_x)/n
        next_mean_y = mean_y + (next_y - mean_y)/n
        current_cn += np.outer((next_x - next_mean_x), (next_y - mean_y))
        mean_x = next_mean_x
        mean_y = next_mean_y

    AnalysisDict = {
            'covar_sum' : current_cn * _weight,
            'x_sum' : mean_x*n * _weight,
            'y_sum' : mean_y*n * _weight,
            'count' : n * _weight,
            }
    return AnalysisDict

def single_pass_covariance(generator1, generator2=None, filter1=None, filter2=None):
    SumDict = single_pass_moment_sums(generator1, generator2=generator2, filter1=filter1, filter2=filter2)
    n = SumDict['count']
    covariance = SumDict['covar_sum'] / n
    mean_x = SumDict['x_sum'] / n
    mean_y = SumDict['y_sum'] / n
    AnalysisDict = {
            'covariance' : covariance,
            'mean_x' : mean_x,
            'mean_y' : mean_y,
            'count' : n,
            }
    return AnalysisDict



def combine_datapoints(x, y, xerr=None, yerr=None, xtol=1):
    if xerr is None:
        xerr = 0*x+1
    if yerr is None:
        yerr = 0*y+1
    xw = 1/np.array(xerr)**2
    yw = 1/np.array(yerr)**2

    sort = np.argsort(x)
    x_temp = list(np.array(x)[sort])
    y_temp = list(np.array(y)[sort])
    xw_temp = list(np.array(xw)[sort])
    yw_temp = list(np.array(yw)[sort])
    i = 0
    while (i < len(x_temp) - 1):
        if x_temp[i+1]-x_temp[i] > xtol:
            i += 1
            continue

        new_x = (x_temp[i]*xw_temp[i] + x_temp[i+1]*xw_temp[i+1]) / np.sum(xw_temp[i]+xw_temp[i+1])
        new_xw = np.sum(xw_temp[i]+xw_temp[i+1])
        x_temp.pop(i)
        xw_temp.pop(i)
        x_temp[i] = new_x
        xw_temp[i] = new_xw

        new_y = (y_temp[i]*yw_temp[i] + y_temp[i+1]*yw_temp[i+1]) / np.sum(yw_temp[i]+yw_temp[i+1])
        new_yw = np.sum(yw_temp[i]+yw_temp[i+1])
        y_temp.pop(i)
        yw_temp.pop(i)
        y_temp[i] = new_y
        yw_temp[i] = new_yw

    output_x = np.array(x_temp)
    output_y = np.array(y_temp)
    output_xerr = 1/np.sqrt(np.array(xw_temp))
    output_yerr = 1/np.sqrt(np.array(yw_temp))
    return output_x, output_y, output_xerr, output_yerr


def background_subtraction(meas_data, back_data):
    back_sub = np.average(meas_data,axis=0)-np.average(back_data,axis=0)
    return back_sub



def save_with_comment(save_location, data, axis1=None, axis2=None, comment='', delimiter=','):
    '''
    Standardizes file saving, while preserving the data types in the
    arrays.

    Parameters
    ----------
    save_location : str
        Location of the save file.
    data : numpy.array
        The data (either one- or two-dimensional) to be saved.
    axis1 : numpy.array, optional
        Values which label the first axis (row-by-row) of the data.
        When None, then is automatically generated.
        The default is None.
    axis2 : TYPE, optional
        Values which label the second axis (column-by-column) of the data.
        When None, then is automatically generated.
        The default is None.
    comment : str, optional
        Comment which is put on the second line of the save file.
        The default is ''.
    delimiter : str, optional
        The delimiter used in the save file e.g. csv format uses
        ','.
        The default is ','.

    Raises
    ------
    Exception
        See descriptions.

    Returns
    -------
    None.

    '''

    if data.ndim > 2:
        raise Exception('data must be either one- or two-dimensional')
    if data.ndim == 2 and axis2 is None:
        axis2 = np.arange(data.shape[1])
        mod_data = data
    elif data.ndim == 1:
        mod_data = data[:,np.newaxis]
        axis2 = np.arange(1)
    else:
        mod_data = data
    if axis1 is None:
        axis1 = np.arange(mod_data.shape[0])

    if (len(axis1), len(axis2)) != np.shape(mod_data):
        raise Exception('Lengths of axis1 ({len(axis1}) and axis2 ({len(axis2)}) must match the shape of data {np.shape(mod_data)}')

    first_row = np.concatenate((np.array(['',]), np.array(axis2,dtype=str)), axis=0)
    other_rows =  np.concatenate((
        np.array(axis1[:,np.newaxis],dtype=str),
        np.array(mod_data,dtype=str)), axis=1)
    save_data = np.concatenate((first_row[np.newaxis,:], other_rows),axis=0)

    axis1_dtype = axis1.dtype
    axis2_dtype = axis2.dtype
    data_dtype = mod_data.dtype
    dtype_comment = f'{axis1_dtype},{axis2_dtype},{data_dtype}'
    header = dtype_comment + '\n' + comment

    np.savetxt(save_location, save_data, header=header,fmt='%s', delimiter=delimiter)

def load_with_comment(load_location, delimiter=','):
    '''
    Loads files which were created by the save_with_comment() function.

    Parameters
    ----------
    load_location : str
        Location of the loading file.
    delimiter : str, optional
        The delimiter used in the loading file e.g. csv format uses
        ','.
        The default is ','.

    Returns
    -------
    data : numpy.array
        Two-dimensional array.
    axis1 : numpy.array
        Array which labels the first axis (row-by-row).
    axis2 : numpy.array
        Array which labels the second axis (column-by-column).
    '''

    loading = np.loadtxt(load_location, delimiter=delimiter, dtype=str)

    with open(load_location) as file:
        first_line = file.readline()

    try:
        axis1_dtype, axis2_dtype, data_dtype = re.sub(r'\n','', re.sub('# ','',first_line)).split(',')
    except TypeError as e:
        print(f"Cannot find datatype, using default float64. Error message: {e}")
        axis1_dtype, axis2_dtype, data_dtype = np.float64, np.float64, np.float64

    axis1 = np.array(loading[1:,0], dtype=axis1_dtype)
    axis2 = np.array(loading[0,1:], dtype=axis2_dtype)
    data = np.array(loading[1:,1:], dtype=data_dtype)

    return data, axis1, axis2


def add_mq_label(ax1, tof_to_mq_func, minor=1, major=1):
    '''
    Function which generates a second axis below the tof
    axis, which a generally non-linear spacing.

    Parameters
    ----------
    tof : numpy.array
        Array of the tof coordinates.
    ax1 : matplotlib.axes._subplots.AxesSubplot
        The x-axis matplotlib.axes object that corresponds to
        the tof coordinate.
    tof_to_mq_func : func
        A function which converts from tof to m/q coordinates.

    Returns
    -------
    ax2 : matplotlib.axes._subplots.AxesSubplot
        The maplotlib.axes object that cooresponds to the m/q
        coordinate.

    '''

    ax2_tof_lims = ax1.get_xlim()

    samples = 1000
    tof_sampling = np.linspace(*ax2_tof_lims, num=samples)
    sampled_mq = tof_to_mq_func(tof_sampling)
    sampled_mq[sampled_mq<0]=1
    mq_to_tof = interp1d(sampled_mq, tof_sampling)

    mq_lim = tof_to_mq_func(np.array(ax2_tof_lims))
    mq_lim = np.array([np.ceil(mq_lim[0]), np.floor(mq_lim[1])])
    mq_lim[np.isnan(mq_lim)]=1
    mq_lin = np.arange(np.ceil(mq_lim[0]/major)*major, mq_lim[1]+1,major, dtype=int)

    ax2 = ax1.twiny()

    all_mq = np.arange(np.ceil(min(mq_lin)/minor)*minor,max(mq_lin)+1,minor,dtype=int)
    newpos = [mq_to_tof(mq_i) for  mq_i in mq_lin]   # position of the xticklabels in the old x-axis
    allpos = [mq_to_tof(mq_i) for  mq_i in all_mq]

    minor_ticker=ticker.FixedLocator(allpos)
    major_ticker=ticker.FixedLocator(newpos)

    ax2.xaxis.set_minor_locator(minor_ticker)
    ax2.xaxis.set_major_locator(major_ticker)
    ax2.set_xticklabels(mq_lin, minor=False)

    ax2.xaxis.set_ticks_position('bottom') # set the position of the second x-axis to bottom
    ax2.xaxis.set_label_position('bottom') # set the position of the second x-axis to bottom
    ax2.spines['bottom'].set_position(('outward', 36))
    ax2.set_xlim(ax2_tof_lims)
    ax2.minorticks_on()

    return ax2

def add_ke_label(ax1, tof_to_ke_func, minor=0.1, major=1, ke_max=None):
    '''
    Function which generates a second axis below the tof
    axis, which a generally non-linear spacing.

    Known issue: the minor keyword doesn't currently work. I don't know why the minor
        ticks aren't showing up.

    Parameters
    ----------
    tof : numpy.array
        Array of the tof coordinates.
    ax1 : matplotlib.axes._subplots.AxesSubplot
        The x-axis matplotlib.axes object that corresponds to
        the tof coordinate.
    tof_to_ke_func : func
        A function which converts from tof to m/q coordinates.

    Returns
    -------
    ax2 : matplotlib.axes._subplots.AxesSubplot
        The maplotlib.axes object that cooresponds to the m/q
        coordinate.

    '''
    ax2_tof_lims = ax1.get_xlim()

    samples = 1000
    tof_sampling = np.linspace(*ax2_tof_lims, num=samples)
    sampled_ke = tof_to_ke_func(tof_sampling)
    isnan = np.isnan(sampled_ke)
    ke_to_tof = interp1d(sampled_ke, tof_sampling)

    ke_lim = tof_to_ke_func(np.array(ax2_tof_lims))
    ke_lim = np.array([np.ceil(ke_lim[1]), np.floor(ke_lim[0])])
    ke_lim[np.isnan(ke_lim)]=np.max(sampled_ke[~np.isnan(sampled_ke)])
    if (ke_max is not None) and (ke_max < ke_lim[1]):
        ke_lim[1]=ke_max
    ke_lin = np.arange(np.ceil(ke_lim[0]/major)*major, ke_lim[1]+1,major)
    all_ke = np.arange(np.ceil(ke_lim[0]/minor)*minor, ke_lim[1]+1,minor)
    ke_lin = np.array(ke_lin, dtype=type(major))
    all_ke = np.array(all_ke, dtype=type(minor))

    newpos = ke_to_tof(ke_lin)   # position of the xticklabels in the old x-axis
    allpos = ke_to_tof(all_ke)
    minor_ticker=ticker.FixedLocator(allpos)
    major_ticker=ticker.FixedLocator(newpos)

    ax2 = ax1.twiny()
    ax2.xaxis.set_minor_locator(minor_ticker)
    ax2.xaxis.set_major_locator(major_ticker)
    ax2.set_xticklabels(ke_lin, minor=False)
    ax2.xaxis.set_ticks_position('bottom') # set the position of the second x-axis to bottom
    ax2.xaxis.set_label_position('bottom') # set the position of the second x-axis to bottom
    ax2.spines['bottom'].set_position(('outward', 36))
    ax2.set_xlim(ax2_tof_lims)
    ax2.minorticks_on()

    return ax2

def gaussians(params, x):
    '''
    Can have as many individual gaussian profiles as needed, as long as the params are in the form:
        {amp0, center0, width0, amp1, center1, width1, ...}
    '''

    param_abbrev = ['amp','center','width']
    Npeaks = 0
    for i in range(len(list(params.keys()))//3):
        for abbrev in param_abbrev:
            name = f'{abbrev}{i}'
            try:
                params[name]
                Npeaks = i+1
            except KeyError:
                print(f'Only 3*{i-1} gaussian parameters found; assuming {i-1} gaussian profiles')
                Npeaks = i
                break
    accumulation = 0.*x
    for i in range(Npeaks):
        amp, center, width = params[f'amp{i}'], params[f'center{i}'], params[f'width{i}']
        next_gaussian = amp/(width*np.sqrt(2*np.pi)) * np.exp(-((x-center)/width)**2/2.)
        accumulation += next_gaussian
    return accumulation

def gaussians_split(params, x):
    '''
    Can have as many individual gaussian profiles as needed, as long as the params are in the form:
        {amp0, center0, width0, amp1, center1, width1, ...}
    '''

    param_abbrev = ['amp','center','width']
    Npeaks = 0
    for i in range(len(list(params.keys()))//3):
        for abbrev in param_abbrev:
            name = f'{abbrev}{i}'
            try:
                params[name]
                Npeaks = i+1
            except KeyError:
                print(f'Only 3*{i-1} gaussian parameters found; assuming {i-1} gaussian profiles')
                Npeaks = i
                break
    separate = []
    for i in range(Npeaks):
        amp, center, width = params[f'amp{i}'], params[f'center{i}'], params[f'width{i}']
        next_gaussian = amp/(width*np.sqrt(2*np.pi)) * np.exp(-((x-center)/width)**2/2.)
        separate.append(next_gaussian)
    return separate

def omit(items_list, remove=None):
    ''' returns a list without any element in "remove".'''
    if remove is None:
        filtered_list = items_list
        return filtered_list
    if (len(remove)==() or type(remove)=='str'):
        remove = [remove,]
    filtered_list = [item for item in items_list if item not in remove]
    return filtered_list

def lrange(start, end, step=1, remove=None):
    ''' combination of omit(list(range)) as a convenience function.'''
    full_list = list(range(start, end, step))
    changed_list = omit(full_list, remove)
    return changed_list

def closest(locs, array):
    indices = [np.where(np.min((loc-array)**2) == (loc-array)**2)[0][0] for loc in locs]
    return np.array(indices)
