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

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
from fermi_libraries.run_module import Run, RunSets
from fermi_libraries.common_functions import (
    rebinning, simplify_data, name_from_runs, set_recursion_limit)
from fermi_libraries.calibration_tools import (
    tof_to_mq_conversion, mq_to_tof_conversion)
from fermi_libraries.dictionary_search import search_symbols

# %%
"""
### Function definitions (that you might change)
"""

# %%
@set_recursion_limit(1)
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

---

# ! Data selection !

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

calibration_run_number = 1

print(run_numbers)

# %%
"""
Create RunCollection (main data structure), and print location of our save directory
"""

# %%
# This block loads all the relevent HDF5 filepaths into their respective Run.
RunCollection = {}  # We will put all the 'Runs' in thes dictionary
for run_id in (list(run_numbers) + [calibration_run_number,]):
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

---

# Show Run-averaged background-subtracted ion TOF

The output for Runset.averageRunData and Runset.average_run_data_weights has the
axes shape (rule, condition, run, data):
"rule" are the filtering rules
"condition" is in the order (FEL:ON SLU:ON, FEL:OFF SLU:ON, FEL:ON SLU:OFF, FEL:OFF SLU:OFF)
"run" are the individual Runs
"data" is the average rundata/weights
"""

# %%
raw_i0m_rundata = BasicRunSet.give_rundata('i0m', make_cache=False, use_cache=False)
try:
    i0m_runset_data, _ = simplify_data(raw_i0m_rundata, single_rule=True)  # can use simplify_data, because no rules
except:
    fore_rundata_i0m, back_rundata_iom, *_ = raw_i0m_rundata
    i0m_runset_data = fore_rundata_i0m
    for i in range(len(i0m_runset_data)):  # collapse the rule dimension
        i0m_runset_data[i] = i0m_runset_data[i][0]


plt.plot(i0m_runset_data[0,:,0])
plt.show()

# %%
"""
Define rules for filtering here
"""

# %%
i0m_edges = np.linspace(-4.5, -3.0, num=4)
i0m_bins = i0m_edges[:-1]
i0m_filter_rules = [f'(i0m>{lo} & i0m<{hi})' for lo, hi in zip(i0m_edges[:-1], i0m_edges[1:])]
print(f'i0m filter rules: {i0m_filter_rules}')

# %%
"""
Get ion TOF spectra, binned by each of the filtering rules.
"""

# %%
runset_ion_tof_data = BasicRunSet.average_run_data('ion_tof', back_sep=BACKGROUND,
                                    slice_range=ion_tof_slices,
                                    rules=i0m_filter_rules,
                                    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
fore_ion_tof_rawdata, back_ion_tof_rawdata = simplify_data(runset_ion_tof_data, single_rule=False)
print(f'shape is (rules, runs, data): {np.shape(fore_ion_tof_rawdata)}')

# %%
subt_ion_tof_rawdata = -(fore_ion_tof_rawdata - back_ion_tof_rawdata)
subt_ion_tof_spectra = rebinning(ion_tof, raw_ion_tof, subt_ion_tof_rawdata, axis=2)

for rule, collected_data in zip(i0m_filter_rules, subt_ion_tof_spectra):
    plt.figure(figsize=(5,2))
    for run_number, data in zip(run_numbers, collected_data):
        plt.plot(ion_tof, data, label=f'Run {run_number:03d}')
    plt.legend()
    plt.title(f'Ion TOF spectra w/ rule: {rule}')
    plt.xlabel('ion TOF (ns)')
    plt.xlim(8000, 15000)
    plt.show()

# %%
"""
Use calibration constants for ion TOF -> ion mass/charge spectra
"""

# %%
ion_t0 = 6059.316278073492
ion_propconst = 7.440783535983542e-07 
ion_constants = ion_t0, ion_propconst

print(f"Using ion constants: (t0, C) = {ion_constants}")
tof_to_mq = lambda tof, spec, axis=None: tof_to_mq_conversion(tof, spec, *ion_constants, axis=axis)
mq_to_tof = lambda mq, spec, axis=None: mq_to_tof_conversion(mq, spec, *ion_constants, axis=axis)

# %%
mq_raw_coor, mq_raw_spectrum = tof_to_mq(raw_ion_tof, subt_ion_tof_rawdata, axis=2)
mq_coor = np.linspace(0.1, 70, num=1000)
mq_spectra = rebinning(mq_coor, mq_raw_coor, mq_raw_spectrum, axis=2)

for rule, collected_mq_data in zip(i0m_filter_rules, mq_spectra):
    fig, ax = plt.subplots(1, 1, figsize=(6,2))
    for run_number, data in zip(run_numbers, collected_mq_data):
        ax.plot(mq_coor, data, label=f'Run {run_number:03d}')
    ax.legend()
    ax.set_title(f'Ion mass/charge spectra w/ rule: {rule}')
    ax.set_xlabel('m/q')
    ax.set_xlim(0, 40)
    plt.show()

# %%
"""
Perform filtering rules on VMI data here
"""

# %%
runset_vmi_data = BasicRunSet.average_run_data('vmi', back_sep=BACKGROUND,
                                    rules=i0m_filter_rules,
                                    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
fore_vmi_rawdata, back_vmi_rawdata = simplify_data(runset_vmi_data, single_rule=False)
print(f'shape is (rules, runs, data): {np.shape(fore_ion_tof_rawdata)}')

# %%
subt_vmi_rawdata = (fore_vmi_rawdata - back_vmi_rawdata)

for rule, collected_data in zip(i0m_filter_rules, subt_vmi_rawdata):
    fig, axes = plt.subplots(1, len(run_numbers), figsize=(6,2))
    axes[0].set_ylabel(f'VMI filter rule:\n{rule}')
    for ax, run_number, data in zip(axes, run_numbers, collected_data):
        cax = ax.imshow(data, label=f'Run {run_number:03d}')
        fig.colorbar(cax, ax=ax)
        ax.set_title(f'Run {run_number:03d}')
    plt.tight_layout()
    plt.show()
