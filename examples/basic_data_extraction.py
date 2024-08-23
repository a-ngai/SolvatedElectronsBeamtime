# %%
"""
# Set-up for Intensity-binning analysis
"""

# %%
"""
## Import statements
"""

# %%
# uncomment the following line when you want to interact with the matplotlib plots
#%matplotlib widget

import os
import sys

import numpy as np
from scipy.integrate import trapezoid
import scipy.constants as spc
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.colors import LogNorm, BASE_COLORS
from matplotlib import colormaps
cmap = colormaps.get_cmap('plasma')

# import lmfit

from scipy.interpolate import CubicSpline, PchipInterpolator
from scipy.signal import convolve as conv1d
from scipy.special import erf

from fermi_libraries.run_module import Run, RunSets
from fermi_libraries.common_functions import (rebinning, tof_mq_calibration, get_colour, 
                              add_ke_label, gaussians, residuals)
from fermi_libraries.dictionary_search import search_symbols

# %%
"""
### Function definitions (that you might change)
"""

# %%

def keyword_functions(keyword, aliasFunc, DictionaryObject):
    

    if False:
        pass
    
    elif keyword=='bunch_parity':
        bunches = DictionaryObject['bunches'][()]
        parity = bunches%2==0

        return parity
    
    elif keyword=='fel_wavelengths_mu':
        fel_spectrum = DictionaryObject['photon_diagnostics/Spectrometer/hor_spectrum'][()]
        padres_span = DictionaryObject['/photon_diagnostics/Spectrometer/WavelengthSpan'][()]
        padres_wavelength = DictionaryObject['/photon_diagnostics/Spectrometer/Wavelength'][()] + 0.0575
        padres_pixel2micron = DictionaryObject['/photon_diagnostics/Spectrometer/Pixel2micron'][()]
        padres_lambda = padres_wavelength + np.arange(-500, 500) * padres_pixel2micron * padres_span / 1000
        fel_lambda = padres_wavelength + np.arange(-500, 500) * padres_pixel2micron * padres_span / 1000

        L = 0.5
        above_half_max = fel_spectrum > np.max(fel_spectrum) * L
        moment_0 = np.sum(fel_lambda**0 * fel_spectrum * above_half_max, axis=1)
        moment_1 = np.sum(fel_lambda**1 * fel_spectrum * above_half_max, axis=1)

        mu = moment_1 / moment_0

        return mu

    elif keyword=='fel_wavelengths_sigma':
        fel_spectrum = DictionaryObject['photon_diagnostics/Spectrometer/hor_spectrum'][()]
        padres_span = DictionaryObject['/photon_diagnostics/Spectrometer/WavelengthSpan'][()]
        padres_wavelength = DictionaryObject['/photon_diagnostics/Spectrometer/Wavelength'][()] + 0.0575
        padres_pixel2micron = DictionaryObject['/photon_diagnostics/Spectrometer/Pixel2micron'][()]
        fel_lambda = padres_wavelength + np.arange(-500, 500) * padres_pixel2micron * padres_span / 1000

        L = 0.5  # include all data points from 0 < L*max < max
        above_half_max = fel_spectrum > np.max(fel_spectrum) * L
        moment_0 = np.sum(fel_lambda**0 * fel_spectrum * above_half_max, axis=1)
        moment_1 = np.sum(fel_lambda**1 * fel_spectrum * above_half_max, axis=1)
        moment_2 = np.sum(fel_lambda**2 * fel_spectrum * above_half_max, axis=1)
        
        biased_sigma = np.sqrt(1/moment_0 * (moment_2 - moment_1**2/moment_0))
        bias_correction = 1 / np.sqrt(1 - np.sqrt(-np.log(L)/np.pi) * 2*L / (erf(np.sqrt(-np.log(L)))) )
        sigma = biased_sigma * bias_correction
        mu = moment_1 / moment_0

        return sigma

    elif keyword=='seed_wavelengths_mu':
        seed_spectrum = DictionaryObject['photon_source/SeedLaserSpectrum_FEL01/WaveMeta'][()]
        seed_lambda = DictionaryObject['photon_source/SeedLaserSpectrum_FEL01/LambdaMeta'][()]
        
        L = 0.5  # include all data points from 0 < L*max < max
        above_half_max = seed_spectrum > np.max(seed_spectrum) * L
        moment_0 = np.sum(seed_lambda**0 * seed_spectrum * above_half_max)
        moment_1 = np.sum(seed_lambda**1 * seed_spectrum * above_half_max)

        mu = moment_1 / moment_0

        return mu

    elif keyword=='seed_wavelengths_sigma':
        seed_spectrum = DictionaryObject['photon_source/SeedLaserSpectrum_FEL01/WaveMeta'][()]
        seed_lambda = DictionaryObject['photon_source/SeedLaserSpectrum_FEL01/LambdaMeta'][()]
        
        L = 0.5
        above_half_max = seed_spectrum > np.max(seed_spectrum) * L
        moment_0 = np.sum(seed_lambda**0 * seed_spectrum * above_half_max)
        moment_1 = np.sum(seed_lambda**1 * seed_spectrum * above_half_max)
        moment_2 = np.sum(seed_lambda**2 * seed_spectrum * above_half_max)
        
        biased_sigma = np.sqrt(1/moment_0 * (moment_2 - moment_1**2/moment_0))
        bias_correction = 1 / np.sqrt(1 - np.sqrt(-np.log(L)/np.pi) * 2*L / (erf(np.sqrt(-np.log(L)))) )
        sigma = biased_sigma * bias_correction
        mu = moment_1 / moment_0

        return sigma

    elif keyword=='fel_wavelengths':
        padres_span = DictionaryObject['/photon_diagnostics/Spectrometer/WavelengthSpan'][()]
        padres_wavelength = DictionaryObject['/photon_diagnostics/Spectrometer/Wavelength'][()] + 0.0575
        padres_pixel2micron = DictionaryObject['/photon_diagnostics/Spectrometer/Pixel2micron'][()]
        padres_lambda = padres_wavelength + np.arange(-500, 500) * padres_pixel2micron * padres_span / 1000

        return padres_lambda

    elif keyword=='total_retardation':
        voltage_1 = DictionaryObject['endstation/MagneticBottle/voltage_ch1'][()]
        voltage_2 = DictionaryObject['endstation/MagneticBottle/voltage_ch2'][()]
        voltage_3 = DictionaryObject['endstation/MagneticBottle/voltage_ch3'][()]
        voltage_1_on = DictionaryObject['endstation/MagneticBottle/ch1_is_enabled'][()]
        voltage_2_on = DictionaryObject['endstation/MagneticBottle/ch2_is_enabled'][()]
        voltage_3_on = DictionaryObject['endstation/MagneticBottle/ch3_is_enabled'][()]
        retardation = voltage_1*voltage_1_on + voltage_2*voltage_2_on - voltage_3*voltage_3_on

        return retardation

    
    elif keyword=='bunch_parity':
        bunches = DictionaryObject['bunches'][()]
        parity = bunches%2==0

        return parity
    

    else:
        return DictionaryObject[aliasFunc(keyword)]




