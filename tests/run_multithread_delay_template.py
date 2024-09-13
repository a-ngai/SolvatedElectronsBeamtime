import re
import os

def test_multithread_delay_template():
    with (open("examples/basic_delay_analysis.py", 'r') as f, 
        open("examples/_temp_multithread_delay.py", 'w') as g):
        new_lines = []
        for line in f.readlines():
            mod_line = re.sub(r"plt\.show\(\)", r"plt.close()", line)
            mod_line = re.sub(
                r"from fermi_libraries.run_module import Run, RunSets",
                r"from fermi_libraries.run_module import MultithreadRun as Run, RunSets",
                mod_line)

            new_lines.append(mod_line)
        g.writelines(new_lines)
    try:
        from examples import _temp_multithread_delay
    except Exception as e:
        # if os.path.exists("examples/_temp_multithread_delay.py"): os.remove("examples/_temp_multithread_delay.py")
        raise e
    # if os.path.exists("examples/_temp_multithread_delay.py"): os.remove("examples/_temp_multithread_delay.py")