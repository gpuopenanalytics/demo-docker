# README

This repository contains demo notebooks for the GPU DataFrame (GDF).


## Demos

### GDF end-to-end example on US Census dataset

In this demo, we will train 4000 regularized linear regression models on the U.S. Census dataset, with the goal to predict the income of a person, given approximately 447 data points (such as age, occupation, zip code, etc.)

By using multiple GPUs, we are able to speed up this process significantly, and can train about 40 models per second (on a DGX-1 with 8 GPUs)


Notebook: `mapd_to_pygdf_to_h2oaiglm.ipynb`.
Uses: mapd, pymapd, pygdf, h2oaiglm


### PyMapD and PyGDF demo on NY Taxi dataset

This is a simple example that demonstrates the use of PyMapD to create a table, populate
it and fetch query result as a GDF.  Then, we show some common PyGDF dataframe operations on
the GDF; for example, groupby, join, and transform columns with custom Python code that is
just-in-time compiled into GPU code.

Notebook: `nytaxi-pymapd-pygdf.ipynb`
Uses: mapd, pymapd, pygdf


## Setup

### Docker Build

To build the docker image, go into the `./notebook-demo-docker` and run:

```bash
docker build -t goai/base:latest ./base
docker build -t goai/demo:latest ./demo
```

### Run Docker

```bash
nvidia-docker run -p 8888:8888 -ti goai/demo:latest
```

This launches the mapd, and the notebook automatically.

Login to the notebook with your browser by following the URL printed on the terminal.

Open `mapd_to_pygdf_to_h2oaiglm.ipynb` and hit "Run All" to test.
This notebook should run to the end without error.


### Diagnostic

To run on specific GPUs, use [NV_GPU](https://github.com/NVIDIA/nvidia-docker/wiki/nvidia-docker#gpu-isolation).

For example:

```bash
NV_GPU=0 nvidia-docker run -p 8888:8888 -ti goai/demo:latest
```
