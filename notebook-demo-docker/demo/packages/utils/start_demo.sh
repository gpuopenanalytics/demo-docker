#!/bin/bash
set -e
cd ~/utils

# start mapd
echo "Start MAPD"
cmd="nohup ./start_mapd.sh"
$cmd &disown

echo "Wait for mapd to start"
sleep 10

# load data
echo "Import CSV"
bash ./create_ipums_easy.sh
