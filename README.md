# README

This repository contains demo notebooks for the GPU DataFrame (GDF).


## Demos

### Getting Started with GDF
Notebook: [Getting Started with GDF](https://github.com/gpuopenanalytics/demo-docker/blob/master/notebook-demo-docker/demo/notebooks/getting_started.ipynb)
Uses: pygdf, h2o4gpu

A quick start to loading data into a Pandas data frame and converting it to a GDF, then manipulating it.


### GDF End-to-End Example on US Census Dataset
Notebook: [MapD to PyGDF to H2OAIGLM](https://github.com/gpuopenanalytics/demo-docker/blob/master/notebook-demo-docker/demo/notebooks/mapd_to_pygdf_to_h2oaiglm.ipynb)
Uses: mapd, pymapd, pygdf, h2oaiglm

In this demo, we will train 4000 regularized linear regression models on the U.S. Census dataset, with the goal to predict the income of a person, given approximately 447 data points (such as age, occupation, zip code, etc.)

By using multiple GPUs, we are able to speed up this process significantly, and can train about 40 models per second (on a DGX-1 with 8 GPUs)


### PyMapD and PyGDF Demo on NY Taxi Dataset
Notebook: [PyMapD and PyGDF Demo on NY Taxi Data Subset](https://github.com/gpuopenanalytics/demo-docker/blob/master/notebook-demo-docker/demo/notebooks/nytaxi-pymapd-pygdf.ipynb)
Uses: mapD, pymapd, pygdf

This is a simple example that demonstrates the use of PyMapD to create a table, populate
it and fetch query result as a GDF.  Then, we show some common PyGDF dataframe operations on
the GDF; for example, groupby, join, and transform columns with custom Python code that is
just-in-time compiled into GPU code.


### Human Activity Recognition using GDF and GPU KMeans
Notebook: [Human Activity Recognition using GPU DataFrame and GPU KMeans](https://github.com/gpuopenanalytics/demo-docker/blob/master/notebook-demo-docker/demo/notebooks/har_dataset_pygdf_h2o4gpu.ipynb)
Uses: pygdf, kmeans, h2o4gpu

Analyzing smart phone sensors to determine the activity the person is engaged in.

Our approach uses KMeans from the h2o4gpu package to form the initial clusters. Then, we use nearest neighbour to classify the clusters; i.e. the intra-cluster dominating class determines the class for the cluster. During the classification, we choose the class of the closest cluster center.


### PyMapD to H2OGPUML to MapD on FIFA Football Dataset
Notebook: [PyMapD to H2OGPUML to MapD on FIFA Football Dataset](https://github.com/gpuopenanalytics/demo-docker/blob/master/notebook-demo-docker/demo/notebooks/pymapd_to_h2ogpuml_to_mapd.ipynb)
Uses: mapD, h2o4gpu

In this demo, we will train 4000 regularized linear regression models on the FIFA Football dataset, with the goal to predict the overall rating of the player, given different feature sets (such as potential, finishing, strength, etc.)


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
