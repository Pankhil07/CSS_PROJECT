from data_lib import data1
from tokenizer import tokenizer, finbert
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import transformers
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import BertTokenizer, BertForSequenceClassification
import time
inputs = data1['title']

inputs =inputs[:1000].to_list()

start = time.time()
nlp = pipeline("text-classification", model=finbert, tokenizer=tokenizer)
results = nlp(inputs)
end = time.time()



inputs = pd.DataFrame(inputs)

print(inputs)

results = results
results_df = pd.DataFrame(results)

print(results_df)

df = pd.concat([inputs, results_df], axis=1)

new_col_name = {0: 'Heading'}
df = df.rename(columns=new_col_name )

print(df)
print(f'Training the model took {(end-start)} seconds')