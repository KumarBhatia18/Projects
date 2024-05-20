import pandas_datareader.data as web
import datetime
import json


# Function to return 52 week high and low.

def get52week(stockname):
    print('Get 52 Week High and Low For : ' + stockname)
    end = datetime.datetime.now()
    start = end - datetime.timedelta(weeks=52)

    df = web.DataReader('AAPL', 'stooq', start, end)
    print(df)
    highest_high = df['High'].max()
    lowest_low = df['Low'].min()

    root = {}
    data = {}
    data['high'] = highest_high
    data['low'] = lowest_low
    root['52week'] = data
    print('52 Week High and Low For : ' + stockname + " is " + str(root))
    return root


symbol = 'MARUTI.NSE'
json_data = get52week(symbol)
