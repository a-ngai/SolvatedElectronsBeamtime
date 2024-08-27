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
cmap = colormaps.get_cmap('plasma')
from scipy.special import erf
from fermi_libraries.run_module import Run, RunSets
from fermi_libraries.common_functions import (
    rebinning, tof_mq_calibration, simplify_data, 
    tof_to_mq_conversion, mq_to_tof_conversion,
    name_from_runs,
    avg_from_moments, stdev_from_moments,
    set_default_labels,
    set_recursion_limit,
    closest)
from fermi_libraries.dictionary_search import search_symbols

# %%
"""
### Function definitions (that you might change)
"""

# %%


@set_recursion_limit(1)
def keyword_functions(keyword, aliasFunc, DictionaryObject):

    if False:
        pass

    elif keyword=='bunch_parity':
        bunches = DictionaryObject['bunches'][()]
        parity = bunches%2==0
        return parity

    elif keyword=='fel_wavelengths':
        padres_span = DictionaryObject['/photon_diagnostics/Spectrometer/WavelengthSpan'][()]
        padres_wavelength = DictionaryObject['/photon_diagnostics/Spectrometer/Wavelength'][()] + 0.0575
        padres_pixel2micron = DictionaryObject['/photon_diagnostics/Spectrometer/Pixel2micron'][()]
        padres_lambda = padres_wavelength + np.arange(-500, 500) * padres_pixel2micron * padres_span / 1000
        return padres_lambda
    
    elif keyword=='fel_wavelengths_avg':
        fel_lambda = keyword_functions('fel_wavelengths', aliasFunc, DictionaryObject)
        fel_spectrum = DictionaryObject['photon_diagnostics/Spectrometer/hor_spectrum'][()]
        average = avg_from_moments(fel_lambda, fel_spectrum, L=0.5)
        return average

    elif keyword=='fel_wavelengths_stdev':
        fel_lambda = keyword_functions('fel_wavelengths', aliasFunc, DictionaryObject)
        fel_spectrum = DictionaryObject['photon_diagnostics/Spectrometer/hor_spectrum'][()]
        stdev = stdev_from_moments(fel_lambda, fel_spectrum, L=0.5)
        return stdev

    elif keyword=='seed_wavelengths_avg':
        seed_spectrum = DictionaryObject['photon_source/SeedLaserSpectrum_FEL01/WaveMeta'][()]
        seed_lambda = DictionaryObject['photon_source/SeedLaserSpectrum_FEL01/LambdaMeta'][()]
        average = avg_from_moments(seed_lambda, seed_spectrum, L=0.5)
        return average

    elif keyword=='seed_wavelengths_stdev':
        seed_spectrum = DictionaryObject['photon_source/SeedLaserSpectrum_FEL01/WaveMeta'][()]
        seed_lambda = DictionaryObject['photon_source/SeedLaserSpectrum_FEL01/LambdaMeta'][()]
        stdev = stdev_from_moments(seed_lambda, seed_spectrum, L=0.5)
        return stdev

    elif keyword=='total_retardation':
        voltage_1 = DictionaryObject['endstation/MagneticBottle/voltage_ch1'][()]
        voltage_2 = DictionaryObject['endstation/MagneticBottle/voltage_ch2'][()]
        voltage_3 = DictionaryObject['endstation/MagneticBottle/voltage_ch3'][()]
        voltage_1_on = DictionaryObject['endstation/MagneticBottle/ch1_is_enabled'][()]
        voltage_2_on = DictionaryObject['endstation/MagneticBottle/ch2_is_enabled'][()]
        voltage_3_on = DictionaryObject['endstation/MagneticBottle/ch3_is_enabled'][()]
        retardation = voltage_1*voltage_1_on + voltage_2*voltage_2_on - voltage_3*voltage_3_on
        return retardation

    else:
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

EON_TOF_REBIN = 1
eon_tof_range = (4000, 10000, 1)
new_eKE = np.linspace(0.5, 50, num=400)

ion_tof_slices = [ion_tof_range]
eon_tof_slices = [eon_tof_range]

