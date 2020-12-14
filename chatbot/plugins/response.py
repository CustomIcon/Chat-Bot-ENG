import aiohttp

async def get_response(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.post(
            f'https://blooming-brook-96225.herokuapp.com/query={query}'
        ) as resp:
            answer = await resp.json()
            return answer['response']['bot']
