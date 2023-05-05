import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

df = pd.read_excel("Chat Statistics.xlsx", header=2)

df1 = df["Conversations"]

print(df1.head(1))