raw_ion_tof = np.arange(*ion_tof_slices[0])
ion_tof = raw_ion_tof[::ION_TOF_REBIN]
raw_eon_tof = np.arange(*eon_tof_slices[0])
eon_tof = raw_eon_tof[::EON_TOF_REBIN]

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

# %% testing here, delete when done!

runset_ion_tof_data = BasicRunSet.average_run_data('fel_wavelengths_avg', back_sep=BACKGROUND,
                                    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)


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
runset_ion_tof_data = BasicRunSet.average_run_data('ion_tof', back_sep=BACKGROUND,
                                    slice_range=ion_tof_slices,
                                    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
fore_ion_tof_rawdata, back_ion_tof_rawdata = simplify_data(runset_ion_tof_data, single_rule=True)

# %%
overall_integral_eKE = []
# fel_energys = nm_to_ev(fel_wavelengths)

subt_ion_tof_rawdata = -(fore_ion_tof_rawdata - back_ion_tof_rawdata)
ion_tof_spec = rebinning(ion_tof, raw_ion_tof, subt_ion_tof_rawdata, axis=1)

fig, ax = plt.subplots(1,1,figsize=(12,4))
for (runnumber, ion_tof_spec_i) in zip( run_numbers, ion_tof_spec):
    ax.plot(ion_tof, ion_tof_spec_i, label=f"Run_{runnumber:03d}")
ax.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)
ax.set_xlabel('ion TOF')
ax.set_ylabel('ion TOF signal; rebinned (arb.u.)')
ax.set_title(f'{run_name}: run averages')
ax.set_ylim(-1,1)

if SAVE_FILES: fig.savefig(outdir+'/Average_of_complete_run.png')
plt.show()

# %%

ion_t0 = 6014.427540823292
ion_propconst = 7.343920984670405e-07 
ion_constants = ion_t0, ion_propconst

print(f"Using ion constants: (t0, C) = {ion_constants}")
tof_to_mq = lambda tof, spec, axis=None: tof_to_mq_conversion(tof, spec, *ion_constants, axis=axis)
mq_to_tof = lambda mq, spec, axis=None: mq_to_tof_conversion(mq, spec, *ion_constants, axis=axis)

# %%

fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,4))
for (runnumber, ion_tof_spec_i) in zip(run_numbers, ion_tof_spec):
    ax1.plot(ion_tof, ion_tof_spec_i, label=f"Run_{runnumber:03d}")

ax1.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)
ax1.set_xlabel('ion TOF')
ax1.set_ylabel('ion TOF signal; rebinned (arb.u.)')
ax1.set_title(f'{run_name}: run averages')
ax1.set_yscale('log')
ylim = ax1.set_ylim()
ax1.set_ylim(ylim[1]*1e-4, ylim[1])

mq_raw_coor, mq_raw_spectrum = tof_to_mq(ion_tof, ion_tof_spec, axis=1)
mq_coor = np.linspace(0.1, 70, num=1000)
mq_spectra = rebinning(mq_coor, mq_raw_coor, mq_raw_spectrum, axis=1)
for (runnumber, mq_spec_i) in zip(run_numbers, mq_spectra):
    ax2.plot(mq_coor, mq_spec_i, label=f"Run_{runnumber:03d}")

# for (runnumber, ion_tof_spec_i) in zip(run_numbers, ion_tof_spec):
#     mq_coor, mq_spectrum = tof_to_mq(rebin_ion_tof, ion_tof_spec_i)
#     rebin_mq = np.linspace(0.1, 70, num=1000)
#     rebin_mq_spectrum = rebinning(rebin_mq, mq_coor, mq_spectrum)
#     ax2.plot(rebin_mq, rebin_mq_spectrum, label=f"Run_{runnumber:03d}")

ax2.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)
ax2.set_xlabel('mq')
ax2.set_ylabel('ion TOF signal; rebinned (arb.u.)')
# ax2.set_yscale('log')
ylim = ax2.set_ylim()
# ax2.set_ylim(ylim[1]*1e-4, ylim[1])
ax2.set_title(f'{run_name}: run averages')

# %%
"""
# ------------------------------------------------------------------------------------------------
# I0M filtering -----------------------------------------------------------------------------------
"""

