import pytest

class TestModules():
    def test_common_functions(self):
        from tests.run_common_functions_test import test_common_functions
        assert test_common_functions() is None
    
    def test_run_module_caching(self):
        from tests.run_run_module_test import test_caching
        assert test_caching() is None

    def test_run_module_run_class(self):
        from tests.run_run_module_test import test_run_class
        assert test_run_class() is None

    def test_run_module_runset_class(self):
        from tests.run_run_module_test import test_runset_class
        assert test_runset_class() is None

    def test_run_module_multithread_caching(self):
        from tests.run_run_module_multithread_test import test_caching
        assert test_caching() is None

    def test_run_module_multithread_run_class(self):
        from tests.run_run_module_multithread_test import test_run_class
        assert test_run_class() is None

    def test_run_module_multithread_runset_class(self):
        from tests.run_run_module_multithread_test import test_runset_class
        assert test_runset_class() is None

class TestTemplates():
    def setUp(self) -> None:
        print(self.__dict__.items())
    
    def test_tutorial_template(self):
        from tests.run_tutorial_template import test_tutorial_template
        assert test_tutorial_template() is None

    def test_tof_calibration_template(self):
        from tests.run_tof_calibration_template import test_tof_calibration_template
        assert test_tof_calibration_template() is None

    def test_filtering_template(self):
        from tests.run_filtering_template import test_filtering_template
        assert test_filtering_template() is None

    def test_abel_template(self):
        from tests.run_abel_template import test_abel_template
        assert test_abel_template() is None

    def test_delay_template(self):
        from tests.run_delay_template import test_delay_template
        assert test_delay_template() is None

    def test_save_gdata(self):
        from tests.run_save_gdata import test_save_gdata
        assert test_save_gdata() is None

    def test_cache_template(self):
        from tests.run_cache_test import test_cache
        assert test_cache() is None

class TestMultithreadTemplates():
    
    def test_multithread_tof_calibration_template(self):
        from tests.run_multithread_tof_calibration_template import test_multithread_tof_calibration_template
        test_multithread_tof_calibration_template()

    def test_multithread_tutorial_template(self):
        from tests.run_multithread_tutorial_template import test_multithread_tutorial_template
        assert test_multithread_tutorial_template() is None

    def test_multithread_filtering_template(self):
        from tests.run_multithread_filtering_template import test_multithread_filtering_template
        assert test_multithread_filtering_template() is None

    def test_multithread_abel_template(self):
        from tests.run_multithread_abel_template import test_multithread_abel_template
        assert test_multithread_abel_template() is None

    def test_multithread_delay_template(self):
        from tests.run_multithread_delay_template import test_multithread_delay_template
        assert test_multithread_delay_template() is None
    
    def test_multithread_run(self):
        from tests.run_test_multithread_run import test_multithread_run
        assert test_multithread_run() is None

class TestNotebooks():
    
    def test_notebook_processing_preprocess_html(self):
        from tests.run_convert_to_ipynb_basic_tutorial import main
        assert main() is None

    def test_notebook_processing_negative_control(self):
        from tests.run_error_convert_to_ipynb import main
        with pytest.raises(RuntimeError) as e_info: main()

    def test_notebook_processing(self):
        from convert_to_ipynb import main
        assert main() is None

# from tests.test_gui_api import TestGUIMethods
from tests.test_gui_api import TestGUIMethodsRough