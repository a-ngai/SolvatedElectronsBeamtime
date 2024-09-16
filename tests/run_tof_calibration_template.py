import re
import os

def test_tof_calibration_template():
    with (open("examples/py_scripts/basic_tof_calibration.py", 'r') as f, 
        open("examples/py_scripts/_temp_calibration.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            new_lines.append(re.sub(r"plt\.show\(\)", r"plt.close()", line))
        g.writelines(new_lines)
    try:
        from examples.py_scripts import _temp_calibration
    except Exception as e:
        # if os.path.exists("examples/py_scripts/_temp_calibration.py"): os.remove("examples/py_scripts/_temp_calibration.py")
        raise e
    if os.path.exists("examples/py_scripts/_temp_calibration.py"): os.remove("examples/py_scripts/_temp_calibration.py")