import re
import os

def test_filtering_template():
    with (open("examples/basic_filtering.py", 'r') as f, 
        open("examples/_temp.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            new_lines.append(re.sub(r"plt\.show\(\)", r"plt.close()", line))
        g.writelines(new_lines)
    try:
        from examples import _temp
    except Exception as e:
        if os.path.exists("examples/_temp.py"): os.remove("examples/_temp.py")
        raise e
    if os.path.exists("examples/_temp.py"): os.remove("examples/_temp.py")
