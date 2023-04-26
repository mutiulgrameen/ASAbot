# cleaner.py

import re
import codecs
#import unicode
#import unicodedata

def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus

#chat_export_file = "E:\\grameen\\chatbot\\my_code_1\\data_air\\FinalDFTrain.csv"
def remove_chat_metadata(chat_export_file):
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # e.g. "9/16/22, 06:34"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # e.g. "Martin"
    metadata_end = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_end

    with codecs.open(chat_export_file, "r", encoding='utf-8', errors='ignore') as corpus_file:
#    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern, "", content)
#    cleaned_corpus = str(cleaned_corpus, errors='ignore')
#    print(tuple(cleaned_corpus.split(",")))
    #return (tuple(cleaned_corpus.split("\n")))
    return (tuple(cleaned_corpus.split("\n")) and tuple(cleaned_corpus.split(",")))
    
#print(remove_chat_metadata("E:\\grameen\\chatbot\\my_code_1\\data_air\\FinalDFTrain.csv"))


def remove_non_message_text(export_text_lines):
    messages = export_text_lines[1:-1]

    filter_out_msgs = ("<Media omitted>", "Missed voice call",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))




"""
if __name__ == "__main__":
    message_corpus = remove_chat_metadata("sampletrain1.txt")
    cleaned_corpus = remove_non_message_text(message_corpus)
    print(cleaned_corpus)
"""