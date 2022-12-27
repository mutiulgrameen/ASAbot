# bot2_air.py

# libraries
import os
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np

# change directory to dataset
os.chdir("E:\grameen\chatbot\my_code_1\data_air")

# create dataframe
df = pd.read_csv("atis_intents.csv", header=None)
#df_train = pd.read_csv("atis_intents_train.csv", header=None)
#df_test = pd.read_csv("atis_intents.csv", header=None)
#df.head()

# Get the DataFrame column names as a list
clist = list(df.columns)

# Rearrange list the way you like 
clist_new = clist[-1:]+clist[:-1]   # brings the last column in the first place

# Pass the new list to the DataFrame - like a key list in a dict 
dfnew = df[clist_new]
dfnew

# Train-Test Split
from sklearn.model_selection import train_test_split as tts
df_train,  df_test = tts(dfnew, test_size=0.25, shuffle=True)

#df_train.shape
#df_test.shape

# Save train data and test data as CSV
df_train.to_csv("FinalDFTrain.csv", index=False)
df_test.to_csv("FinalDFTest.csv", index=False)