#!/bin/bash 
python3 get-url.py > urls.txt & 
python3 scrape-data.py -url-file urls.txt -max 10 > produkty.tsv 

