# %%
"""
## Import statements

- numpy, matplotlib are the usual libraries.

- fermi_libraries.run_module contains the data structure scripts used for compiling the raw data into easy-to-handle data.

- fermi_libraries.common_functions has generally useful functions with no specific goal.

- fermi_libraries.dictionary_search allows the filter capability of the Run.give_average_data() functions.

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
    rebinning, simplify_data, weighted_linear_regression,
    avg_from_moments, stdev_from_moments,
    name_from_runs,
    set_default_labels,
    set_recursion_limit,
    closest,
    )
from fermi_libraries.dictionary_search import search_symbols
import pathlib

# %%
"""
There's a difference between looking for the current script location when running .py vs .ipynb files. This is the best way I could come up with to make things work for both.
"""

# %%
try:
    CURRENT_SCRIPT_DIR = str(pathlib.Path(__file__).parent.resolve())+'/'
except NameError:  # this will happen in .ipynb files
    CURRENT_SCRIPT_DIR = os.path.abspath('')

# %%
"""
### Function definitions (that you might change)

This extends our filtering capabilities from simple things (e.g. I0M>5) anything
you want. For example, if we want to filter by the averages of the TOF spectra,
we would define some other keyword function as "average_TOF", and write a rule
such as "average_TOF>4". Here is an extreme example below.
"""

# %%
@set_recursion_limit(1)
def keyword_functions(keyword, aliasFunc, DictionaryObject):
    return DictionaryObject[aliasFunc(keyword)]

# %%
"""
### Alias definitions

This lets us re-name the long HDF5 groupnames into more intuitive names e.g.
"digitizer/channel1" -> "ion_tof".
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

# **Data selection**

This is the "options" part of the scripts, which we expect to change depending
on what we want. e.g. To look at different "Runs", we would change the
run_numbers variable.

Cacheing is provided as an option, to avoid recompiling raw data.

Maybe the "CURRENT_SCRIPT_DIR" is wrong, so you will have to adjust this
yourself; this is only an issue when we're all testing the scripts on our own
computers. Once we're all at the endstation, this will be fixed without any more
ambiguity.
"""

# %%
# BEAMTIME_DIR =  '/net/online4ldm/store/20234049/results/Beamtime/'  # expected directory at FERMI
BEAMTIME_DIR =  f'{CURRENT_SCRIPT_DIR}/TestBeamtime/'
DATA_DIR = f'{BEAMTIME_DIR}/Beamtime/'  # change from fictitious to the real raw data directory!
SAVE_DIR = f'{BEAMTIME_DIR}/results/evaluation/'#'/net/online4ldm/store/20234049/results/results' # ditto

SAVE_FILES = False

BACKGROUND = True  # Only set to False if you want to sum up everything
NAMEADD = 'test' # your name here
run_numbers = [1, 2]

MAKE_CACHE = True
LOAD_FROM_CACHE = False

CALIBRATION_RUN_NUMBER = 1

print(f'Run numbers: {run_numbers}')

# %%
"""
Create RunCollection (main data structure), and print location of our save
directory. I don't expect this to ever change.
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

# This is a single Run object
CalibrationRun = RunCollection[CALIBRATION_RUN_NUMBER]

# This creates a RunSet object
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
Create directory if non-existent (and if we are actually saving files).
"""

# %%
if SAVE_FILES:
    if not os.path.exists(outdir):
        os.mkdir(outdir)

# %%
"""

---

# Data compilation

Finally load some data! This is our bread-and-butter function to
load/filter/separate raw data, and compile into a more useful form.

**Everything stems from this function**. Play around with it!

The output for Runset.averageRunData and Runset.average_run_data_weights has the
axes shape (rule, condition, run, data):

- "rule" are the filtering rules
- "condition" is in the order (FEL:ON SLU:ON, FEL:OFF SLU:ON, FEL:ON SLU:OFF, FEL:OFF SLU:OFF)
- "run" are the individual Runs
- "data" is the average rundata/weights

If you ever get confused on the output_data you're getting, you can deduce which
axis stands for what by looking at the shape of the output_data:

> print(np.shape(output_data))
"""

# %%
"""
This is an example of using a "Run" object. This represents a single measurement and its replicates.
"""

# %%
"""
Make cache with 5 files per cache
"""
# %%
no_cache_vmi = CalibrationRun.average_run_data('vmi',back_sep=BACKGROUND,
                                    make_cache=True, use_cache=False,
                                    num_files_per_cache=5,
                                    )
print(f'shape of output data is: {np.shape(no_cache_vmi)}')
print('data has axes (condition, rules, ...data...)')

# %%
"""
Load cache; check for cache with all files, then check for cache with 5 files per cache
"""

# %%
no_cache_vmi = CalibrationRun.average_run_data('vmi',back_sep=BACKGROUND,
                                    make_cache=True, use_cache=False,
                                    num_files_per_cache=5,
                                    )
print(f'shape of output data is: {np.shape(no_cache_vmi)}')
print('data has axes (condition, rules, ...data...)')

# %%
"""
Load cache; check for cache with all files,
"""

# %%
##%%time
cache_vmi = CalibrationRun.average_run_data('vmi',back_sep=BACKGROUND,
                                    make_cache=True, use_cache=True,
                                    num_files_per_cache=None)
print(f'shape of output data is: {np.shape(cache_vmi)}')
print('data has axes (condition, rules, ...data...)')

# %%
"""
Load cache; make cache with all files
"""

# %%
no_cache_vmi = CalibrationRun.average_run_data('vmi',back_sep=BACKGROUND,
                                    make_cache=True, use_cache=False,
                                    num_files_per_cache=None)
print(f'shape of output data is: {np.shape(no_cache_vmi)}')
print('data has axes (condition, rules, ...data...)')

# %%
"""
This is an example of using a "RunSet" object. This represents multiple measurements, and is what we will typically use all the time out of convenience.
"""

# %%
##%%time
runset_vmi = BasicRunSet.average_run_data('vmi',back_sep=BACKGROUND,
                                    make_cache=MAKE_CACHE, use_cache=LOAD_FROM_CACHE)
print(f'shape of output data is: {np.shape(runset_vmi)}')
print('data has axes (condition, run, rules, ...data...)')