def spectra_subtraction(foreground,background):
    return -(foreground-background)

def remove_slu_cycling(data):
    '''
    Remove the part corresponding to the keyword "slu_sep=True" in the Run() methods.
    For reference:
        data = (ff_fs, bf_fs, ff_bs, bf_bs)
    where:
        ff = FEL ON  (foreground fel)
        bf = FEL OFF (background fel)

        _fs = SLU ON  (foreground slu)
        _bs = SLU OFF (background slu)
    '''

    return data[:2]

def swap_rules_runs(data, single_rule=False, single_run=False, single_shot = False, file_level=False):
    '''
    Takes either the axes conditions:
        axes = (conditions, runs, rules, data)
    and returns the axes:
        axes = (conditions, rules, runs, data)
    OR the axes conditions:
        axes = (conditions, rules, data)
    and returns the axes:
        axes = (conditions, rules, data)

   IMPORTANT: 
        The names "single_rule" and "single_run" make sense ONLY for the averaging functions
            e.g. Run.average_rundata_weights()
            i.e. the data has axes average_data = (conditions, runs, rules, shot_data).
        When you use this on the file-yielding generators, the axes are different
            e.g. Run.yield_filedata()
            i.e. the data has axes file_data = (conditions, rules, shot_data).
        So when using this on the file-yielding generators, treat 
            "single_run" -> "single_rule"
            "single_rule"-> "single_shot"

    single_rule : bool (optional)
        if True, collapses the "rules" dimension of the data and only gives the first element
    '''
    output = []
    for condition in data:
        ndim = np.ndim(data[0])

        if file_level:
            if ndim < 2:
                raise Exception(f'ndim of condition ({ndim}) should be >=2 if file_level=True')

            transposed = np.array(condition)
            if single_shot:
                transposed = transposed[:,0]
            if single_rule:
                transposed = transposed[0]
            output.append(np.array(transposed))

        elif not file_level and ndim < 2:
            raise Exception(f'ndim of condition ({ndim}) should be >=2 if file_level=False')
        else:

            transposed = np.array(np.swapaxes(condition, 1,0))
            if single_shot and ndim < 4:
                print('single_shot keyword not valid here')
            elif single_shot:
                transposed = transposed[:,:,0]
            if single_run:
                transposed = transposed[:,0]
            if single_rule:
                transposed = transposed[0]
            output.append(np.array(transposed))

    return output

