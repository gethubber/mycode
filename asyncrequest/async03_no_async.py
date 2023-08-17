#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Synchronous requests, this should be much slower than the asynchronous method"""
   
# standard library
import time

# python3 -m pip install requests
import requests

def main():
    # start a timer
    start_time = time.time()

    # typical loop
    for number in range(1, 151):
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(url)
        pokemon = resp.json()
        print(pokemon['name'])

    print("--- %s seconds ---" % (time.time() - start_time))
    
# call our script if it was not imported
if __name__ == "__main__":
    main()

