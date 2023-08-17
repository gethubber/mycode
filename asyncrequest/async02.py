#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Demonstrating how to use the asyncio library by utilizing the pokeapi.co
   to perform 150 HTTP GET lookups"""

# standard library
import asyncio
import time

# python3 -m pip install aiohttp
import aiohttp

# start a timer to determine how quickly these lookups are performed
start_time = time.time()

async def main():

    async with aiohttp.ClientSession() as session:
        # loop from 1 to 150 (non inclusive of 151)
        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'    # number is defined by the range for-loop
            async with session.get(pokemon_url) as resp:     # the coroutine we are defining should be run async with an event loop
                pokemon = await resp.json()         # pass control back to the event loop (do other things until this happens)
                print(pokemon['name'])

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

