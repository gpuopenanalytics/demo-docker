FROM nvidia/cuda:8.0-devel-ubuntu16.04

# needed for source activate with conda
SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get install -y wget git vim

# Add user
RUN useradd -ms /bin/bash appuser
USER appuser
WORKDIR /home/appuser

# Download miniconda
RUN wget https://repo.continuum.io/miniconda/Miniconda3-4.3.11-Linux-x86_64.sh
# Install miniconda
RUN bash Miniconda3-4.3.11-Linux-x86_64.sh -b -p /home/appuser/Miniconda3
# Append PATH to miniconda
ENV PATH=$PATH:/home/appuser/Miniconda3/bin

# Install Java
USER root
RUN apt-get update --fix-missing
RUN apt-get install -y default-jre-headless
RUN apt-get install -y libopenblas-dev

USER appuser
