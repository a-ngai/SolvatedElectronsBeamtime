import numpy as np
import lmfit
from .common_functions import residuals, transpose_axis_to_zero

def get_tof_mq_constants(peaks=None, constants=None):
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
    t0 : float
    propconst : float
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

    calibration_constants = timezero, propconst
    if np.isnan(calibration_constants):
        raise ValueError(f'nan found in calibration constants {calibration_constants}')

    return timezero, propconst

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



def tof_mq_coordinate_func(tof_in, timezero, propconst):
    """ See tof_mq_calibration() """
    mq_coordinate = tof_in*np.nan
    mq_coordinate[tof_in>=timezero] = propconst * (tof_in[tof_in>=timezero]-timezero)**2
    return mq_coordinate

def tof_mq_jacobian_func(tof_in, timezero, propconst):
    """ See tof_mq_calibration() """
    # |dT/dmq_in|
    jacobian = tof_in*np.nan
    jacobian[tof_in>timezero] = 1/(propconst*2*(tof_in[tof_in>timezero]-timezero))
    return jacobian

def mq_tof_coordinate_func(mq_in, timezero, propconst):
    """ See tof_mq_calibration() """
    tof_in = np.sqrt(mq_in/propconst) + timezero
    tof_in[mq_in<0] = np.nan
    return tof_in

def mq_tof_jacobian_func(mq_in, timezero, propconst):
    """ See tof_mq_calibration() """
    # |dmq_in/dT|
    jacobian = (propconst*2*(mq_tof_coordinate_func(mq_in)-timezero))
    jacobian[mq_in<0] = np.nan
    return jacobian

def tof_to_mq_conversion(tof, spectrum, t0, propconst, axis=None):
    """ Helper function that converts TOF into KE spectra with the Jacobian correction """
    spectrum = transpose_axis_to_zero(spectrum, axis=axis)
    mq = tof_mq_coordinate_func(tof, t0, propconst)
    mask = tof>t0
    jacobian = tof_mq_jacobian_func(tof, t0, propconst)
    jacobian = np.expand_dims(jacobian, list(np.arange(-1, -spectrum.ndim, -1)))
    mq_coor = mq[mask]
    mq_spec = (spectrum * jacobian)[mask]
    mq_spec = transpose_axis_to_zero(mq_spec, axis=axis)  # revert transposition
    return mq_coor, mq_spec

def mq_to_tof_conversion(mq, spectrum, t0, propconst, axis=None):
    """ Helper function that converts KE into TOF spectra with the Jacobian correction """
    spectrum = transpose_axis_to_zero(spectrum, axis=axis)
    tof = mq_tof_coordinate_func(mq, t0, propconst)
    mask = tof>t0
    jacobian = mq_tof_jacobian_func(mq, t0, propconst)
    jacobian = np.expand_dims(jacobian, list(np.arange(-1, -spectrum.ndim, -1)))
    tof_coor = tof[mask]
    tof_spec = (spectrum * jacobian)[mask]
    tof_spec = transpose_axis_to_zero(tof_spec, axis=axis)  # revert transposition
    return tof_coor, tof_spec

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

def tof_ke_coordinate_func(tof_in, t0, propconst, ke0):
    """ See tof_ke_calibration() """
    ke_coordinate = tof_in*np.nan
    ke_coordinate[tof_in>t0] = 1/propconst / (tof_in[tof_in>t0] - t0+0.)**2 + ke0
    return ke_coordinate

def tof_ke_jacobian_func(tof_in, t0, propconst, ke0):
    """ See tof_ke_calibration() """
    # |dT/dke_in|
    jacobian = tof_in*np.nan
    jacobian[tof_in>t0] = (tof_in[tof_in>t0] - t0+0.)**3 / (-2 * 1/propconst)

    return jacobian

def ke_tof_coordinate_func(ke_in, t0, propconst, ke0):
    """ See tof_ke_calibration() """
    tof_in = ke_in*np.nan
    tof_in[ke_in>ke0] = np.sqrt(1/propconst / (ke_in[ke_in>ke0] - ke0+0.)) + t0
    return tof_in

def ke_tof_jacobian_func(ke_in, t0, propconst, ke0):
    """ See tof_ke_calibration() """
    # |dke_in/dT|
    jacobian = (-2 * 1/propconst) / (ke_tof_coordinate_func(ke_in, t0, propconst, ke0) - t0+0.)**3
    return jacobian

def tof_to_ke_conversion(tof, spectrum, t0, propconst, ke0, axis=None):
    """ Helper function that converts TOF into KE spectra with the Jacobian correction """
    spectrum = transpose_axis_to_zero(spectrum, axis=axis)
    ke = tof_ke_coordinate_func(tof, t0, propconst, ke0)
    mask = ke>ke0
    jacobian = tof_ke_jacobian_func(tof, t0, propconst, ke0)
    jacobian = np.expand_dims(jacobian, list(np.arange(-1, -spectrum.ndim, -1)))
    ke_coor = ke[mask]
    ke_spec = (spectrum * jacobian)[mask]
    ke_spec = transpose_axis_to_zero(ke_spec, axis=axis)  # revert transposition
    return ke_coor, ke_spec

def ke_to_tof_conversion(ke, spectrum, t0, propconst, ke0, axis=None):
    """ Helper function that converts KE into TOF spectra with the Jacobian correction """
    spectrum = transpose_axis_to_zero(spectrum, axis=axis)
    tof = ke_tof_coordinate_func(ke, t0, propconst, ke0)
    mask = ke>0
    jacobian = ke_tof_jacobian_func(ke, t0, propconst, ke0)
    jacobian = np.expand_dims(jacobian, list(np.arange(-1, -spectrum.ndim, -1)))
    tof_coor = tof[mask]
    tof_spec = (spectrum * jacobian)[mask]
    tof_spec = transpose_axis_to_zero(tof_spec, axis=axis)  # revert transposition
    return tof_coor, tof_spec
