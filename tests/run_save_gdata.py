import re
import os

def test_save_gdata():
    with (open("examples/py_scripts/save_gdata.py", 'r') as f, 
        open("examples/py_scripts/_temp_save_gdata.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            new_line = re.sub('nx = 225', "nx = 50", line)
            new_line = re.sub('save_half_path = None', "save_half_path = '_temp_save_gdata_half.py'", new_line)
            new_line = re.sub('save_quar_path = None', "save_quar_path = '_temp_save_gdata_quar.py'", new_line)
            new_lines.append(new_line)
        g.writelines(new_lines)
    try:
        from examples.py_scripts import _temp_save_gdata
    except Exception as e:
        # if os.path.exists("examples/py_scripts/_temp_save_gdata.py"): os.remove("examples/py_scripts/_temp_save_gdata.py")
        if os.path.exists("examples/py_scripts/_temp_save_gdata_half.h5"): os.remove("examples/py_scripts/_temp_save_gdata_half.h5")
        if os.path.exists("examples/py_scripts/_temp_save_gdata_quar.h5"): os.remove("examples/py_scripts/_temp_save_gdata_quar.h5")
        raise e
    # if os.path.exists("examples/py_scripts/_temp_save_gdata.py"): os.remove("examples/py_scripts/_temp_save_gdata.py")
    if os.path.exists("examples/py_scripts/_temp_save_gdata_half.h5"): os.remove("examples/py_scripts/_temp_save_gdata_half.h5")
    if os.path.exists("examples/py_scripts/_temp_save_gdata_quar.h5"): os.remove("examples/py_scripts/_temp_save_gdata_quar.h5")
    if os.path.exists("examples/py_scripts/_temp_save_gdata.py"): os.remove("examples/py_scripts/_temp_save_gdata.py")