def simplify_data(data, single_rule=False, single_run=False, file_level=False):
    return swap_rules_runs(remove_slu_cycling(data), 
                           single_rule=single_rule, single_run=single_run, file_level=file_level)

def nm_to_ev(nm):
    '''Convert from nm to eV.'''
    return spc.h*spc.c/spc.nano/spc.e/nm

def ev_to_nm(eV):
    '''Convert from eV to nm.'''
    return spc.h*spc.c/spc.nano/spc.e/eV

# %%
"""
### Alias definitions
"""

# %%
# Figure bookkeeping to save memory
figs = {}
def newfig(id, *args, **kwargs):
    id = 0
    if id in figs:
        plt.close(figs[id].number)
    fig, ax = plt.subplots(*args, **kwargs)
    figs.update({id: fig})
    return fig, ax

# Alternative names for the HDF5 groupnames
alias_dict = {
    'i0m' : 'photon_diagnostics/FEL01/I0_monitor/iom_sh_a',
    'i0m_current' : 'photon_diagnostics/FEL01/I0_monitor/iom_sh_a_pc',
    'vmi' : 'vmi/andor',
    'ion_tof' : 'digitizer/channel1',
    'delay' : 'user_laser/delay_line/position',
    'slu' : 'user_laser/energy_meter/Energy2',
    'fel_spectrometer' : 'photon_diagnostics/Spectrometer/hor_spectrum',
    'fel_wavelength' : 'photon_source/FEL01/wavelength',
    'seed_spectrometer' : 'photon_source/SeedLaserSpectrum_FEL01/WaveMeta',
    'seed_wavelength' : 'photon_source/SeedLaser/Wavelength',
    'seed_wavelengths' : 'photon_source/SeedLaserSpectrum_FEL01/LambdaMeta',
    'harmonic_number' : 'photon_source/FEL01/harmonic_number',
    'bunch_number' : 'bunches',
    'pressure' : 'photon_diagnostics/FEL01/Gas_Attenuator/Pressure',
    'poletto' : 'cosp/HorSpectrum',
    }

# %%
"""
# ------------------------------------------------------------------------------------------------
# ! Data selection ! -----------------------------------------------------------------------------

This block contains the variables you might change every different Run. 
Changing "ion_tof_range" or "eon_tof_range" __does not__ make the program run faster; we are limited
by the compression in FERMI's HDF5 files. If working memory is a problem, then decrease these
ranges.
"""

# %%
# BEAMTIME_DIR =  '/net/online4ldm/store/20209112b/results/TestData/'
BEAMTIME_DIR =  'TestBeamtime/'
DATA_DIR = BEAMTIME_DIR+'Beamtime/'  # change from fictitious to the real raw data directory!
SAVE_DIR = BEAMTIME_DIR+'results/evaluation/'#'/net/online4ldm/store/20209134/results/results' # ditto

SAVE_FILES = False

BACKGROUND = True  # Only set to False if you want to sum up everything
NAMEADD = 'test' # your name here
run_numbers = np.arange(1,3)


# variables for data extraction ans rebinning
ION_TOF_REBIN = 10
ion_tof_range = (4000, 30000, 1) # select ion tof range for plotting
new_ion_mq = np.linspace(0.1,200,num=1200)

EON_TOF_REBIN = 1
eon_tof_range = (4000, 10000, 1)
new_eKE = np.linspace(0.5, 50, num=400)

ion_tof_slices = [ion_tof_range]
eon_tof_slices = [eon_tof_range]

ion_tof = np.arange(*ion_tof_slices[0])
rebin_ion_tof = ion_tof[::ION_TOF_REBIN]
eon_tof = np.arange(*eon_tof_slices[0])
rebin_eon_tof = eon_tof[::EON_TOF_REBIN]

