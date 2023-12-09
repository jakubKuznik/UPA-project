#!/bin/bash 
python3 get-url.py > url_test.txt

python3 scrape-data.py --url-file url_test.txt --max 10

