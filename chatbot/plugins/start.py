from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from chatbot import chatbot

text = """
Hello [{firstname}](tg://user?id={userid})
I'm a Chatbot developed by Developers in EagleUnion for testing and learning purposes. I am opensource.
for now I can only speak English, Italian, French, German, Spanish and Portuguese.
"""
@chatbot.on_message(filters.command("start"))
async def alive(_, message):
    await message.reply(text.format(firstname=message.from_user.first_name,
                                    userid=message.from_user.id))