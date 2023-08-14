#!/usr/bin/env python3
"""Star Wars API HTTP response parsing"""

# pprint helps make things like dictionaries more human-readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

URL= "https://swapi.dev/api/people/1"

def main():
    """dissecting a requests.Response object"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)

    print("STATUS CODE and REASON:", resp.status_code, resp.reason)

    # dict() will force resp.headers into a dictionary format pprint can use
    pprint(dict(resp.headers))

if __name__ == "__main__":
    main()

