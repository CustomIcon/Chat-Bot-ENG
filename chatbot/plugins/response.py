import aiohttp
import asyncio


async def get_response(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            f'https://some-random-api.ml/chatbot?message={query}'
        ) as resp:
            return (await resp.json())['response']
async def BotThread():
    response = asyncio.run( get_response('world'))
    await asyncio.gather(*[get_response for _ in range(500)])
        
