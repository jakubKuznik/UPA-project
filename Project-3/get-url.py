import time
import argparse
import os
from bs4 import BeautifulSoup
import requests

url = "https://massi.pl/pl/57-wszystkie-umywalki"

urls = []

def parse_args():
    parser = argparse.ArgumentParser(description='UPA web scraper:', add_help=False)
    parser.add_argument("-h", "--help", action="count", default=0, help="./get-url.py path_to_chrome_driver")
    try:
        args = parser.parse_args()
    except:
        sys.exit(1)

    return args


def get_urls(maximum):
    urls = []
    current_page = 1

    while len(urls) < maximum:
        response = requests.get(f"{url}?page={current_page}")
        if response.status_code != 200:
            print(f"Failed to fetch page {current_page}. Status code: {response.status_code}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', class_="product-miniature__thumb-link")

        for link in links:
            href = link.get('href')
            if href and "umywalka" in href and href not in urls:
                urls.append(href)

        current_page += 1

    return urls[:maximum]

def main():
    parse_args()
    urls = get_urls(100)
    for u in urls:
        print(u)


if __name__ == '__main__':
    start = time.time()
    main()

