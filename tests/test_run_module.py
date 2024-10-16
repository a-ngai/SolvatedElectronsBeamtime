import os
import time
import numpy as np
import warnings
from fermi_libraries.run_module import Run, RunSets
from fermi_libraries.common_functions import (
    name_from_runs,
    set_recursion_limit,
    resolve_path, find_subdir,
    simplify_data
    )
from fermi_libraries.dictionary_search import search_symbols
import pathlib

def setup():

    CURRENT_SCRIPT_DIR = str(pathlib.Path(__file__).parent.resolve())+'/'
    BEAMTIME_DIR = find_subdir('TinyTestData', resolve_path(CURRENT_SCRIPT_DIR, ''), give_single=True)
    # BEAMTIME_DIR = resolve_path(CURRENT_SCRIPT_DIR, 'TinyTestData')
    DATA_DIR = f'{BEAMTIME_DIR}/Beamtime'

    @set_recursion_limit(1)
    def keyword_functions(keyword, aliasFunc, DictionaryObject):
        return DictionaryObject[aliasFunc(keyword)]

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

    run_numbers = [1, 2]

    print(CURRENT_SCRIPT_DIR)
    print(resolve_path(CURRENT_SCRIPT_DIR))
    print(BEAMTIME_DIR)
    print(DATA_DIR)
    RunCollection = {}
    for run_id in run_numbers:
        folderpath = resolve_path(f'{DATA_DIR}/Run_{run_id:03d}/rawdata')
        print(folderpath)
        filenames = os.listdir(folderpath)
        RunCollection[run_id] = Run(filenames,
                                    filedir=folderpath,
                                    alias_dict=alias_dict, search_symbols=search_symbols,
                                    keyword_functions=keyword_functions,
                                    )  # create a Run object with its respective filepaths

    BasicRunSet = RunSets([])
    for run in run_numbers:
        BasicRunSet.add([RunCollection[run]])
    print(f'Data set contains {len(BasicRunSet.run_instances)} run(s).')
    
    return RunCollection, BasicRunSet, DATA_DIR, run_numbers

