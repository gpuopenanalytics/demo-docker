# This Dockerfile take two optional build arguments:
# - MAPD_FILE is the name of the tarball for the mapd package.
#   Defaults to "mapd-os-3.0.1dev-20170508-21fc39f-Linux-x86_64"
# - PYGDF_COMMIT is the commit to use from the pygdf repo.
#   Defaults to "master".
FROM conda_cuda_base:latest

USER root
# Install Java
RUN apt-get install -y openjdk-7-jre
RUN apt-get install -y libopenblas-dev

USER appuser
# Add MapD
ARG MAPD_FILE="mapd-os-3.1.1-20170628-45a6fa8-Linux-x86_64"
RUN wget https://builds.mapd.com/os/${MAPD_FILE}.tar.gz
# Extract MapD
RUN tar -xvf ${MAPD_FILE}.tar.gz
RUN ln -s $MAPD_FILE ./mapd

# Prepend path to libcuda and libjvm for mapd
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server/:/usr/local/nvidia/lib64/
RUN echo $LD_LIBRARY_PATH

# Add pygdf (pin to last known working commit)
ARG PYGDF_COMMIT="485cf15"
RUN git clone https://github.com/gpuopenanalytics/pygdf && cd pygdf && git checkout $PYGDF_COMMIT
RUN conda env create -f=pygdf/conda_environments/notebook_py35.yml && conda clean -iltpsy
RUN conda install conda-build=2.1.10 -y

# Add utils script
COPY ./packages/utils ./utils
RUN ln -s ./utils/start_demo.sh ./start_demo.sh

# Add h2oaiglm
RUN bash ./utils/pip_install_h2oaiglm.sh

CMD bash ./utils/start_demo_notebook.sh
