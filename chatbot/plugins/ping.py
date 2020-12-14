import asyncio
from pyrogram import filters as  Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..chatbot import chatbot


@chatbot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):
from chatbot.plugins.pong import ping


@chatbot.on_message(Filters.private & Filters.command("start"))
async def chat_bot(client, message):
    if message.text:
        chat_id = message.chat.id
        if await check_message(client, message):
            query = message.text
            await client.send_chat_action(chat_id, action='typing')
            rep = await get_response(query)
            await message.reply_text(rep)


async def check_message(client, message):
    if message.chat.type == 'private':
        return True
    Bot = await client.get_me()
    if message.text.lower() == f"@{Bot.username}":
        return True
    elif message.reply_to_message:
        return message.reply_to_message.from_user.id == Bot.id
    else:
        return False
