H2OAIGLM is a solver for convex optimization problems in _graph form_ using [Alternating Direction Method of Multipliers] (ADMM).

Requirements
------
CUDA8 for GPU version, OpenMP (for distributed GPU version)

Add to .bashrc or your own environment (e.g.):
------

export CUDA_HOME=/usr/local/cuda
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH_MORE=/home/$USER/lib/:$CUDA_HOME/lib64/:$CUDA_HOME/lib/:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:LD_LIBRARY_PATH_MORE
export CUDADIR=/usr/local/cuda/include/
export OMP_NUM_THREADS=32
export MKL_NUM_THREADS=32
export VECLIB_MAXIMUM_THREADS=32
