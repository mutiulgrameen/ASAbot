# bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from cleaner import clean_corpus
from cleaner2 import divideFile
#import pandas as pd

CORPUS_FILE = "E:\\grameen\\chatbot\\my_code_1\\data_air\\FinalDFTrain.csv"
#df = pd.read_csv(CORPUS_FILE, header=None)

#df1 = df.values.tolist()

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned_corpus = divideFile(CORPUS_FILE)
trainer.train(cleaned_corpus)
#trainer.train(CORPUS_FILE)

trainer.train([
    "Hi",
    "Welcome, friend 🤗",
])
trainer.train([
    "Hello",
    "Welcome, friend 🤗",
])
trainer.train([
    "Greetings",
    "Welcome, friend 🤗",
])

"""
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])
"""


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")