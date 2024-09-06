import re
import os

def test_save_gdata():
    with (open("examples/save_gdata.py", 'r') as f, 
        open("examples/_temp.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            new_line = re.sub('nx = 256', "nx = 50", line)
            new_line = re.sub('save_half_path = None', "save_half_path = '_temp_half'", new_line)
            new_line = re.sub('save_quar_path = None', "save_quar_path = '_temp_quar'", new_line)
            new_lines.append(new_line)
        g.writelines(new_lines)
    try:
        from examples import _temp
    except Exception as e:
        if os.path.exists("examples/_temp.py"): os.remove("examples/_temp.py")
        if os.path.exists("examples/_temp_half.h5"): os.remove("examples/_temp_half.h5")
        if os.path.exists("examples/_temp_quar.h5"): os.remove("examples/_temp_quar.h5")
        raise e
    if os.path.exists("examples/_temp.py"): os.remove("examples/_temp.py")
    if os.path.exists("examples/_temp_half.h5"): os.remove("examples/_temp_half.h5")
    if os.path.exists("examples/_temp_quar.h5"): os.remove("examples/_temp_quar.h5")

