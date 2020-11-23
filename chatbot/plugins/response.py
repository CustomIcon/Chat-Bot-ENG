import aiohttp

async def get_response(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.post(
            f'https://some-random-api.ml/chatbot?message={query}'
        ) as resp:
            answer = await resp.json(content_type='text/html')
            return answer['response']['response']
