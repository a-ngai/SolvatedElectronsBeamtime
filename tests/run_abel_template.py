import re
import os

def test_abel_template():
    with (open("examples/basic_abel_inversion.py", 'r') as f, 
        open("examples/_temp_abel.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            new_lines.append(re.sub(r"plt\.show\(\)", r"plt.close()", line))
        g.writelines(new_lines)
    try:
        from examples import _temp_abel
    except Exception as e:
        # if os.path.exists("examples/_temp_abel.py"): os.remove("examples/_temp_abel.py")
        raise e
    # if os.path.exists("examples/_temp_abel.py"): os.remove("examples/_temp_abel.py")