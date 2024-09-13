import unittest
import subprocess

class TestTemplates(unittest.TestCase):
    # def setUp(self) -> None:
        # print(self.__dict__.items())
    
    def test_gui_methods(self):
        from tests.test_gui_api import TestGUIMethods

    def test_tof_calibration_template(self):
        from tests.run_tof_calibration_template import test_tof_calibration_template
        self.assertIsNone(test_tof_calibration_template())

    def test_tutorial_template(self):
        from tests.run_tutorial_template import test_tutorial_template
        test_tutorial_template()

    def test_filtering_template(self):
        from tests.run_filtering_template import test_filtering_template
        self.assertIsNone(test_filtering_template())

    def test_abel_template(self):
        from tests.run_abel_template import test_abel_template
        self.assertIsNone(test_abel_template())

    def test_delay_template(self):
        from tests.run_delay_template import test_delay_template
        self.assertIsNone(test_delay_template())

    def test_save_gdata(self):
        from tests.run_save_gdata import test_save_gdata
        self.assertIsNone(test_save_gdata())

    def test_cache_function(self):
        from tests.run_cache_test import test_cache
        self.assertIsNone(test_cache())

    def test_multithread_tof_calibration_template(self):
        from tests.run_multithread_tof_calibration_template import test_multithread_tof_calibration_template
        self.assertIsNone(test_multithread_tof_calibration_template())

    def test_multithread_tutorial_template(self):
        from tests.run_multithread_tutorial_template import test_multithread_tutorial_template
        self.assertIsNone(test_multithread_tutorial_template())

    def test_multithread_filtering_template(self):
        from tests.run_multithread_filtering_template import test_multithread_filtering_template
        self.assertIsNone(test_multithread_filtering_template())

    def test_multithread_abel_template(self):
        from tests.run_multithread_abel_template import test_multithread_abel_template
        self.assertIsNone(test_multithread_abel_template())

    def test_multithread_delay_template(self):
        from tests.run_multithread_delay_template import test_multithread_delay_template
        self.assertIsNone(test_multithread_delay_template())
    
    def test_multithread_run(self):
        from tests.run_test_multithread_run import test_multithread_run
        self.assertIsNone(test_multithread_run())

if __name__ == '__main__':
    unittest.main()