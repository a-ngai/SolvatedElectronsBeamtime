import re
import os
import importlib

test_file_template =  "tests/test_run_module.py"
temp_test_file = "tests/_test_run_module_multithread.py"

def setup():
    found_multithread_import = False
    before_multithread_import_string = r"from fermi_libraries.run_module import Run, RunSets"
    after_multithread_import_string = r"from fermi_libraries.run_module import MultithreadRun as Run, RunSets"
    with (open(test_file_template, 'r') as f, open(temp_test_file, 'w') as g):
        new_lines = []
        for line in f.readlines():
            mod_line = line
            if before_multithread_import_string in line:
                found_multithread_import = True
                re_string = re.sub(r'\.', r'\.', before_multithread_import_string)

                mod_line = re.sub(
                    re_string,
                    after_multithread_import_string,
                    mod_line)

            new_lines.append(mod_line)
        g.writelines(new_lines)
    try:
        if not found_multithread_import:
            raise ValueError("Cannot change to multithread import!")
        module_name = re.sub(r'/',r'.',temp_test_file)
        module_name = re.sub(r'\.py', r'', module_name)
        multithread_test_module = importlib.import_module(module_name)
    except Exception as e:
        raise e
    return multithread_test_module


def teardown():
    if os.path.exists(temp_test_file): os.remove(temp_test_file)

def test_caching():
    multithread_test_module = setup()
    multithread_test_module.test_caching()
    teardown()

def test_run_class():
    multithread_test_module = setup()
    multithread_test_module.test_run_class()
    teardown()

def test_runset_class():
    multithread_test_module = setup()
    multithread_test_module.test_runset_class()
    teardown()