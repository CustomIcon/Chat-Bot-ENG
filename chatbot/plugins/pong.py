import aiohttp
from pyrogram import filters as  Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..chatbot import chatbot


@chatbot.on_message(Filters.private & Filters.command("ping"))

async def start(query):
    async with aiohttp.ClientSession() as ses:
        async with ses.post(
            f'https://blooming-brook-96225.herokuapp.com/?query=hi'
        ) as resp:
            answer = await resp.json()
            return answer['response']['time_taken']
