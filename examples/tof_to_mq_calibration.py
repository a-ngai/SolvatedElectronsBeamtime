# %%
"""
# Set-up for ion-m/q Calibration
"""

# %%
"""
## Import statements
"""

# %%
# uncomment the following line when you want to interact with the matplotlib plots
#%matplotlib widget

import os

import numpy as np
import matplotlib.pyplot as plt
from fermi_libraries.run_module import Run, RunSets
from fermi_libraries.common_functions import (
    rebinning, tof_mq_calibration, simplify_data, 
    tof_to_mq_conversion, mq_to_tof_conversion,
    tof_mq_coordinate_func, mq_tof_coordinate_func,
    name_from_runs,
    set_default_labels,
    closest)
from fermi_libraries.dictionary_search import search_symbols

# %%
"""
### Function definitions (that you might change)
"""

# %%

def keyword_functions(keyword, aliasFunc, DictionaryObject):
    return DictionaryObject[aliasFunc(keyword)]

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

ion_tof_slices = [ion_tof_range]

raw_ion_tof = np.arange(*ion_tof_slices[0])
ion_tof = raw_ion_tof[::ION_TOF_REBIN]

MAKE_CACHE = True
LOAD_FROM_CACHE = False

CALIBRATION_RUN_NUMBER = 1

print(run_numbers)

# %%
"""
Create RunCollection (main data structure), and print location of our save directory
"""

# %%
# This block loads all the relevent HDF5 filepaths into their respective Run.
RunCollection = {}  # We will put all the 'Runs' in thes dictionary
for run_id in (list(run_numbers) + [CALIBRATION_RUN_NUMBER,]):
    folderpath = os.path.join(DATA_DIR, f'Run_{run_id:03d}/rawdata')
    filepaths = [folderpath+'/'+filename for filename in os.listdir(folderpath)[::]]
    RunCollection[run_id] = Run(filepaths,
                                alias_dict=alias_dict, search_symbols=search_symbols,
                                keyword_functions=keyword_functions,
                                )  # create a Run object with its respective filepaths

# This creates a set out of the run_numbers selected above
BasicRunSet = RunSets([])
for run in run_numbers:
    BasicRunSet.add([RunCollection[run]])
print(f'Data set contains {len(BasicRunSet.run_instances)} run(s).')

run_name = f'Runs {run_numbers[0]}-{run_numbers[-1]}'
run_string = name_from_runs(run_numbers)
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
runset_ion_tof_data = BasicRunSet.average_run_data('ion_tof', 
    back_sep=BACKGROUND, slice_range=ion_tof_slices,
    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
fore_ion_tof_rawdata, back_ion_tof_rawdata = simplify_data(runset_ion_tof_data, single_rule=True)

# %%
subt_ion_tof_rawdata = -(fore_ion_tof_rawdata - back_ion_tof_rawdata)
ion_tof_spectra = rebinning(ion_tof, raw_ion_tof, subt_ion_tof_rawdata, axis=1)

fig, ax = plt.subplots(1,1,figsize=(12,4))
for (runnumber, ion_tof_spectrum) in zip(run_numbers, ion_tof_spectra):
    ax.plot(ion_tof, ion_tof_spectrum, label=f"Run_{runnumber:03d}")
ax.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)
ax.set_xlabel('ion TOF')
ax.set_ylabel('ion TOF signal; rebinned (arb.u.)')
ax.set_title(f'{run_name}: run averages')
ax.set_ylim(-1,1)

if SAVE_FILES: fig.savefig(outdir+'/Average_of_complete_run.png')
plt.show()

# %%

ion_tof_mq_peaks = np.array([
    # [5000, 999],
    [6000, 0],
    [10500, 14],
    [12000, 28],
    [13100, 36],
])
tof_points, mq_points = ion_tof_mq_peaks.T

ion_cal_rawdata = RunCollection[CALIBRATION_RUN_NUMBER].average_run_data('ion_tof', 
    back_sep=BACKGROUND, slice_range=ion_tof_slices,
    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
fore_ion_rundata, back_ion_rundata = simplify_data(ion_cal_rawdata)
cal_sub_spectrum = back_ion_rundata[:,0] - fore_ion_rundata[:,0]

ion_calibration_dict = tof_mq_calibration(peaks=ion_tof_mq_peaks)
(_, _, _, _, ion_constants_dict) = list(ion_calibration_dict.values())
print(f'calibration constants:  {ion_constants_dict}')
ion_constants = ion_constants_dict['timezero'], ion_constants_dict['C']
tof_mq_coor_func = lambda tof: tof_mq_coordinate_func(tof, *ion_constants)
mq_tof_coor_func = lambda mq: mq_tof_coordinate_func(mq, *ion_constants)
tof_to_mq = lambda tof, spec, axis=None: tof_to_mq_conversion(tof, spec, *ion_constants, axis=axis)
mq_to_tof = lambda mq, spec, axis=None: mq_to_tof_conversion(mq, spec, *ion_constants, axis=axis)

model_tof = np.linspace(np.min(tof_points), np.max(tof_points), num=1000)
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,4))
ax1.plot(tof_points, cal_sub_spectrum[closest(tof_points, ion_tof)], marker='v', linestyle='')
ax1.plot(raw_ion_tof, cal_sub_spectrum)
# ax1.set_xlim(5000,7000)
set_default_labels(ax1, title='calibration points', xlabel='tof (ns)', ylabel='tof (ns)')
ax2.plot(tof_points, mq_points, marker='o', linestyle='')
ax2.plot(model_tof, tof_mq_coor_func(model_tof), color='black')
set_default_labels(ax2, title='calibration fit', xlabel='tof (ns)', ylabel='m/q')
plt.show()


# %%

mq_raw_coor, mq_raw_spectra = tof_to_mq(ion_tof, ion_tof_spectra, axis=1)
mq_coor = np.linspace(0.1, 70, num=1000)
mq_spectra = rebinning(mq_coor, mq_raw_coor, mq_raw_spectra, axis=1)

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,4))
for (runnumber, ion_tof_spec_i) in zip(run_numbers, ion_tof_spectra):
    ax1.plot(ion_tof, ion_tof_spec_i, label=f"Run_{runnumber:03d}")
ax1.legend()
ax1.set_xlabel('ion TOF')
ax1.set_ylabel('ion TOF signal; rebinned (arb.u.)')
ax1.set_title(f'{run_name}: run averages')
ax1.grid()

for (runnumber, mq_spec_i) in zip(run_numbers, mq_spectra):
    ax2.plot(mq_coor, mq_spec_i, label=f"Run_{runnumber:03d}")
ax2.legend()
ax2.set_xlabel('m/q')
ax2.set_ylabel('ion TOF signal; rebinned (arb.u.)')
ax2.set_title(f'{run_name}: run averages')
ax2.grid()
plt.show()
