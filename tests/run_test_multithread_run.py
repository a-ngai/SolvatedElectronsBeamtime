import re
import os

def test_multithread_run():
    with (open("tests/test_multithread_run.py", 'r') as f, 
        open("tests/_temp_multithread_run.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            mod_line = re.sub(r"plt\.show\(\)", r"plt.close()", line)
            mod_line = re.sub(
                r"from fermi_libraries.run_module import Run, RunSets",
                r"from fermi_libraries.run_module import MultithreadRun as Run, RunSets",
                mod_line)
            mod_line = re.sub(
                r"BEAMTIME_DIR = '/net/online4ldm/store/20234049/results/Beamtime'",
                r"BEAMTIME_DIR = find_subdir('TestBeamtime', resolve_path(CURRENT_SCRIPT_DIR, '..'))",
                mod_line)
            new_lines.append(mod_line)
        g.writelines(new_lines)
    try:
        from tests import _temp_multithread_run
    except Exception as e:
        # if os.path.exists("test/_temp_multithread_run.py"): os.remove("test/_temp_multithread_run.py")
        raise e
    if os.path.exists("tests/_temp_multithread_run.py"): os.remove("tests/_temp_multithread_run.py")