set -e
# Create table
cd ~/pygdf/notebooks
cat ~/pygdf/notebooks/create_table_ipums_easy.txt | ~/mapd/bin/mapdql -p HyperInteractive
# Import CSV
gzip -f -k -d ipums_easy.csv.gz
echo "COPY ipums_easy FROM '~/pygdf/notebooks/ipums_easy.csv';" | ~/mapd/bin/mapdql -p HyperInteractive
