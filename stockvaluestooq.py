import os
import datetime as dt
import pandas_datareader.data as web

stock_code='9783'
stock_code_dr=stock_code + '.JP'

first='2024-01-01'
last = dt.date.today()

df = web.DataReader(stock_code_dr, data_source='stooq',start=first,end=last)

df.to_csv('stockdata_stooq.csv') 

""" df.sort_values(by='Date', ascending=True, inplace=True)

df_graph = df[['Open', 'High', 'Low', 'Close']]

df_graph.plot(kind='line') plt.show() """