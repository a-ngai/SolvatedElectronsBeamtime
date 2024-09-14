# %%
import nbformat
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.exporters import HTMLExporter, NotebookExporter
from fermi_libraries.common_functions import resolve_path
import pathlib
import os

try:
    CURRENT_SCRIPT_DIR = str(pathlib.Path(__file__).parent.resolve())+'/'
except NameError:  # this will happen in .ipynb files
    CURRENT_SCRIPT_DIR = os.path.abspath('')

target_dir = resolve_path(CURRENT_SCRIPT_DIR, 'examples')

PREPROCESS = False
CONVERT_TO_HTML = False

py_files_to_convert = [
    'basic_tutorial',
    'save_gdata',
    'basic_tof_calibration',
    'basic_filtering',
    'basic_abel_inversion',
    'basic_delay_analysis',
]

def main():

    for filename in py_files_to_convert:
        script_filepath = f'{target_dir}/{filename}.py'
        save_notebook_filepath = f'{target_dir}/{filename}.ipynb'
        success = os.system(f'ipynb-py-convert {script_filepath} {save_notebook_filepath}') == 0
        if not success:
            raise OSError(f'Could not convert ({script_filepath}) to ({save_notebook_filepath})')

    for filename in py_files_to_convert:
        notebook_filepath = f'{target_dir}/{filename}.ipynb'
        save_notebook_filepath = f'{target_dir}/{filename}.ipynb'
        save_html_filepath = f'{target_dir}/{filename}.html'
        with open(notebook_filepath) as f:
            nb = nbformat.read(f, as_version=4)
        
        if PREPROCESS:
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            try:
                ep.preprocess(nb, {'metadata': {'path': f'{target_dir}/'}})
            except Exception as e:
                raise RuntimeError(f'Problem processing ({notebook_filepath})').with_traceback(e.__traceback__)

        notebook_exporter = NotebookExporter()
        notebook_data, resources = notebook_exporter.from_notebook_node(nb)
        with open(save_notebook_filepath, "w") as f:
            f.write(notebook_data)
            f.close()

        if CONVERT_TO_HTML:
            html_exporter = HTMLExporter()
            html_data, resources = html_exporter.from_notebook_node(nb)
            with open(save_html_filepath, "w") as f:
                f.write(html_data)
                f.close()
                
if __name__ == "__main__":
    main()