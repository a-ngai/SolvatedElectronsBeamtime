# %%
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps
from fermi_libraries.run_module import Run, RunSets, MultithreadRun
from fermi_libraries.common_functions import simplify_data, set_recursion_limit, resolve_path
from fermi_libraries.dictionary_search import search_symbols
import pathlib


def main():

    try:
        CURRENT_SCRIPT_DIR = str(pathlib.Path(__file__).parent.resolve())
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

    DATA_DIR = '../examples/TestBeamtime/Beamtime'


    print('CURRENT_SCRIPT_DIR: ', CURRENT_SCRIPT_DIR)
    print('DATA_DIR: ', DATA_DIR)
    DATA_DIR = resolve_path(CURRENT_SCRIPT_DIR, DATA_DIR)
    print('NEW_DIR', DATA_DIR)
    print()

    run_numbers = [1,]
    CALIBRATION_RUN_NUMBER = 1

    ## %%
    # This block loads all the relevent HDF5 filepaths into their respective Run.
    RunCollection = {}  # We will put all the 'Runs' in thes dictionary
    for run_id in (list(run_numbers) + [CALIBRATION_RUN_NUMBER,]):
        folderpath = os.path.join(DATA_DIR, f'Run_{run_id:03d}/rawdata')
        filepaths = [folderpath+'/'+filename for filename in os.listdir(folderpath)[::]]
        # RunCollection[run_id] = Run(filepaths,
        RunCollection[run_id] = MultithreadRun(filepaths,
                                    alias_dict=alias_dict, search_symbols=search_symbols,
                                    keyword_functions=keyword_functions,
                                    )  # create a Run object with its respective filepaths

    # This creates a set out of the run_numbers selected above
    BasicRunSet = RunSets([])
    for run in run_numbers:
        BasicRunSet.add([RunCollection[run]])
    print(f'Data set contains {len(BasicRunSet.run_instances)} run(s).')

    CalibrationRun = RunCollection[CALIBRATION_RUN_NUMBER]

    runset_vmi = CalibrationRun.average_run_data('vmi',back_sep=True,
                                        make_cache=True, use_cache=False,
                                        num_files_per_cache=5)
    # fore_vmi, back_vmi, *_ = simplify_data(runset_vmi, single_rule=True, single_run=True)
    fore_vmi, back_vmi, *_ = runset_vmi
    fore_vmi = fore_vmi[0][np.newaxis,:,:]
    back_vmi = back_vmi[0][np.newaxis,:,:]

    """
    By convention, the data axes will be (x-axis, y-axis, images). This shape is
    necessary for cpbasex to work easily.

    Show the VMI images

    """

    from cpbasex.cpbasex import cpbasex as cpbasex_inversion, cpbasex_energy as cpbasex_energy_inversion
    from cpbasex.gData import loadG
    from cpbasex.image_mod import resize, resizeFoldedHalf, foldHalf

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

if __name__ == "__main__":    
    main()