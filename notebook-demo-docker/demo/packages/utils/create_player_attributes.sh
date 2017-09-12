set -e
cd ~/notebooks/data/player_attributes
# Create table
cat ./create_table_player_attributes.txt | ~/mapd/bin/mapdql -p HyperInteractive
# Import CSV
gzip -f -k -d player_attributes.csv.gz
echo "COPY player_attributes FROM '~/notebooks/data/player_attributes/player_attributes.csv';" | ~/mapd/bin/mapdql -p HyperInteractive
