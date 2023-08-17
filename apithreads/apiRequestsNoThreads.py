#!/usr/bin/python3
"""API requests without threads | rzfeeser@alta3.com"""

# standard library
from time import time

# python3 -m pip install requests
import requests

# a list of apis from https://api.le-systeme-solaire.net/rest/bodies/
url_list = [
    "https://api.le-systeme-solaire.net/rest/bodies/lune",
    "https://api.le-systeme-solaire.net/rest/bodies/phobos",
    "https://api.le-systeme-solaire.net/rest/bodies/deimos",
    "https://api.le-systeme-solaire.net/rest/bodies/europe",
    "https://api.le-systeme-solaire.net/rest/bodies/callisto",
    "https://api.le-systeme-solaire.net/rest/bodies/himalia",
    "https://api.le-systeme-solaire.net/rest/bodies/elara",
    "https://api.le-systeme-solaire.net/rest/bodies/sinope",
    "https://api.le-systeme-solaire.net/rest/bodies/leda",
    "https://api.le-systeme-solaire.net/rest/bodies/thebe",
]

def download_file(url):
    html = requests.get(url, stream=True)
    return html.status_code

start = time()

for url in url_list:
    print(download_file(url))

# display the total run time
print(f'Time taken: {time() - start}')

