import aiohttp
import asyncio


_sem = None


async def get_response(query):
    async with _sem:
        async with aiohttp.ClientSession() as ses:
            async with ses.get(f'https://some-random-api.ml/chatbot?message={query}') as resp:
                return (await resp.json())['response']


async def main():
    global _sem
    _sem = asyncio.Semaphore(10)  # read https://stackoverflow.com/q/48483348/1113207

    return await asyncio.gather(*[get_response(i) for i in range(20)])

   
res = asyncio.run(main())
print(res)
