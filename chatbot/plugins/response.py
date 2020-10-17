import aiohttp

async def get_response(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.post(
            f'https://heroku.mannu.me/bot?message={query}'
        ) as resp:
            answer = await resp.json()
            return answer['bot_response']