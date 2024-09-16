import re
import os

def test_multithread_run():
    with (open("tests/test_multithread_run.py", 'r') as f, 
        open("tests/_temp_multithread_run.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            new_lines.append(re.sub(r"plt\.show\(\)", r"plt.close()", line))
        g.writelines(new_lines)
    try:
        from tests import _temp_multithread_run
    except Exception as e:
        # if os.path.exists("test/_temp_multithread_run.py"): os.remove("test/_temp_multithread_run.py")
        raise e
    if os.path.exists("tests/_temp_multithread_run.py"): os.remove("tests/_temp_multithread_run.py")