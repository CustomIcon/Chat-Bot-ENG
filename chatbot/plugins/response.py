
import aiohttp
import asyncio


async def get_response(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            f'https://some-random-api.ml/chatbot?message={query}'
        ) as resp:
            return (await resp.json()),['response']
    
#using an event loop
loop = asyncio.get_event_loop()
Task = asyncio.gather(*[get_response('response') for _ in range(500)])
    else:
Task = asyncio.gather(*[get_response('error') for _ in range(500)]
try:
    loop.run_until_complete(Task)
finally:
    loop.close()
