set -e
cd ~/notebooks/data/ipums
# Create table
cat ./create_table.txt | ~/mapd/bin/mapdql -p HyperInteractive
# Import CSV
gzip -f -k -d ipums_easy.csv.gz
echo "COPY ipums_easy FROM '~/notebooks/data/ipums/ipums_easy.csv';" | ~/mapd/bin/mapdql -p HyperInteractive

