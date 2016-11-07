import quandl
import csv
import datetime
import pandas as pd

now = datetime.datetime.now()
today = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

quandl.ApiConfig.api_key = "ernvt3f_Psui_ywdxf5d"

merged = quandl.get('NSE/BPCL + '.5', start_date = "2012-01-04", end_date = today')

with open ("E:/Neural Stock Prediction/NSE_Tickers/NSE_Oil.csv", "rb") as QTickers:
    reader = csv.reader(QTickers)
    for row in reader:
       try:
            data = quandl.get(row[0] + '.5', start_date = "2012-01-04", end_date = today)
            merged = merged.join(data, rsuffix = '_' + row[0])
        except:
            pass

QTickers.close()
    
merged.drop(merged.columns[[0]],inplace=True,axis=1,errors='ignore')
print merged

merged.to_csv('E:/Neural Stock Prediction/DataFrames/NSE_Oil_BPCL.csv')
