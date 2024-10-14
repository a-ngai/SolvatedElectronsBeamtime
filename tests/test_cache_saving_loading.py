# %%
import os
import numpy as np
from fermi_libraries.run_module import Run, RunSets
from fermi_libraries.common_functions import (
    name_from_runs,
    set_recursion_limit,
    resolve_path, find_subdir
    )
from fermi_libraries.dictionary_search import search_symbols
import pathlib

try:
    CURRENT_SCRIPT_DIR = str(pathlib.Path(__file__).parent.resolve())+'/'
except NameError:  # this will happen in .ipynb files
    CURRENT_SCRIPT_DIR = os.path.abspath('')

@set_recursion_limit(1)
def keyword_functions(keyword, aliasFunc, DictionaryObject):
    return DictionaryObject[aliasFunc(keyword)]

alias_dict = {
    'vmi' : 'vmi/andor',
    'ion_tof' : 'digitizer/channel1',
    'delay' : 'user_laser/delay_line/position',
    'slu' : 'user_laser/energy_meter/Energy2',
    }

# %%
BEAMTIME_DIR = find_subdir('TestBeamtime', resolve_path(CURRENT_SCRIPT_DIR, '../examples'), give_single=True)
DATA_DIR = f'{BEAMTIME_DIR}/Beamtime'
SAVE_DIR = f'{BEAMTIME_DIR}/results/evaluation'

SAVE_FILES = True

BACKGROUND = True  # Only set to False if you want to sum up everything
NAMEADD = 'test' # your name here
NAMEADD = 'cachingtest_XX' # your name here
run_numbers = [1, 2]

CALIBRATION_RUN_NUMBER = 1

print(f'Run numbers: {run_numbers}')
print(f'CURRENT_SCRIPT_DIR: {CURRENT_SCRIPT_DIR}')
print(f'BEAMTIME_DIR: {BEAMTIME_DIR}')
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
    filepaths = os.listdir(folderpath)
    RunCollection[run_id] = Run(filepaths,
                                filedir=folderpath,
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
# no caching
no_cache_vmi, cache_info = CalibrationRun.average_run_data_cache_info('vmi',back_sep=BACKGROUND,
                                    make_cache=False, use_cache=False,
                                    )
assert len(cache_info['saved']) == 0
assert len(cache_info['loaded']) == 0

# make cache with 5 files per cache
no_cache_vmi, cache_info = CalibrationRun.average_run_data_cache_info('vmi',back_sep=BACKGROUND,
                                    make_cache=True, use_cache=False,
                                    num_files_per_cache=1,
                                    )
saved, loaded = cache_info['saved'], cache_info['loaded']
assert len(cache_info['saved']) == 3
assert len(cache_info['loaded']) == 0

# Load cache; check for cache, where only 5-file caches exist
full_run_cache = cache_info['saved'][-1][0]
os.remove(full_run_cache)
cache_vmi, cache_info = CalibrationRun.average_run_data_cache_info('vmi',back_sep=BACKGROUND,
                                    make_cache=True, use_cache=True,
                                    num_files_per_cache=1)
assert len(cache_info['saved']) == 1
assert len(cache_info['loaded']) == 2

# Load cache; make cache with all files
no_cache_vmi, cache_info = CalibrationRun.average_run_data_cache_info('vmi',back_sep=BACKGROUND,
                                    make_cache=True, use_cache=False,
                                    num_files_per_cache=None)
assert len(cache_info['saved']) == 1
assert len(cache_info['loaded']) == 0

# Make cache for RunSet
runset_vmi, cache_info = BasicRunSet.average_run_data_cache_info('vmi',back_sep=BACKGROUND,
                                    make_cache=True, use_cache=False)
print(cache_info['saved'])
assert len(cache_info['saved']) == 2
assert len(cache_info['loaded']) == 2
assert len(cache_info['saved'][0]) == 1
assert len(cache_info['loaded'][0]) == 0
assert len(cache_info['saved'][0][0]) == 2
# assert np.shape(cache_info['saved']) == (2, 1, 2)
# assert np.shape(cache_info['loaded']) == (2, 0, 2)

# Load cache for RunSet
runset_vmi, cache_info = BasicRunSet.average_run_data_cache_info('vmi',back_sep=BACKGROUND,
                                    make_cache=True, use_cache=True)
assert len(cache_info['saved']) == 2
assert len(cache_info['loaded']) == 2
assert len(cache_info['saved'][0]) == 0
assert len(cache_info['loaded'][0]) == 1
assert len(cache_info['loaded'][0][0]) == 2
# assert np.shape(cache_info['saved']) == (2, 0, 2)
# assert np.shape(cache_info['loaded']) == (2, 1, 2)