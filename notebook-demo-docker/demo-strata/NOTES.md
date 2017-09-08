# Notes

## Dataset

* http://archive.ics.uci.edu/ml/datasets/Heterogeneity+Activity+Recognition#

## Run

* Launch docker container from `<source-root>/notebook-demo-docker`; map port 8888; map demo-strata dir; and, override startup CMD:
  ```bash
  nvidia-docker run -v `pwd`/demo-strata:/home/appuser/demo-strata  -p 8888:8888 -ti goai/demo:latest /bin/bash
  ```
* Once in the docker, move into ~/demo-strata dir
* Download data from http://archive.ics.uci.edu/ml/machine-learning-databases/00344/Activity%20recognition%20exp.zip and unzip.  The CSV data should be in ~/demo-strata/data/Activity_recognition_exp
* run
  ```bash
  pip install h2o4gpu-0.0.3-py2.py3-none-any.whl
  ```
* run
  ```bash
  conda install -c numba numba
  ```
  (got downgraded from previous cmd)
* launch mapd-server with `~/utils/start_mapd.sh` and keep in running

* launch
  ```bash
  cd ~/demo-strata
  jupyter notebook --ip=*
  ```
* load data with "Load data into mapd" notebook
* the processing & KMeans is in the "Analysis" notebook

optionally, in the host, launch cpugpu heatmap with `bokeh serve --allow-websocket-origin=<machine-name>:5006 cpugpu_heatmap.py` in ~/demo-strata dir.
It depends on `py3nvml` and `psutil` (pip install-able).


## Issues

* MapD requires LIMIT on the SQL query.
  Otherwise, it raises the error:
  "Exception: Query would require a scan without a limit on table(s): <table_name>"
  Large LIMIT also got rejected with the same error.

* h2o4gpu is downgrading Numba and other packages.
  (e.g. it should use numba >= 0.35.0 versions to accept new versions.)

* h204gpu.KMeans lack fit_ptr to take GPU ptr.

