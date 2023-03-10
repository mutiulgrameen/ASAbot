# ashabot1.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from cleaner import clean_corpus
#from cleaner2 import divideFile
from db_process import process_db
#import pandas as pd

#CORPUS_FILE = "E:\\grameen\\chatbot\\my_code_1\\data_air\\FinalDFTrain.csv"
#df = pd.read_csv(CORPUS_FILE, header=None)

#df1 = df.values.tolist()

#chatbot = ChatBot("asha1", storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')
#chatbot = ChatBot("Johnny Five", read_only=True)
chatbot = ChatBot("asha1", logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch', 'default_response': 'I am sorry, but I do not understand.', 'maximum_similarity_threshold': 0.65}])
#chatbot.storage.drop()     # use to unlearn if needed



#### APP
#query = input("> ")
def chat_resp(query):
    # chatbot.storage.drop()     # use to unlearn if needed
    # CORPUS_FILE = "E:\\grameen\\chatbot\\my_code_1\\data_air\\db_mental.db"       # path to dataset
    # cleaned_corpus = process_db(CORPUS_FILE, 'Faq')
    # trainer = ListTrainer(chatbot)
    # trainer.train(cleaned_corpus)
    resp = chatbot.get_response(query)
    conf = resp.confidence
    return(resp, conf)     #
"""
    cleaned_corpus = divideFile(CORPUS_FILE)
    trainer = ListTrainer(chatbot)

    trainer.train(cleaned_corpus)
#trainer.train(CORPUS_FILE)
"""

#print(f"🪴 {chatbot.get_response(query)}")
    



"""
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
"""
trainer.train([
    "Are you a plant?",
    "No, I'm the pot below the plant!",
])
"""

"""
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
"""     
