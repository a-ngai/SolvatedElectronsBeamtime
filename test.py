import unittest
import subprocess

class TestTemplates(unittest.TestCase):

    def test_calibration_template(self):
        from tests.run_calibration_template import test_calibration_template
        self.assertIsNone(test_calibration_template())

    def test_tutorial_template(self):
        from tests.run_tutorial_template import test_tutorial_template
        self.assertIsNone(test_tutorial_template())

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

if __name__ == '__main__':
    unittest.main()