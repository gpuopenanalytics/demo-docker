# READ ME

## Additional Packages

The following files must be downloaded separately.

* `./demo/packages/mapd-2.3.1dev-20170414-67568ff-Linux-x86_64.tar.gz`

    Contact mapd for this tarball.

* `./demo/packages/pygdf.tar.gz`

    Can be created by:

    ```bash
    tar -czvf pygdf.tar.gz pygdf
    ```

(Note: this will be easier once the packages are public.)


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

Open `mapd_to_pygdf_to_matrix_2-smallipums.ipynb` and hit "Run All" to test.
This notebook should run to the end without error.


## Diagnostic

To run on specific GPUs, use [NV_GPU](https://github.com/NVIDIA/nvidia-docker/wiki/nvidia-docker#gpu-isolation).

For example:

```bash
NV_GPU=0 nvidia-docker run -p 8888:8888 -ti cudf:latest
```
