#!/bin/bash

set -e
source activate pycudf_notebook_py35
pip install https://s3.amazonaws.com/h2o-beta-release/goai/h2oaiglm-0.0.1-py2.py3-none-any.whl
pip install pandas
pip install seaborn
pip install psutil
pip install -e "git+https://github.com/fbcotter/py3nvml#egg=py3nvml"