MAKE_CACHE = True
LOAD_FROM_CACHE = False

calibration_run_number = 1

print(run_numbers)

# %%
"""
Create RunCollection (main data structure), and print location of our save directory
"""

# %%
# This block loads all the relevent HDF5 filepaths into their respective Run
# (Each Run has more than a single HDF5 file! Usually less than 100.)

RunCollection = {}  # We will put all the 'Runs' in thes dictionary
for run_id in (list(run_numbers) + [calibration_run_number,]):
    folderpath = os.path.join(DATA_DIR, f'Run_{run_id:03d}/rawdata')
    filepaths = [folderpath+'/'+filename for filename in os.listdir(folderpath)[::]]
    RunCollection[run_id] = Run(filepaths,
                                alias_dict=alias_dict, search_symbols=search_symbols,
                                keyword_functions=keyword_functions,
                                )  # create a Run object with its respective filepaths

# This creates a set out of the run_numbers selected above
Set1 = RunSets([])
for run in run_numbers:
    Set1.add([RunCollection[run]])
print(f'Data set contains {len(Set1.run_instances)} run(s).')

if len(run_numbers) > 1:
    run_string = f"run_{min(run_numbers):04d}-{max(run_numbers):04d}"
elif run_numbers:
    run_string = f"run_{run_numbers[0]:04d}"
else:
    raise IndexError('no run numbers???')

prefix = os.path.join(SAVE_DIR, run_string)
outdir = (prefix + '_' + NAMEADD).rstrip('_')
print(f'Save directory: ...{outdir[30:]}')

# %%
"""
Create directory if non-existent (and if we are actually saving files)
"""

# %%
if SAVE_FILES:
    if not os.path.exists(outdir):
        os.mkdir(outdir)

# %%
"""
# ------------------------------------------------------------------------------------------------
# Show the average background-subtracted electron TOF for each Run ---------------------

The output for Runset.averageRunData and Runset.average_run_data_weights has the
axes shape (rule, condition, run, data):
"rule" are the filtering rules
"condition" is in the order (FEL:ON SLU:ON, FEL:OFF SLU:ON, FEL:ON SLU:OFF, FEL:OFF SLU:OFF)
"run" are the individual Runs
"data" is the average rundata/weights
"""

# %%
runset_ion_tof_data = Set1.average_run_data('ion_tof', back_sep=BACKGROUND,
                                    slice_range=ion_tof_slices,
                                    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
fore_ion_rundata, back_ion_rundata = simplify_data(runset_ion_tof_data, single_rule=True)

# %%
overall_integral_eKE = []
# fel_energys = nm_to_ev(fel_wavelengths)

subt_ion_tof_rundata = -(fore_ion_rundata - back_ion_rundata)
rebin_ion_tof_rundata = rebinning(rebin_ion_tof, ion_tof, subt_ion_tof_rundata, axis=1)

fig, ax = plt.subplots(1,1,figsize=(12,4))
for (runnumber, ion_spectrum_tof) in zip(
    run_numbers, rebin_ion_tof_rundata):
    ax.plot(rebin_ion_tof, ion_spectrum_tof, label=f"Run_{runnumber:03d}")

ax.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)
ax.set_xlabel('ion TOF')
ax.set_ylabel('ion TOF signal; rebinned (arb.u.)')
ax.set_title(f'Runs {run_numbers[0]}-{run_numbers[-1]} Average of the complete Run')

# if SAVE_FILES:
#     fig.savefig(outdir+'/Average_of_complete_run.png')
#     fig1.savefig(outdir+'/Average_of_complete_run_eV.png')
ax.set_ylim(-1,1)

plt.show()

# %%

def closest(locs, array):
    indices = [np.where(np.min((loc-array)**2) == (loc-array)**2)[0][0] for loc in locs]
    return np.array(indices)

ion_tof_mq_peaks = np.array([
    # [5000, 999],
    [6000, 0],
    [10500, 14],
    [12000, 28],
    [13100, 36],

])
tof_points, mq_points = ion_tof_mq_peaks.T

