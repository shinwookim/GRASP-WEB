import nbformat
import shutil
import os
from nbconvert.preprocessors import ExecutePreprocessor

def copy_template(template_path, notebook_path):
    shutil.copyfile(template_path, notebook_path)

def run_notebook(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': 'notebooks/'}})
    with open(notebook_path, 'wt') as f:
        nbformat.write(nb, f)

def create_notename(dataset, hpo_strategy, run_id, time):
    return dataset + '_' + hpo_strategy + '_' + run_id + '_' + time + '.ipynb'