# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 08:40:22 2016

@author: nfett
BTC transaction
"""


import sys
import time, json, requests, csv, datetime
import pandas as pd 
import numpy as np


url="https://api.gdax.com"
product_id="BTC-USD" 

today = datetime.datetime.now()
three_hours = datetime.timedelta(hours=3)



titles = ('time','low','high','open','close','volume')
all_data =[]


def getProductHistoricRates(product='', start='', end='', granularity=''): 
    payload = { "start" : start, "end" : end,"granularity" : granularity} 


    response = requests.get(url + '/products/%s/candles' % (product), params=payload) 
    return response.json() 

lenny=1
x=0
while lenny > 0:
    x = x + 1
    tdelta = datetime.timedelta(hours=3 *x)
    endtime = today - tdelta
    starttime = endtime - three_hours
    data = getProductHistoricRates(product=product_id,start=starttime,end=endtime,granularity=60)
    for i in data:
        try:
            all_data.append(i)
        except: 
            pass
    lenny = len(data)
    time.sleep(1)


df = pd.DataFrame(all_data,columns=titles)
df['time']=pd.to_datetime(df['time'],unit='s')
print (df.head())
print (len(df))   
df.to_csv('coinbase_data.csv')
print (starttime,'to',today)