def test_caching():
    RunCollection, BasicRunSet, DATA_DIR, run_numbers = setup()

    # no caching
    time_start = time.time()
    no_cache_vmi, cache_info = RunCollection[1].average_run_data_cache_info('vmi',back_sep=True,
                                        make_cache=False, use_cache=False,
                                        )
    assert len(cache_info['saved']) == 0
    assert len(cache_info['loaded']) == 0

    cache_folder = resolve_path(f'{DATA_DIR}/Run_001/work/average_run_data_weights_cache')
    mod_times = np.array([os.path.getmtime(f'{cache_folder}/{filename}') for filename in os.listdir(cache_folder)])
    assert np.sum(mod_times>=time_start) == len(cache_info['saved'])

    # make cache with 5 files per cache
    time_start = time.time()
    no_cache_vmi, cache_info = RunCollection[1].average_run_data_cache_info('vmi',back_sep=True,
                                        make_cache=True, use_cache=False,
                                        num_files_per_cache=2,
                                        )
    saved, loaded = cache_info['saved'], cache_info['loaded']
    assert len(cache_info['saved']) == 3
    assert len(cache_info['loaded']) == 0

    cache_folder = resolve_path(f'{DATA_DIR}/Run_001/work/average_run_data_weights_cache')
    mod_times = np.array([os.path.getmtime(f'{cache_folder}/{filename}') for filename in os.listdir(cache_folder)])
    assert np.sum(mod_times>=time_start) == len(cache_info['saved'])

    # Load cache; check for cache, where only 5-file caches exist
    time_start = time.time()
    full_run_cache = cache_info['saved'][-1][0]
    os.remove(full_run_cache)
    cache_vmi, cache_info = RunCollection[1].average_run_data_cache_info('vmi',back_sep=True,
                                        make_cache=True, use_cache=True,
                                        num_files_per_cache=2)
    assert len(cache_info['saved']) == 1
    assert len(cache_info['loaded']) == 2

    cache_folder = resolve_path(f'{DATA_DIR}/Run_001/work/average_run_data_weights_cache')
    mod_times = np.array([os.path.getmtime(f'{cache_folder}/{filename}') for filename in os.listdir(cache_folder)])
    assert np.sum(mod_times>=time_start) == len(cache_info['saved'])

    # Load cache; make cache with all files
    time_start = time.time()
    no_cache_vmi, cache_info = RunCollection[1].average_run_data_cache_info('vmi',back_sep=True,
                                        make_cache=True, use_cache=False,
                                        num_files_per_cache=None)
    saved = cache_info['saved']
    loaded = cache_info['loaded']
    assert len(cache_info['saved']) == 1
    assert len(cache_info['loaded']) == 0

    cache_folders = [resolve_path(f'{DATA_DIR}/Run_{run_number:03d}/work/average_run_data_weights_cache')
                     for run_number in [1,]]
    all_cache_files = np.concatenate([
        np.array([f'{cache_folder}/{filename}' for filename in os.listdir(cache_folder)]) for cache_folder in cache_folders])
    mod_times = np.array([os.path.getmtime(path) for path in all_cache_files])
    assert np.sum(mod_times>=time_start) == len(cache_info['saved'])


    # Make cache for RunSet
    time_start = time.time()
    runset_vmi, cache_info = BasicRunSet.average_run_data_cache_info('vmi',back_sep=True,
                                        make_cache=True, use_cache=False)
    print(cache_info['saved'])
    assert len(cache_info['saved']) == 2
    assert len(cache_info['loaded']) == 2
    assert len(cache_info['saved'][0]) == 1
    assert len(cache_info['loaded'][0]) == 0
    assert len(cache_info['saved'][0][0]) == 2
    assert len(cache_info['saved'][0][0][1]) == 4
    # assert np.shape(cache_info['saved']) == (2, 1, 2)
    # assert np.shape(cache_info['loaded']) == (2, 0, 2)

    cache_folders = [resolve_path(f'{DATA_DIR}/Run_{run_number:03d}/work/average_run_data_weights_cache')
                     for run_number in run_numbers]
    all_cache_files = np.concatenate([
        np.array([f'{cache_folder}/{filename}' for filename in os.listdir(cache_folder)]) for cache_folder in cache_folders])
    mod_times = np.array([os.path.getmtime(path) for path in all_cache_files])
    assert np.sum(mod_times>=time_start) == len(run_numbers)

    # Load cache for RunSet
    time_start = time.time()
    runset_vmi, cache_info = BasicRunSet.average_run_data_cache_info('vmi',back_sep=True,
                                        make_cache=True, use_cache=True)
    assert len(cache_info['saved']) == 2
    assert len(cache_info['loaded']) == 2
    assert len(cache_info['saved'][0]) == 0
    assert len(cache_info['loaded'][0]) == 1
    assert len(cache_info['loaded'][0][0]) == 2
    assert len(cache_info['loaded'][0][0][1]) == 4
    # assert np.shape(cache_info['saved']) == (2, 0, 2)
    # assert np.shape(cache_info['loaded']) == (2, 1, 2)

    cache_folders = [resolve_path(f'{DATA_DIR}/Run_{run_number:03d}/work/average_run_data_weights_cache')
                     for run_number in run_numbers]
    mod_times = np.concatenate([
        np.array([os.path.getmtime(f'{cache_folder}/{filename}') for filename in os.listdir(cache_folder)]) for cache_folder in cache_folders])
    assert np.sum(mod_times>=time_start) == 0

def test_run_class():
    RunCollection, BasicRunSet, DATA_DIR, run_numbers = setup()
    run_vmi = RunCollection[1].average_run_data('vmi',back_sep=True,
                                        make_cache=False, use_cache=False)
    print(f'shape of output data is: {np.shape(run_vmi)}')
    print('data has axes (condition, rules, ...data...)')
    assert np.shape(run_vmi)[:2] == (4, 1)

    warnings.warn("fermi_libraries.run_module run_class tests not complete!")