ion_cal_rundata = RunCollection[calibration_run_number].average_run_data('ion_tof', back_sep=BACKGROUND,
                                    slice_range=ion_tof_slices,
                                    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
fore_ion_rundata, back_ion_rundata = simplify_data(ion_cal_rundata)
cal_sub_spectrum = back_ion_rundata[:,0] - fore_ion_rundata[:,0]


ion_calibration_dict = tof_mq_calibration(peaks=ion_tof_mq_peaks)
(tof_mq_coor_func, tof_mq_jaco_func,
 mq_tof_coor_func, mq_tof_jaco_func,
 ion_constants_dict) = list(ion_calibration_dict.values())
print(f'calibration constants:  {ion_constants_dict}')
ion_constants = ion_constants_dict['timezero'], ion_constants_dict['C']

model_tof = np.linspace(np.min(tof_points), np.max(tof_points), num=1000)

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,4))
ax1.plot(tof_points, cal_sub_spectrum[closest(tof_points, ion_tof)], marker='v', linestyle='')
ax1.plot(ion_tof, cal_sub_spectrum)
# ax1.set_xlim(5000,7000)
ax1.set_title('calibration points')
ax1.set_xlabel('tof (ns)')
ax1.set_ylabel('tof (ns)')
ax2.plot(tof_points, mq_points, marker='o', linestyle='')
ax2.plot(model_tof, tof_mq_coor_func(model_tof), color='black')
ax2.set_title('calibration fit')
ax2.set_xlabel('tof (ns)')
ax2.set_ylabel('mq (m/q)')
plt.show()



# %%
print(f"Using ion constants: (t0, C) = {ion_constants}")
# print(f"Using eon constants: (t0, C, E0) = {eon_constants}")

ion_calibration_dict = tof_mq_calibration(constants=ion_constants)
(tof_mq_coor_func, tof_mq_jaco_func,
 mq_tof_coor_func, mq_tof_jaco_func,
 ion_constants_dict) = list(ion_calibration_dict.values())

# eon_calibration_dict = tof_ke_calibration(constants=eon_constants)
# (tof_ke_coor_func, tof_ke_jaco_func,
#  ke_tof_coor_func, ke_tof_jaco_func,
#  eon_constants_dict) = list(eon_calibration_dict.values())

def transpose_axis(y, axis=None):
    if (axis is None) or (np.ndim(y)==1):
        transpose = y
    else:
        transpose_order = np.arange(np.ndim(y))
        if axis!=0:
            transpose_order[0]=axis
            transpose_order[axis]=0
        transpose = np.transpose(y, axes=transpose_order)
    return transpose

# def tof_to_eke(tof, spectrum, axis=None):
#     """ Helper function that converts TOF into eKE spectra with the Jacobian correction """
#     spectrum = transpose_axis(spectrum, axis=axis)
#     eke = tof_ke_coor_func(tof)
#     mask = eke>eon_constants_dict['KE0']
#     jacobian = tof_ke_jaco_func(tof)
#     if np.ndim(spectrum)>1:
#         jacobian = jacobian[:,np.newaxis]
#     eke_coor = eke[mask]
#     eke_spec = (spectrum * jacobian)[mask]
#     eke_spec = transpose_axis(eke_spec, axis=axis)  # revert transposition
#     return eke_coor, eke_spec

# def eke_to_tof(eke, spectrum, axis=None):
#     """ Helper function that converts eKE into TOF spectra with the Jacobian correction """
#     spectrum = transpose_axis(spectrum, axis=axis)
#     tof = ke_tof_coor_func(eke)
#     mask = eke>0
#     jacobian = ke_tof_jaco_func(eke)
#     if np.ndim(spectrum)>1:
#         jacobian = jacobian[:,np.newaxis]
#     tof_coor = tof[mask]
#     tof_spec = (spectrum * jacobian)[mask]
#     tof_spec = transpose_axis(tof_spec, axis=axis)  # revert transposition
#     return tof_coor, tof_spec

def tof_to_mq(tof, spectrum, axis=None):
    """ Helper function that converts TOF into eKE spectra with the Jacobian correction """
    spectrum = transpose_axis(spectrum, axis=axis)
    mq = tof_mq_coor_func(tof)
    mask = tof>ion_constants_dict['timezero']
    jacobian = tof_mq_jaco_func(tof)
    if np.ndim(spectrum)>1:
        jacobian = jacobian[:,np.newaxis]
    mq_coor = mq[mask]
    mq_spec = (spectrum * jacobian)[mask]
    mq_spec = transpose_axis(mq_spec, axis=axis)  # revert transposition
    return mq_coor, mq_spec

