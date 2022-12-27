# cleaner2.py

#import re
import codecs

def divideFile(chat_export_file):
    chat_export_file = divBySpace(chat_export_file)
    chat_export_file = divByComa(chat_export_file)
    return(chat_export_file)

def divBySpace(chat_export_file):
    with codecs.open(chat_export_file, "r", encoding='utf-8', errors='ignore') as corpus_file:
        content = corpus_file.read()
        return (tuple(content.split("\n")))
    
def divByComa(spaced_file):
    b = []
    for x in spaced_file:
        y = x.split(",")
        for z in y:
            b.append(z)
    return(b)
"""
def divByComa(chat_export_file):
    with codecs.open(chat_export_file, "r", encoding='utf-8', errors='ignore') as corpus_file:
        content = corpus_file.read()
        return (tuple(content.split(",")))
#    return ((chat_export_file.split(",")))
"""    
    
###
#print(divBySpace("E:\\grameen\\chatbot\\my_code_1\\data_air\\FinalDFTrain.csv"))
#print(divByComa("E:\\grameen\\chatbot\\my_code_1\\data_air\\FinalDFTrain.csv"))
#a = (divBySpace(divByComa("E:\\grameen\\chatbot\\my_code_1\\data_air\\FinalDFTrain.csv")))
#print(a)

"""
a = divideFile("E:\\grameen\\chatbot\\my_code_1\\data_air\\FinalDFTrain.csv")
print(a)
a.shape()
"""
"""
b = []
for x in a:
    y = x.split(",")
    for z in y:
        b.append(z)
#    b.append(y)
print(b)

#a[55]
"""
"""
with codecs.open("E:\\grameen\\chatbot\\my_code_1\\data_air\\FinalDFTrain.csv", "r", encoding='utf-8', errors='ignore') as corpus_file:
        content = corpus_file.read()
        #return (tuple(content.split(",")))
        print(content)
"""
"""
"""