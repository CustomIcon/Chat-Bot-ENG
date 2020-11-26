import aiohttp
import asyncio

async def get_response(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            f'https://some-random-api.ml/chatbot?message={query}'
        ) as resp:
            return (await resp.json())['response']
def main():
    print(asyncio.run(get_response('world')))
