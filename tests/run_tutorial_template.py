import re
import os

def test_tutorial_template():
    with (open("examples/basic_tutorial.py", 'r') as f, 
        open("examples/_temp_tutorial.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            new_lines.append(re.sub(r"plt\.show\(\)", r"plt.close()", line))
        g.writelines(new_lines)
    try:
        from examples import _temp_tutorial
    except Exception as e:
        # if os.path.exists("examples/_temp_tutorial.py"): os.remove("examples/_temp_tutorial.py")
        raise e
    # if os.path.exists("examples/_temp_tutorial.py"): os.remove("examples/_temp_tutorial.py")