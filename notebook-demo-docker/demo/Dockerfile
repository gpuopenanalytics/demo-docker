# This Dockerfile take two optional build arguments:
# - MAPD_FILE is the name of the tarball for the mapd package.
#   Defaults to "mapd-os-3.0.1dev-20170508-21fc39f-Linux-x86_64"
# - PYGDF_COMMIT is the commit to use from the pygdf repo.
#   Defaults to "master".
FROM goai/base:latest

ENV PYGDF_CONDA_ENV=pygdf_examples

USER appuser
# Add HAR data
RUN mkdir data
RUN wget -nv http://archive.ics.uci.edu/ml/machine-learning-databases/00344/Activity%20recognition%20exp.zip -O "data/Activity recognition exp.zip"

# Add MapD
# Manually downloaded mapd
ENV MAPD_FILE="mapd-os-3.2.3dev-20170909-e7053e6-Linux-x86_64-open"
ADD https://mapd-core-os-builds.s3.amazonaws.com/${MAPD_FILE}.tar.gz ${MAPD_FILE}.tar.gz
USER root
RUN chown appuser ${MAPD_FILE}.tar.gz

USER appuser
# Extract MapD
RUN tar -xvf ${MAPD_FILE}.tar.gz
RUN ln -s $MAPD_FILE ./mapd

# Prepend path to libcuda and libjvm for mapd
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server/:/usr/local/nvidia/lib64/
RUN echo $LD_LIBRARY_PATH

# Create environment
RUN conda create -n $PYGDF_CONDA_ENV python=3.6

# Add pygdf v0.1.0a2
RUN conda install -n $PYGDF_CONDA_ENV -y --no-update-deps -c numba -c defaults -c conda-forge -c gpuopenanalytics/label/dev pygdf=0.1.0a2=py36h01fc00e_29 numba=0.35 cudatoolkit=8

# Add pymapd
RUN conda install -n $PYGDF_CONDA_ENV -y --no-update-deps  -c defaults -c pymapd/label/dev -c conda-forge -c gpuopenanalytics/label/dev pymapd
# Add jupyterlab
RUN conda install -n $PYGDF_CONDA_ENV -y --no-update-deps jupyter notebook

# Add h2oaiglm dep
RUN conda install -n $PYGDF_CONDA_ENV -y --no-update-deps pandas seaborn psutil scipy
RUN source activate $PYGDF_CONDA_ENV && pip install https://s3.amazonaws.com/h2o-beta-release/goai/h2oaiglm-0.0.1-py2.py3-none-any.whl
RUN source activate $PYGDF_CONDA_ENV && pip install py3nvml

# Add h2o4gpu
ENV H2O4GPU_WHL="h2o4gpu-0.1.0-py36-none-any.whl"
ADD https://s3.amazonaws.com/h2o-release/h2o4gpu/releases/bleeding-edge/ai/h2o/h2o4gpu/0.1-nccl-cuda8/${H2O4GPU_WHL} ${H2O4GPU_WHL}
USER root
RUN chown appuser ${H2O4GPU_WHL}

# Install h2o4gpu
USER appuser
RUN source activate $PYGDF_CONDA_ENV && pip install ${H2O4GPU_WHL}
RUN source activate $PYGDF_CONDA_ENV && pip install feather-format


# Extra packages for the demo
RUN conda install -n $PYGDF_CONDA_ENV -y holoviews bokeh

# Add utils script
COPY ./packages/utils ./utils
RUN ln -s ./utils/start_demo.sh ./start_demo.sh

COPY ./notebooks ./notebooks
USER root
RUN chown -R appuser ./notebooks
RUN apt-get install -y unzip


USER appuser
RUN bash ./utils/create_har.sh

CMD bash ./utils/start_demo_notebook.sh
