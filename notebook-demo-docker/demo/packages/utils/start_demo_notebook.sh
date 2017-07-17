set -e
bash ~/utils/start_demo.sh

cd ~/notebooks
jupyter notebook --ip=*
