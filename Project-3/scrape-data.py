## Program will scrape 100 urls from: 
# https://allegro.pl/kategoria/smartfony-i-telefony-komorkowe-165

## Usage: 
#./python3 path_to_chrome_drive -url-file urls.txt [-max] 
url="https://massi.pl/pl/57-wszystkie-umywalki"

import time
import socket
import sys
import argparse
import os
import pandas as pd
import requests
from typing import List, Any

script_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, script_directory)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


from bs4 import BeautifulSoup



#CHROME MODE
################################################
options = Options()
# Todo dat pryc na serveru 
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
## change to path so it works on merlin 
## or maybe use args  
path_to_chrome_driver = os.path.join(script_directory, 'drivers/chromedriver')
driver = webdriver.Chrome()

def parse_args():
  parser = argparse.ArgumentParser(description='UPA web scraper:', add_help=False)
  parser.add_argument("-h", "--help", action="count", default=0, help="./get-url.py path_to_chrome_driver")
  parser.add_argument("-url-file", dest="url_file", type=str, help="Path to the file containing URLs")
  parser.add_argument("-max", dest="max_items", type=int, default=100, help="Maximum number of items to scrape")

  try:
    args = parser.parse_args()
  except:
    sys.exit(1)
  
  return args

def scrape_data(urls):
  data_list = []
  for url in urls:
    driver.get(url)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, "html.parser")
    product_details = soup.find('div', class_='product-details js-product-details')

    if product_details:
      product_info = {}
      product_info["url"] = url

      product_name_element = soup.find('h1', class_='h1')
      product_name = product_name_element.text.strip()
      product_info["nazwa"] = product_name

      product_price_element = soup.find('span', class_='price--lg')
      product_price = product_price_element.text.strip()
      product_info["cena"] = product_price

      dt_details = product_details.find_all('div', class_='dt_detail')
      for dt_detail in dt_details:
        text_parts = list(dt_detail.stripped_strings)
        if len(text_parts) == 2:
          key = text_parts[0]
          value = text_parts[1]
          product_info[key] = value

      data_list.append(product_info)

  data = pd.DataFrame(data_list)
  data.to_csv(sys.stdout, sep='\t', header=False, index=False)

def main():
	
  args = parse_args()
  url_file = args.url_file

  if (url_file == None):
    print("Url file is missing. Please provide file in -url-file")
  
  urls = []

  with open(url_file, 'r') as file:
    urls.extend(file.read().splitlines())

  scrape_data(urls)
  driver.quit()


if __name__ == '__main__':
    start = time.time()
    main()
