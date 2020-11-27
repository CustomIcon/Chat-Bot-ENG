

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
group1 = asyncio.gather(*[get_response("group 1.{}".format(i)) for i in range(1, 6)])
group2 = asyncio.gather(*[get_response("group 2.{}".format(i)) for i in range(1, 4)])
group3 = asyncio.gather(*[get_response("group 3.{}".format(i)) for i in range(1, 10)])
all_groups = asyncio.gather(group1, group2, group3)
results = loop.run_until_complete(all_groups)
loop.close()

print(results)
