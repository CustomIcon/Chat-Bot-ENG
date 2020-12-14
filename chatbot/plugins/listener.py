import asyncio
from pyrogram import filters
from chatbot import chatbot
from chatbot.plugins.response import get_response


@chatbot.on_message(
    ~filters.me &
    ~filters.edited &
    (filters.group | filters.private)
    ,
    group=1)
async def chat_bot(client, message):
    if message.text:
        chat_id = message.chat.id
        if await check_message(client, message):
            query = message.text
            await client.send_chat_action(chat_id, action='typing')
            rep = await get_response(query)
            await message.reply_text(rep)


async def check_message(client, message):
    if message.text == '/':
        return False
    Bot = await client.get_me()
    if message.text.lower() == f"@{Bot.username}":
        return True
    elif message.reply_to_message:
        return message.reply_to_message.from_user.id == Bot.id
    else:
        return False
