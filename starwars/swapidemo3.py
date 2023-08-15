#!/usr/bin/env python3
"""Star Wars API HTTP response parsing"""

# pprint helps make things like dictionaries more human-readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

URL= "https://swapi.dev/api/people/1"

def main():
    """getting at the JSON attached to this response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)

    x= """
    The .content attribute returns the content (our Star Wars data)!...
    but in bytes. Bytes are a sequence of bits/bytes that represent data,
    but is only really meant to be read by machines.

    Note the superfluous apostrophes (') and the "b" character at the beginning of each line.
    """

    print(x)
    print(type(resp.content))
    pprint(resp.content)
    input()

    y= """
    The .text attribute will return the content as a string! Much more readable!
    However, this data is useless to us in most programs...
    we can't easily parse strings!
    """

    print(y)
    print(type(resp.text))
    pprint(resp.text)
    input()

    z= """
    The .json() method is wonderful. If the page is returning JSON, the .json() method
    will convert it into the Pythonic data equivalent! We can now use this data
    INFINITELY more effectively because it has been converted to a Python dictionary!
    """

    print(z)
    print(type(resp.json()))
    pprint(resp.json())

    # now we can do some cool stuff with the data we received!
    print("\n" + resp.json()["name"] + " is the protagonist of Star Wars! He appeared in the following films:")

    for film in resp.json()["films"]:
        print("  •", requests.get(film).json()["title"])

if __name__ == "__main__":
    main()

