#!/usr/bin/env python3
"""RZFeeser | rzfeeser@alta3.com"""

# standard library
import aiohttp
import asyncio

# create a coroutine called 'main'
async def main():           # the async keyword creates a coroutine to be run asynchronously

    async with aiohttp.ClientSession() as session:
        # request the pokemon 'Mew' (pokemon number 151)
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()     # passes control back to the event loop suspending execution of coroutine until
                                            # the awaited result is returned
            print(pokemon['name'])

asyncio.run(main())

