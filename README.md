# README

## PYGDF end-to-end example.

In this demo, we will train 4000 regularized linear regression models on the U.S. Census dataset, with the goal to predict the income of a person, given approximately 447 data points (such as age, occupation, zip code, etc.)

By using multiple GPUs, we are able to speed up this process significantly, and can train about 40 models per second (on a DGX-1 with 8 GPUs)

## Additional Packages

The following files must be downloaded separately.

* `./demo/packages/mapd-os-3.0.1dev-20170508-21fc39f-Linux-x86_64.tar.gz`

    Can be downloaded by:
    `wget https://builds.mapd.com/os/mapd-os-3.0.1dev-20170508-21fc39f-Linux-x86_64.tar.gz`

* `./demo/packages/pygdf.tar.gz`

    Can be created by:

    ```bash
    git clone https://github.com/gpuopenanalytics/pygdf.git
    tar -czvf pygdf.tar.gz pygdf
    ```


## Docker Build

```bash
docker build -t conda_cuda_base:latest ./base
docker build -t cudf:latest ./demo
```

## Run Docker

```bash
nvidia-docker run -p 8888:8888 -ti cudf:latest
```

This launches the mapd, and the notebook automatically.

Login to the notebook with your browser by following the URL printed on the terminal.

Open `mapd_to_pygdf_to_h2oaiglm.ipynb` and hit "Run All" to test.
This notebook should run to the end without error.


## Diagnostic

To run on specific GPUs, use [NV_GPU](https://github.com/NVIDIA/nvidia-docker/wiki/nvidia-docker#gpu-isolation).

For example:

```bash
NV_GPU=0 nvidia-docker run -p 8888:8888 -ti cudf:latest
```
