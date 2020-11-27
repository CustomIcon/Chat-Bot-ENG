import aiohttp
import asyncio
from multithreading import threading

async def get_response(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
            f'https://some-random-api.ml/chatbot?message={query}'
        ) as resp:
            return (await resp.json())['response']
def BotThread():
    response = asyncio.run( get_response('world'))
    print(response)
        
def main():
    # Create ten threads as follows
    try:
        thread.start_new_thread( BotThread, ("Thread-1", 2, ) )
        thread.start_new_thread( BotThread, ("Thread-2", 4, ) )
        thread.start_new_thread( BotThread, ("Thread-3", 6, ) )
        thread.start_new_thread( BotThread, ("Thread-4", 8, ) )
        thread.start_new_thread( BotThread, ("Thread-5", 10, ) )
        thread.start_new_thread( BotThread, ("Thread-6", 12, ) )
        thread.start_new_thread( BotThread, ("Thread-7", 14, ) )
        thread.start_new_thread( BotThread, ("Thread-8", 16, ) )
        thread.start_new_thread( BotThread, ("Thread-9", 18, ) )
        thread.start_new_thread( BotThread, ("Thread-10", 20, ) )
    except:
       print("Error: unable to start thread")
