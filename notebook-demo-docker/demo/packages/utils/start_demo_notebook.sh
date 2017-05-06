set -e
~/utils/start_demo.sh

source activate pycudf_notebook_py35
cd ~/pygdf
# add pygdf to path
conda develop .
cd notebooks
jupyter notebook --ip=*