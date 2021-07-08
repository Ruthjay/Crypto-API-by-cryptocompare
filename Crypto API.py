from google.colab import drive
drive.mount('drive')
drive.mount('/drive')

import requests
import pandas as pd
from datetime import datetime
import time

URL = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}"
i = 0

#testTable = pd.DataFrame(date_time = "Date", currentPrice = "currentPrice")
data = pd.DataFrame(columns = ['Date','currentPrice'])

def get_price(coin, currency):
  try:
    response = requests.get(URL.format(coin, currency)).json()
    return response
  except:
    return False

#f = open("save.txt","w+") 

while True:
    date_time = datetime.now()
    date_time = date_time.strftime("%d/%m/%Y %H:%M:%S")
    #currentPrice = get_price("BTC", "USD")
    #currentPrice = get_price("USDT", "USD")
    currentPrice = get_price("BTC", "USDT")
    if currentPrice:
      print(date_time, "$", currentPrice)
      data.loc[i] = [date_time, currentPrice]
      data.to_csv('Crypo_data_20210701_01.csv')
      data.to_csv('/drive/My Drive/Crypo_data_20210701_01.csv')
    time.sleep(1)
    i += 1
    data.to_csv('Crypo_data_20210628_01.csv')
    data.to_csv('/drive/My Drive/Crypo_data_20210701_01.csv')

#f.close() 