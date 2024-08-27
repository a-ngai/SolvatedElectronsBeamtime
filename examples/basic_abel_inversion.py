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
from fermi_libraries.run_module import Run, RunSets
from fermi_libraries.common_functions import (
    rebinning, simplify_data, 
    name_from_runs,
    set_default_labels,
    set_recursion_limit,
    )
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

# Alternative names for the HDF5 groupnames
alias_dict = {
    'vmi' : 'vmi/andor',
    'ion_tof' : 'digitizer/channel1',
    'delay' : 'user_laser/delay_line/position',
    'slu' : 'user_laser/energy_meter/Energy2',
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

# VMI images section

"""

# %%

##%%time
runset_vmi = BasicRunSet.average_run_data('vmi',back_sep=BACKGROUND,
                                    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
fore_vmi, back_vmi = simplify_data(runset_vmi, single_rule=True, single_run=False)

# %%
"""
By convention, the data axes will be (x-axis, y-axis, images). This shape is
necessary for cpbasex to work easily.

Show the VMI images

"""

# %%

from cpbasex import resizeFoldedHalf, foldHalf, loadG, cpbasex as cpbasex_inversion
from cpbasex.image_mod import resize

sub_vmi = fore_vmi - back_vmi
sub_vmi = sub_vmi.transpose(1,2,0)

vmi = resize(sub_vmi, (512, 512), axis=(0,1))

show_raw_vmi = sub_vmi[:,:,0]
show_bin_vmi = vmi[:,:,0]
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(9,4))
cax1 = ax1.imshow(show_raw_vmi)
ax1.set_title(f'first raw VMI image\nshape={show_raw_vmi.shape}')
fig.colorbar(cax1, ax=ax1)
ax1.grid()
cax2 = ax2.imshow(show_bin_vmi)
ax2.set_title(f'binned VMI image\nshape={show_bin_vmi.shape}')
fig.colorbar(cax2, ax=ax2)
ax2.grid()
plt.show()

# %%
"""
Correcting the VMI images
"""

# %%

test_image = vmi[:,:,0]

from cpbasex.image_mod import find_center, find_rotation, find_ellipticity
from cpbasex.image_mod import center_image, rotate, stretch


if True: # straightforward way; rotation -> ellipticity -> center
    guess_rot = find_rotation(test_image)
    guess_ell = find_ellipticity(test_image)
    guess_cen = find_center(test_image, center_guess=(250,250), r_max=30)

# guess_corrrection = zoom(rotate(center_image(test_image, guess_cen), guess_rot), guess_ell)
test_correction = stretch(rotate(center_image(test_image, guess_cen), guess_rot), [1,1.1])

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(9,4))
cax1 = ax1.imshow(test_image)
ax1.set_title('before image')
ax1.grid()
fig.colorbar(cax1, ax=ax1)
cax2 = ax2.imshow(test_correction)
ax2.set_title('corrected image')
ax2.grid()
fig.colorbar(cax2, ax=ax2)
plt.show()

corrected = [stretch(rotate(center_image(image, guess_cen), guess_rot), [1,1.1]) for image in vmi]

if False: # to make image correction easier, these should "commute"
    find_rotation()
    find_ellipticity()
    find_center()

# %%
"""
Fold the VMI images in preparation for the Abel inversion
"""

# %%

x0, y0 = 264, 260
half_filter = [True, True]
folded = foldHalf(vmi, x0=x0, y0=y0, half_filter=half_filter)
resized = resizeFoldedHalf(folded, 256)

plt.imshow(resized[:,:,0])
plt.title(f'Half-folded. [left, right]={half_filter}')
plt.grid()
plt.show()

# %%
"""
Perform the Abel inversion
"""

# %%

# load inversion object
MAKE_IMAGES = True
gData = loadG('G_r256_k64_l4_half.h5', make_images=MAKE_IMAGES)

# Apply the pBASEX algorithm
out = cpbasex_inversion(resized, gData, make_images=MAKE_IMAGES, alpha=4.1e-5, shape='half')
energy, pes, betas, c = out['E'], out['IE'], out['betas'], out['c']
if MAKE_IMAGES: fit, inv = out['fit'], out['inv']

raw = vmi

Nimages = np.shape(vmi)[2]
fig, axes = plt.subplots(Nimages, 5, figsize=(14,5))
axes[0][0].set_title('Raw Image')
axes[-1][1].set_xlabel('Energy (eV)')
axes[0][2].set_title('Fitted Image')
axes[0][3].set_title('Fit Residual')
axes[0][4].set_title('Inverted Image')
for i in range(Nimages):
    ax = axes[i]
    cax0 = ax[0].imshow(raw[:,:,i])
    clim = cax0.get_clim()
    fig.colorbar(cax0, ax=ax[0])
    ax[0].set_ylabel(i)
    ax[1].plot(out['E'], out['IE'][:,i], 'k')
    axbetas = ax[1].twinx()
    axbetas.set_ylim(-2,2)
    axbetas.plot(out['E'], out['betas'][:,:,i], '.', markersize=5, alpha=0.6)
	# plt.gca().ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    if i==0:
		# plt.text(-3, 3.5, 'counts per eV', size='small')
		# plt.text(12, 3.5, 'beta', size='small')
		# plt.text(3.5, 3.25, 'I(E), ', color='black', size='large')
		# plt.text(6, 3.25, 'B2', color=u'#1f77b4', size='large')
		# plt.text(7.5, 3.25, ', ', color='black', size='large')
		# plt.text(8, 3.25, 'B4', color=u'#ff7f0e', size='large')
        pass
    cax2 = ax[2].imshow(out['fit'][:,:,i]/2)
    cax2.set_clim(0,clim[1])
    fig.colorbar(cax2, ax=ax[2])
    cax3 = ax[3].imshow(out['fit'][:,:,i]/2-raw[:,:,i])
    # cax4.set_clim(0,clim[1]/5)
    fig.colorbar(cax3, ax=ax[3])
    cax4 = ax[4].imshow(out['inv'][:,:,i]/2)
    fig.colorbar(cax4, ax=ax[4])
plt.tight_layout()
plt.show()
