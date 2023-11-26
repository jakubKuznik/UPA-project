## Program will scrape 100 urls from: 
# https://allegro.pl/kategoria/smartfony-i-telefony-komorkowe-165

## Usage: 
#./get-url.py path_to_chrome_drive 
url="https://allegro.pl/kategoria/smartfony-i-telefony-komorkowe-165"

import time
import socket
import sys
import argparse
import os
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
print("Path to Chrome Driver:", path_to_chrome_driver)
print("Options:", options)
driver = webdriver.Chrome()

urls = []


def parse_args():
  parser = argparse.ArgumentParser(description='UPA web scraper:', add_help=False)
  parser.add_argument("-h", "--help", action="count", default=0, help="./get-url.py path_to_chrome_driver")
  try:
    args = parser.parse_args()
  except:
    sys.exit(1)
  
  print(args)
  return args

## get maximum of maximum url 
def get_urls(maximum):

  # pwhile we dont have 100 smarthphones 
  print(url)
  driver.get(str(url))
  time.sleep(0.5)
  while True:
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    links = soup.find_all('a')
    for link in links:
      href = link.get('href')
      if href and "produkt/smartfon" in href:
        if href not in urls:
          urls.append(href) 
    ## if there are no more hrefs on page and we haven't reach 100 
      ## then go to next page 
    if len(urls) > 100:
      break;
    
    
  print(urls) 

def main():
	
  parse_args()
  get_urls(100)
  driver.quit()


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
