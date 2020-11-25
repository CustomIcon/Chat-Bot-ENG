import aiohttp
import asyncio

async def get_response(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            f'https://some-random-api.ml/chatbot?message={query}'
        ) as resp:
            return (await resp.json())['response']

async def main():
    print(await get_response('world'))

asyncio.run(main())
