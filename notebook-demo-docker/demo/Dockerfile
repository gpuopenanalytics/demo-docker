# This Dockerfile take two optional build arguments:
# - MAPD_FILE is the name of the tarball for the mapd package.
#   Defaults to "mapd-os-3.0.1dev-20170508-21fc39f-Linux-x86_64"
# - PYGDF_COMMIT is the commit to use from the pygdf repo.
#   Defaults to "master".
FROM goai/base:latest

USER appuser
# Add MapD
# Manually downloaded mapd
ENV MAPD_FILE="mapd-os-3.2.3dev-20170909-e7053e6-Linux-x86_64-open"
COPY ./packages/${MAPD_FILE}.tar.gz ${MAPD_FILE}.tar.gz
# Extract MapD
RUN tar -xvf ${MAPD_FILE}.tar.gz
RUN ln -s $MAPD_FILE ./mapd

# Prepend path to libcuda and libjvm for mapd
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server/:/usr/local/nvidia/lib64/
RUN echo $LD_LIBRARY_PATH

# Add pygdf v0.1.0a2
RUN conda install -y --no-update-deps -c numba -c defaults -c conda-forge -c gpuopenanalytics/label/dev pygdf=0.1.0a2 numba=0.35 cudatoolkit=8

# Add pymapd
RUN conda install -y --no-update-deps  -c defaults -c pymapd/label/dev -c conda-forge -c gpuopenanalytics/label/dev pymapd
# Add jupyterlab
RUN conda install -y --no-update-deps jupyter notebook

# Add h2oaiglm dep
RUN conda install -y --no-update-deps pandas seaborn psutil scipy
# RUN pip install https://s3.amazonaws.com/h2o-beta-release/goai/h2oaiglm-0.0.1-py2.py3-none-any.whl
RUN pip install py3nvml

# Add utils script
COPY ./packages/utils ./utils
RUN ln -s ./utils/start_demo.sh ./start_demo.sh

COPY ./notebooks ./notebooks
USER root
RUN chown -R appuser ./notebooks

USER appuser

CMD bash ./utils/start_demo_notebook.sh
