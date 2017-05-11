FROM conda_cuda_base:latest

USER root
# Install Java
RUN apt-get install -y openjdk-7-jre
RUN apt-get install -y libopenblas-dev

USER appuser
# Add MapD
COPY ./packages/mapd-os-3.0.1dev-20170508-21fc39f-Linux-x86_64.tar.gz ./mapd.tar.gz
# Extract MapD
RUN tar -xvf mapd.tar.gz
RUN ln -s mapd-os-3.0.1dev-20170508-21fc39f-Linux-x86_64 ./mapd

# Prepend path to libcuda and libjvm for mapd
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/jvm/java-7-openjdk-amd64/jre/lib/amd64/server/:/usr/local/nvidia/lib64/
RUN echo $LD_LIBRARY_PATH

# Add pygdf
COPY ./packages/pygdf.tar.gz ./pygdf.tar.gz
RUN tar -xvf ./pygdf.tar.gz
RUN conda env create -f=pygdf/conda_environments/notebook_py35.yml && conda clean -iltpsy
RUN conda install conda-build=2.1.10 -y

# Add utils script
COPY ./packages/utils ./utils
RUN ln -s ./utils/start_demo.sh ./start_demo.sh

# Add h2oaiglm
RUN bash ./utils/pip_install_h2oaiglm.sh

CMD bash ./utils/start_demo_notebook.sh
