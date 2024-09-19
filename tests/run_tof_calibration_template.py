import re
import os

def test_tof_calibration_template():
    with (open("examples/py_scripts/basic_tof_calibration.py", 'r') as f, 
        open("examples/py_scripts/_temp_calibration.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            mod_line = re.sub(r"plt\.show\(\)", r"plt.close()", line)
            mod_line = re.sub(
                r"BEAMTIME_DIR = '/net/online4ldm/store/20234049/results/Beamtime'",
                r"BEAMTIME_DIR = find_subdir('TestBeamtime', resolve_path(CURRENT_SCRIPT_DIR, '..'))",
                mod_line)
            new_lines.append(mod_line)
        g.writelines(new_lines)
    try:
        from examples.py_scripts import _temp_calibration
    except Exception as e:
        # if os.path.exists("examples/py_scripts/_temp_calibration.py"): os.remove("examples/py_scripts/_temp_calibration.py")
        raise e
    if os.path.exists("examples/py_scripts/_temp_calibration.py"): os.remove("examples/py_scripts/_temp_calibration.py")