def test_runset_class():
    RunCollection, BasicRunSet, DATA_DIR, run_numbers = setup()
    runset_vmi = BasicRunSet.average_run_data('vmi',back_sep=True,
                                        make_cache=False, use_cache=False)
    print(f'shape of output data is: {np.shape(runset_vmi)}')
    print('data has axes (condition, run, rules, ...data...)')
    assert np.shape(runset_vmi)[:3] == (4, 2, 1)
    vmi_shape = np.shape(runset_vmi)[3:]

    fore_vmi, back_vmi, *_ = simplify_data(runset_vmi, 
                                           single_rule=True, single_run=False)
    assert np.shape(fore_vmi) == np.shape(back_vmi)
    assert np.shape(fore_vmi) == (2, *vmi_shape)

    fore_vmi, back_vmi, *_ = simplify_data(runset_vmi, 
                                           single_rule=True, single_run=True)
    print(f'shape of fore data is: {np.shape(fore_vmi)}')
    print(f'shape of back data is: {np.shape(back_vmi)}')
    print('data has axes (...data...)')
    assert np.shape(fore_vmi) == np.shape(back_vmi)
    assert np.shape(fore_vmi) == vmi_shape

    separated_runset_iontof = BasicRunSet.average_run_data('ion_tof', back_sep=True,
                                        make_cache=False, use_cache=False)
    assert np.shape(separated_runset_iontof)[:3] == (4, 2, 1)
    iontof_shape = np.shape(separated_runset_iontof)[3:]

    fore_iontof, back_iontof, *_ = simplify_data(separated_runset_iontof,
                                                 single_run=False, single_rule=True)
    assert np.shape(fore_iontof) == np.shape(back_iontof)
    assert np.shape(fore_iontof) == (2, *iontof_shape)

    separated_runsetdata_i0m = BasicRunSet.give_rundata('i0m', back_sep=False, make_cache=False, use_cache=False)
    assert len(separated_runsetdata_i0m) == 4  # irregular axes: (conditions, runs, rules, data)
    assert np.shape(separated_runsetdata_i0m[0])[:2] == (2, 1)
    i0m_shape = np.shape(separated_runsetdata_i0m[0][0][0])
    runsetdata_i0m, *_ = simplify_data(separated_runsetdata_i0m, 
                                       single_run=False, single_rule=True)  # can use simplify_data, because no rules
    assert np.shape(runsetdata_i0m) == (2, *i0m_shape)

    delays = BasicRunSet.average_run_data('delay',back_sep=False,
                                        make_cache=False, use_cache=False)
    assert np.shape(delays[0]) == (2, 1, 1)

    delays, *_ = simplify_data(delays, single_rule=True, single_run=False)
    assert np.shape(delays) == (2, 1)

    i0m_edges = np.linspace(-4.5, -3.0, num=4)
    i0m_filter_rules = [f'(i0m>{lo} & i0m<{hi})' for lo, hi in zip(i0m_edges[:-1], i0m_edges[1:])]
    print(f'i0m filter rules: {i0m_filter_rules}')

    separated_runset_iontof = BasicRunSet.average_run_data('ion_tof', back_sep=True,
                                        rules=i0m_filter_rules,
                                        make_cache=False, use_cache=False)
    print(f'shape is (rules, runs, data): {np.shape(separated_runset_iontof)}')
    assert np.shape(separated_runset_iontof)[:3] == (4, 2, len(i0m_filter_rules))
    iontof_shape = np.shape(separated_runset_iontof)[3:]

    fore_iontof, back_iontof, *_ = simplify_data(separated_runset_iontof, 
                                                 single_run=False, single_rule=False)
    assert np.shape(fore_iontof) == np.shape(back_iontof)
    assert np.shape(fore_iontof) == (len(i0m_filter_rules), 2, *iontof_shape)

    separated_runset_vmi = BasicRunSet.average_run_data('vmi', back_sep=True,
                                        rules=i0m_filter_rules,
                                        make_cache=False, use_cache=False)
    assert np.shape(separated_runset_vmi)[:3] == (4, 2, len(i0m_filter_rules))
    vmi_shape = np.shape(separated_runset_vmi)[3:]
    fore_vmi, back_vmi, *_ = simplify_data(separated_runset_vmi, single_rule=False)
    assert np.shape(fore_vmi) == np.shape(back_vmi)
    assert np.shape(fore_vmi) == (len(i0m_filter_rules), 2, *vmi_shape)