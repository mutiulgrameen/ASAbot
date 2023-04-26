# ashabot1.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from db_process import process_db

#### APP

def chat_resp(query):
    chatbot = ChatBot("gmoina", logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch', 'default_response': 'I am sorry, but I do not understand.', 'maximum_similarity_threshold': 0.77}])

    # chatbot.storage.drop()     # use to unlearn if needed
    # CORPUS_FILE = "D:\\chatbot\\ASAbot-master\\data_air\\db_mfi.db"       # path to dataset #D:\chatbot\ASAbot-master\data_air
    # cleaned_corpus = process_db(CORPUS_FILE, 'faq')
    # #print(cleaned_corpus)                                                # debug
    # trainer = ListTrainer(chatbot)
    # trainer.train(cleaned_corpus)
    resp = chatbot.get_response(query)
    conf = resp.confidence
    print(conf)                                                            # debug
    return(resp, conf)     #
