from data_lib import data_stocks,data_stocks2, data_stocks2_label_adj_next
from data_lib import data1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from main_task import df

pd.set_option('display.max_columns', None)
#print(df)
#print(data_stocks)
#print(data_stocks.columns)
data_stocks['Date'] = pd.to_datetime(data_stocks['Date'])
df['date'] = pd.to_datetime(df['date'])

merge_df = pd.merge(df,data_stocks2,left_on='date',right_on='Date',how='inner')
merge_df = merge_df.drop('Date',axis=1)
merge_df = pd.DataFrame(merge_df)
merge_df2 = pd.merge(merge_df,data_stocks2_label_adj_next,how='inner', left_index=True,right_index=True)
#merge_df = merge_df.drop(columns=['Adj Close'])
merge_df2 = pd.DataFrame(merge_df2)
#print(data_stocks2_label_adj_next)
print(merge_df)
merge_df.to_csv('/home/pankhil/PycharmProjects/pythonProject5/data/out.csv')
