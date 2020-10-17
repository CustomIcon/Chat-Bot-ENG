import asyncio
from pyrogram import filters
from chatbot import chatbot, BotID, BotUsername
from chatbot.plugins.training import cb


@chatbot.on_message(~filters.me & ~filters.edited & ~filters.command(['start', f'start@{BotUsername}'], prefixes='/') & (filters.group | filters.private), group=6)
async def chat_bot(client, message):
    chat_id = message.chat.id
    if message.text and not message.document:
        if not await check_message(message):
            return
        query = message.text
        await client.send_chat_action(chat_id, action='typing')
        rep = cb.get_response(query)
        await message.reply_text(rep)


async def check_message(message):
    if message.chat.type == 'private':
        return True
    else:
        if message.text.lower() == f"@{BotUsername}":
            return True
        if message.reply_to_message:
            if message.reply_to_message.from_user.id == BotID:
                return True
            else:
                return False
