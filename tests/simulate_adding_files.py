import os
import pathlib
from shutil import copyfile
from time import sleep
from fermi_libraries.common_functions import resolve_path

try:
    CURRENT_SCRIPT_DIR = str(pathlib.Path(__file__).parent.resolve())
except NameError:  # this will happen in .ipynb files
    CURRENT_SCRIPT_DIR = os.path.abspath('')

src_path = resolve_path(CURRENT_SCRIPT_DIR, '../examples/TestBeamtime/Beamtime/Run_001/rawdata')
tar_path = resolve_path(CURRENT_SCRIPT_DIR, '_temp/TestBeamtime/Beamtime/Run_001/rawdata')

counter = 0
while True:
    print(f'loop {counter}')
    while len(os.listdir(tar_path)) > 0:
        for filename in os.listdir(tar_path):
            filepath = f'{tar_path}/{filename}'
            try:
                os.remove(filepath)
            except PermissionError:
                continue
    for filename in os.listdir(src_path)[:20]:
        src_filepath = f'{src_path}/{filename}'
        tar_filepath = f'{tar_path}/{filename}'
        print(f'    copying file {src_filepath} to {tar_filepath}')
        try:
            copyfile(src_filepath, tar_filepath)
        except PermissionError:
            print('    ! race condition!')
        sleep(5)

    counter += 1