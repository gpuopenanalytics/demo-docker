set -e
bash ~/utils/start_demo.sh

cd ~/notebooks
source activate $PYGDF_CONDA_ENV
jupyter notebook --ip=*
