import aiohttp

async def get_response(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.post(
            f'http://api.brainshop.ai/get?bid=178&key=sX5A2PcYZbsN5EY6&uid=1&msg={query}'
        ) as resp:
            answer = await resp.json()
            return answer['cnt']
