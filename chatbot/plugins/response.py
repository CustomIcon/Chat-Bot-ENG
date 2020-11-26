import aiohttp
import asyncio #to run async funtions you need to import asyncio

async def get_response(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            f'https://some-random-api.ml/chatbot?message={query}'
        ) as resp:
            return (await resp.json())['response']

print((asyncio.run( get_response('world')))
