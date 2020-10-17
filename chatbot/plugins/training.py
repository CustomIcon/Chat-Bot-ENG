from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
cb = ChatBot('Example Bot')

# Start by training our bot with the ChatterBot corpus data
trainer = ChatterBotCorpusTrainer(cb)

trainer.train(
    'chatterbot.corpus.english'
)