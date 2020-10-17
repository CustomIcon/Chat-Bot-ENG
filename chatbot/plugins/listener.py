import asyncio
from pyrogram import filters
from chatbot import chatbot
from chatbot.plugins.response import get_response


@chatbot.on_message(
    ~filters.me &
    ~filters.edited &
    ~filters.command('start', prefixes='/') &
    (filters.group | filters.private)
    ,
    group=1)
async def chat_bot(client, message):
    chat_id = message.chat.id
    if message.text:
        if await check_message(client, message):
            query = message.text
            await client.send_chat_action(chat_id, action='typing')
            rep = await get_response(query)
            await message.reply_text(rep)


async def check_message(client, message):
    if message.chat.type == 'private':
        return True
    else:
        Bot = await client.get_me()
        if message.text.lower() == f"@{Bot.username}":
            return True
        elif message.reply_to_message:
            if message.reply_to_message.from_user.id == Bot.id:
                return True
            else:
                return False
        else:
            return False
