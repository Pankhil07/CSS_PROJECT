import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import transformers
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import BertTokenizer, BertForSequenceClassification

data_elon = pd.read_csv('/home/pankhil/Downloads/mc-onlinenews-mediacloud-20240122211520-content.csv')

data1 = data_elon.copy()

data_tesla  = pd.read_csv('/home/pankhil/Downloads/mc-onlinenews-mediacloud-20240122210956-content.csv')

data2 = data_tesla.copy

data1 = data1.drop(['id','indexed_date','language','media_name','media_url','url'],axis=1)