# %%
raw_i0m_rundata = BasicRunSet.give_rundata('i0m', make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
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
ax1.set_title(f'{run_name}: I0M over time')
#ax1.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)

ax2.set_ylabel('binned counts')
ax2.set_xlabel('I0M (uJ)')
ax2.set_title(f'{run_name}: Histogram of I0M')
#ax2.legend(bbox_to_anchor=(1.04, 1), borderaxespad=0, ncol = 2)
plt.tight_layout()

if SAVE_FILES:
    plt.savefig(outdir+'/I0M_time_and_bins.png')
plt.show()

# %%
# %%time # uncomment to show time
runset_vmi = BasicRunSet.average_run_data('vmi',back_sep=BACKGROUND,
                                    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
fore_vmi, back_vmi = simplify_data(runset_vmi, single_rule=True, single_run=False)

# %% Show VMI and resizing

from cpbasex import loadG, cpbasex as cpbasex_inversion
from cpbasex.image_mod import resizeFoldedHalf, foldHalf

sub_vmi = fore_vmi - back_vmi
sub_vmi = sub_vmi.transpose(1,2,0)
print(np.shape(sub_vmi))
plt.imshow(sub_vmi[:,:,0])
plt.show()

rebinned_vmi = rebinning(np.linspace(0, 900, 512), np.arange(900), sub_vmi, axis=1)
rebinned_vmi = rebinning(np.linspace(0, 900, 512), np.arange(900), rebinned_vmi, axis=0)

plt.imshow(rebinned_vmi[:,:,0])
plt.grid()
plt.show()

x0, y0 = 264, 260
half_filter = [1,1]
folded = foldHalf(rebinned_vmi, x0=x0, y0=y0, half_filter=half_filter)
resized = resizeFoldedHalf(folded, 256)

plt.imshow(resized[:,:,0])
plt.title('half-folded')
plt.grid()
plt.show()


# %%
# Perform Abel inversion


gData = loadG('G_r256_k64_l4_half.h5', make_images=True)

# Apply the pBASEX algorithm
out = cpbasex_inversion(resized, gData, make_images=True, alpha=4.1e-5, shape='half')

raw = rebinned_vmi

# Plot some results
plt.figure(figsize=(12,9))
for i, sample in enumerate(np.arange(np.shape(folded)[2])):
	plt.subplot(4,5,5*i+1)
	plt.imshow(raw[:,:,i])
	plt.xticks([])
	plt.yticks([])
	plt.ylabel(sample)
	clim = plt.gci().get_clim()
	plt.clim(0,clim[1])
	if i==0:
		plt.title('Raw Image')
	plt.subplot(4,5,5*i+2)
	plt.plot(out['E'], out['IE'][:,i], 'k')
	plt.gca().ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
	if i==3:
		plt.xlabel('Energy (eV)')
	plt.gca().twinx()
	plt.plot(out['E'], out['betas'][:,:,i], '.', markersize=5, alpha=0.6)
	if i==0:
		# plt.text(-3, 3.5, 'counts per eV', size='small')
		# plt.text(12, 3.5, 'beta', size='small')
		# plt.text(3.5, 3.25, 'I(E), ', color='black', size='large')
		# plt.text(6, 3.25, 'B2', color=u'#1f77b4', size='large')
		# plt.text(7.5, 3.25, ', ', color='black', size='large')
		# plt.text(8, 3.25, 'B4', color=u'#ff7f0e', size='large')
		pass
	plt.ylim(-1,3)
	plt.subplot(4,5,5*i+3)
	plt.imshow(out['fit'][:,:,i]/2)
	plt.xticks([])
	plt.yticks([])
	plt.clim(0,clim[1])
	if i==0:
		plt.title('Fitted Image')
	plt.subplot(4,5,5*i+4)
	plt.imshow(out['fit'][:,:,i]/2-raw[:,:,i])
	plt.xticks([])
	plt.yticks([])
	if i==0:
		plt.title('Fit Residual')
	plt.subplot(4,5,5*i+5)
	plt.imshow(out['inv'][:,:,i]/2)
	plt.xticks([])
	plt.yticks([])
	plt.clim(0,clim[1]/5)
	if i==0:
		plt.title('Inverted Image')
plt.tight_layout()
plt.show()

