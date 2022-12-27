# bot1_eng.py

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from cleaner import clean_corpus

#CORPUS_FILE = "sampletrain1.txt"

chatbot = ChatBot("Training Example")

trainer = ChatterBotCorpusTrainer(chatbot)
#cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train("chatterbot.corpus.english")


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")