def mq_to_tof(eke, spectrum, axis=None):
    """ Helper function that converts eKE into TOF spectra with the Jacobian correction """
    spectrum = transpose_axis(spectrum, axis=axis)
    tof = mq_tof_coor_func(eke)
    mask = tof>ion_constants_dict['timezero']
    jacobian = mq_tof_jaco_func(mq)
    if np.ndim(spectrum)>1:
        jacobian = jacobian[:,np.newaxis]
    tof_coor = tof[mask]
    tof_spec = (spectrum * jacobian)[mask]
    tof_spec = transpose_axis(tof_spec, axis=axis)  # revert transposition
    return tof_coor, tof_spec

# %%

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,4))
for (runnumber, ion_spectrum_tof) in zip(
    run_numbers, rebin_ion_tof_rundata):
    ax1.plot(rebin_ion_tof, ion_spectrum_tof, label=f"Run_{runnumber:03d}")

ax1.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)
ax1.set_xlabel('ion TOF')
ax1.set_ylabel('ion TOF signal; rebinned (arb.u.)')
ax1.set_title(f'Runs {run_numbers[0]}-{run_numbers[-1]} Average of the complete Run')
ax1.set_yscale('log')
ylim = ax1.set_ylim()
ax1.set_ylim(ylim[1]*1e-4, ylim[1])

for (runnumber, ion_spectrum_tof) in zip(
    run_numbers, rebin_ion_tof_rundata):
    mq_coor, mq_spectrum = tof_to_mq(rebin_ion_tof, -ion_spectrum_tof)
    rebin_mq = np.linspace(0.1, 70, num=1000)
    rebin_mq_spectrum = rebinning(rebin_mq, mq_coor, mq_spectrum)
    ax2.plot(rebin_mq, rebin_mq_spectrum, label=f"Run_{runnumber:03d}")

ax2.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)
ax2.set_xlabel('mq')
ax2.set_ylabel('ion TOF signal; rebinned (arb.u.)')
ax2.set_yscale('log')
ylim = ax2.set_ylim()
ax2.set_ylim(ylim[1]*1e-4, ylim[1])
ax2.set_title(f'Runs {run_numbers[0]}-{run_numbers[-1]} Average of the complete Run')

# %%
"""
# ------------------------------------------------------------------------------------------------
# I0M filtering -----------------------------------------------------------------------------------


"""

# %%
raw_i0m_rundata = Set1.give_rundata('i0m', make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
try:
    i0m_runset_data, _ = simplify_data(raw_i0m_rundata, single_rule=True)  # can use simplify_data, because no rules
except:
    fore_rundata_i0m, back_rundata_iom, *_ = raw_i0m_rundata
    i0m_runset_data = fore_rundata_i0m
    for i in range(len(i0m_runset_data)):  # collapse the rule dimension
        i0m_runset_data[i] = i0m_runset_data[i][0]

# %%
# Check the range of possible I0M intensities here; change I0M binning in the next block if needed!
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(8,3))
for runnumber, i0m_run_data in zip(run_numbers, i0m_runset_data):
    i0m_data = i0m_run_data[:,0]  # just collapsing an extraneous dimension
    ax1.plot(i0m_data, marker='o', markersize=1, linestyle='', label=f'Run_{runnumber:03d}')
    ax2.hist(i0m_data, bins=np.linspace(min(i0m_data),max(i0m_data),num=100),
             label=f'Run_{runnumber:03d}')
ax1.set_ylabel('I0M intensity (uJ)')
ax1.set_xlabel('shot number')
ax1.set_title(f'Runs {run_numbers[0]}-{run_numbers[-1]} I0M over time')
#ax1.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)

ax2.set_ylabel('binned counts')
ax2.set_xlabel('I0M (uJ)')
ax2.set_title(f'Runs {run_numbers[0]}-{run_numbers[-1]} Histogram of I0M')
#ax2.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)
plt.tight_layout()

if SAVE_FILES:
    plt.savefig(outdir+'/I0M_time_and_bins.png')
plt.show()

# %%
# %%time # uncomment to show time
runset_vmi = Set1.average_run_data('vmi',back_sep=BACKGROUND,
                                    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
fore_vmi, back_vmi = simplify_data(runset_vmi, single_rule=True, single_run=False)

# %%
sub_vmi = fore_vmi - back_vmi
print(np.shape(sub_vmi))
plt.imshow(np.average(sub_vmi, axis=0))
plt.show()

