#!/usr/bin/python3
"""API requests with threads | rzfeeser@alta3.com"""

# standard library
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time

# python3 -m pip install requests
import requests


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

processes = []

# we want to be careful with the number of workers
# if you are making thousands of requests, does your target have limiting engaged?
# beware you don't overload internal or external services; 5 to 10 is fine for most scripts
with ThreadPoolExecutor(max_workers=5) as executor:
    for url in url_list:
        processes.append(executor.submit(download_file, url))   # add a new task to the threadpool and store in processes list

for task in as_completed(processes):    # yields the items in processes as they complete (it finished or was canceled)
    print(task.result())

# display the total run time 
print(f'Time taken: {time() - start}')

