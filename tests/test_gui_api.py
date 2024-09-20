import sys
import pathlib
import os
import time
from shutil import copyfile
from fermi_libraries.common_functions import resolve_path
import unittest

try:
    CURRENT_SCRIPT_DIR = str(pathlib.Path(__file__).parent.resolve())
except NameError:  # this will happen in .ipynb files
    CURRENT_SCRIPT_DIR = os.path.abspath('')

tar_path = resolve_path(CURRENT_SCRIPT_DIR, '..')
if __name__ == "__main__": print(f'adding ({tar_path}) to path')
sys.path.insert(1, tar_path)
from gui_scripts.fermi_gui import QApplication, Ui_MainWindow, MainWindow

def clear_test_data_folder(dir):
    if '_temp' not in dir:
        print(f"substring '_temp' not in dir ({dir}), aborting")
        raise Exception
    while len(os.listdir(dir)) > 0:
        for filename in os.listdir(dir):
            filepath = f'{dir}/{filename}'
            try:
                os.remove(filepath)
            except PermissionError:
                continue

def add_file_to_test_data(src_dir, tar_dir):
    file_found = False
    for filename in os.listdir(src_dir):
        src_filepath = f'{src_dir}/{filename}'
        tar_filepath = f'{tar_dir}/{filename}'
        if os.path.exists(tar_filepath):
            continue
        file_found = True
        break
    if not file_found:
        raise OSError('no suitable file found; all other files already exist in target dir')
    print(f'    copying file {src_filepath} to {tar_filepath}')
    copyfile(src_filepath, tar_filepath)


search_dir = resolve_path(CURRENT_SCRIPT_DIR, '_temp/TestBeamtime/Beamtime')
data_dir = resolve_path(CURRENT_SCRIPT_DIR, '../examples/TestBeamtime/Beamtime/Run_001/rawdata')
test_dir = f'{CURRENT_SCRIPT_DIR}/_temp/TestBeamtime/Beamtime/Run_001/rawdata'

if __name__ == "__main__":
    print()
    print(f'taking data from {data_dir}')
    print(os.path.exists(data_dir))
    print(f'saving data into {test_dir}')
    print(os.path.exists(test_dir))
    print()

class TestGUIMethods(unittest.TestCase):
    
    @staticmethod
    def setup_qapplication():
        if not (app := QApplication.instance()):
            app = QApplication(sys.argv)
        return app

    # # @staticmethod
    # def remove_qapplication_singleton(self):
    #     print('here!')
    #     if app := QApplication.instance():
    #         app.exit()  # doesn't seem to work!
    #         del app  

    def setup(self):

        app = self.setup_qapplication()
        tabWidgetApp = Ui_MainWindow()
        w = MainWindow()

        tabWidgetApp.setupUi(w)
        tabWidgetApp.setup_signals()
        w.add_canvas(tabWidgetApp)

        tabWidgetApp.text_edit_search_dir_for_newest_folder.setText(search_dir)

        tabWidgetApp.apply_settings()

        return app, tabWidgetApp, w
    
    def tear_down(self):
        self.app.exit()
        self.app.shutdown()


    def test_new_file_detection(self):
        from gui_scripts.fermi_gui import setup_window_app_tabwidget
        
        try:
            w, app, tabWidgetApp = setup_window_app_tabwidget()
            # app, tabWidgetApp, w = self.setup()
            self.app = app
            tabWidgetApp.terminal_print = False

            clear_test_data_folder(test_dir)
            time.sleep(0.5)
            tabWidgetApp.click_auto_newest_folder()
            self.assertEqual(tabWidgetApp.status['current_files'], [])
            tabWidgetApp.update_data_if_change()
            self.assertEqual(tabWidgetApp.status['current_folder'], f'{search_dir}/Run_001')

            add_file_to_test_data(data_dir, test_dir)
            self.assertTrue(tabWidgetApp.check_filechange())
            self.assertTrue(tabWidgetApp.background_key)
            tabWidgetApp.update_data_if_change()
            self.assertEqual(len(tabWidgetApp.status['current_files']), 1)
            
            time_start = time.time()
            time_current = time.time()
            max_time_allowed = 20  # max one second for process to end
            while (time_current - time_start < max_time_allowed) and not tabWidgetApp.background_key:
                time.sleep(0.7)
                app.processEvents()
                time_current = time.time()
            self.assertTrue(tabWidgetApp.background_key)

            tabWidgetApp.get_newest_folder()
            tabWidgetApp.check_filechange()
            tabWidgetApp.get_filechange()
            self.assertFalse(tabWidgetApp.check_filechange())
            self.assertTrue(tabWidgetApp.background_key)

        except Exception as e:
            raise e
        
        finally:
            self.tear_down()

# if __name__ == '__main__':
#     unittest.main()



class TestGUIMethodsRough(unittest.TestCase):
    
    @staticmethod
    def setup_qapplication():
        if not (app := QApplication.instance()):
            app = QApplication(sys.argv)
        return app

    def setup(self):

        app = self.setup_qapplication()
        tabWidgetApp = Ui_MainWindow()
        w = MainWindow()

        tabWidgetApp.setupUi(w)
        tabWidgetApp.setup_signals()
        w.add_canvas(tabWidgetApp)

        tabWidgetApp.text_edit_search_dir_for_newest_folder.setText(search_dir)

        tabWidgetApp.apply_settings()

        return app, tabWidgetApp, w
    
    def tear_down(self):
        self.app.exit()
        self.app.shutdown()


    def test_new_file_detection(self):
        from gui_scripts.fermi_gui_rough import setup_window_app_tabwidget
        

        try:
        
            w, app, tabWidgetApp = setup_window_app_tabwidget()
            # app, tabWidgetApp, w = self.setup()
            self.app = app
            tabWidgetApp.terminal_print = False

            clear_test_data_folder(test_dir)
            time.sleep(0.5)
            tabWidgetApp.click_auto_newest_folder()
            self.assertEqual(tabWidgetApp.status['current_files'], [])
            tabWidgetApp.update_data_if_change()
            self.assertEqual(tabWidgetApp.status['current_folder'], f'{search_dir}/Run_001')

            add_file_to_test_data(data_dir, test_dir)
            self.assertTrue(tabWidgetApp.check_filechange())
            self.assertTrue(tabWidgetApp.background_key)
            tabWidgetApp.update_data_if_change()
            self.assertEqual(len(tabWidgetApp.status['current_files']), 1)
            
            time_start = time.time()
            time_current = time.time()
            max_time_allowed = 15  # max one second for process to end
            while (time_current - time_start < max_time_allowed) and not tabWidgetApp.background_key:
                time.sleep(0.7)
                app.processEvents()
                time_current = time.time()
            self.assertTrue(tabWidgetApp.background_key)

            tabWidgetApp.get_newest_folder()
            tabWidgetApp.check_filechange()
            tabWidgetApp.get_filechange()
            self.assertFalse(tabWidgetApp.check_filechange())
            self.assertTrue(tabWidgetApp.background_key)

        except Exception as e:
            raise e
        
        finally:
            self.tear_down()