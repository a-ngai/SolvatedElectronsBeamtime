import re
import os

def test_multithread_cache_function():
    multithread_filepath = "tests/test_multithread_cache_saving_loading.py"
    with (open("tests/test_cache_saving_loading.py", 'r') as f, 
        open(multithread_filepath, 'w') as g):
        new_lines = []
        for line in f.readlines():
            mod_line = line
            mod_line = re.sub(
                r"from fermi_libraries.run_module import Run, RunSets",
                r"from fermi_libraries.run_module import MultithreadRun as Run, RunSets",
                mod_line)
            new_lines.append(mod_line)
        g.writelines(new_lines)
    try:
        from tests import test_multithread_cache_saving_loading
    except Exception as e:
        raise e
    if os.path.exists(multithread_filepath): os.remove(multithread_filepath)
