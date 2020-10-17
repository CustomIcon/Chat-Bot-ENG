"""Client Initial."""
import logging
from configparser import ConfigParser
from datetime import datetime

from chatbot.chatbot import chatbot

# Logging at the start to catch everything
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.WARNING,
    handlers=[logging.StreamHandler()],
)
LOGS = logging.getLogger(__name__)

name = "chatbot"

BotUsername = ""
BotID = 0
BotName = ""

# Read from config file
config_file = f"{name}.ini"
config = ConfigParser()
config.read(config_file)

# Extra details
__version__ = "1.1"
__author__ = "pokurt"

# Global Variables
CMD_HELP = {}
client = None
START_TIME = datetime.now()

chatbot = chatbot(name)

async def get_bot():
    global BotID, BotName, BotUsername
    getbot = await chatbot.get_me()
    BotID = getbot.id
    BotName = getbot.first_name
    BotUsername = getbot.username
