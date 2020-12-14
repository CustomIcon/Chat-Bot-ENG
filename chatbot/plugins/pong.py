import aiohttp

async def ping(query):):
    async with aiohttp.ClientSession() as ses:
        async with ses.post(
            f'https://blooming-brook-96225.herokuapp.com/?query=hi'
        ) as resp:
            answer = await resp.json()
            return answer['response']['time_taken']
