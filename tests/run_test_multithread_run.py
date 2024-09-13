import re
import os

def test_multithread_run():
    with (open("tests/test_multithread_run.py", 'r') as f, 
        open("tests/_temp.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            new_lines.append(re.sub(r"plt\.show\(\)", r"plt.close()", line))
        g.writelines(new_lines)
    try:
        from examples import _temp
    except Exception as e:
        if os.path.exists("test/_temp.py"): os.remove("test/_temp.py")
        raise e
    if os.path.exists("test/_temp.py"): os.remove("test/_temp.py")