import pandas_datareader as web
import datetime
import json


# Function to return 52 week high and low.

def getweeklydata(stockname):
    print('Get Support Data For Stock : ' + stockname)
    end = datetime.datetime.now()
    start = end - datetime.timedelta(weeks=52)

    df = web.DataReader(stockname, 'yahoo', start, end)
    lowest_low = df['Low'].min()
    highest_high = df['High'].max()
    data = {}
    root = {}

    agg_dict = {'Open': 'first',
                'High': 'max',
                'Low': 'min',
                'Close': 'last',
                'Adj Close': 'last',
                'Volume': 'mean'}

    r_df = df.resample('W').agg(agg_dict)
    r_df_lastfiveweeksdata = r_df.tail()
    sortedr_df = sorted(r_df['Close'].values)
    data['lowestClose'] = str(round(sortedr_df[0], 2))
    lowestClosing = round(sortedr_df[0], 2)
    secondlowestClosing = round(sortedr_df[1], 2)
    length = r_df['Close'].values.__len__()
    lengthOfTail = r_df_lastfiveweeksdata.values.__len__()
    print(sortedr_df[0])
    for i in range(0, lengthOfTail):
        if r_df_lastfiveweeksdata.get('Close')[i] - sortedr_df[0] < sortedr_df[0] * 0.05:
            print('Closing price is less than 5% away from Lowest Closing in 52-Weeks. So a Buy')
            data['reco'] = 'STRONG_BUY'
            data['message'] = 'Closing price is less than 5% away from Lowest Closing in 52-Weeks'
            data['closingPrice'] = round(r_df_lastfiveweeksdata.get('Close')[i], 2);
            secondlowestClosing = r_df_lastfiveweeksdata.get('Close')[i]
            root['bestSupport'] = data

    for i in range(0, lengthOfTail):
        currentClosing = r_df_lastfiveweeksdata.get('Close')[i]
        currentOpening = r_df_lastfiveweeksdata.get('Open')[i]
        if currentOpening - currentClosing > currentClosing * 0.1 and (currentClosing > secondlowestClosing or
            currentClosing > lowestClosing):
            print('Closing price is 10% more than Opening')
            data = {}
            data['lowestClose'] = round(secondlowestClosing, 2)
            data['reco'] = 'BUY'
            data['message'] = 'Closing price is 10% more than Opening'
            data['closingprice'] = round(currentClosing, 2);
            root['secondbestsupport'] = data

    if root == {}:
        firstlowestclosing = 0
        for i in range(0, length):
            currentClosing = r_df['Close'][i]
            currentOpening = r_df['Open'][i]
            if currentOpening - currentClosing > currentClosing * 0.09 and currentClosing > lowestClosing:
                firstlowestclosing = currentClosing
                print(firstlowestclosing)
                for i in range(0, lengthOfTail):
                    currentClosing = r_df_lastfiveweeksdata.get('Close')[i]
                    if currentClosing > firstlowestclosing and currentClosing - firstlowestclosing < firstlowestclosing * 0.02:
                        print('Closing price is 2% more than highest range of open and close of 9%')
                        data = {}
                        data['lowestClose'] = round(firstlowestclosing, 2)
                        data['reco'] = 'BUY'
                        data['message'] = 'Closing price is 2% more than highest range of open and close of 9%'
                        data['closingprice'] = round(currentClosing, 2);
                        root['bestsupport'] = data

    if root == {}:
        firstlowestclosing = 0
        firstlowestlow = 0
        for i in range(0, length):
            currentClosing = r_df['Close'][i]
            currentOpening = r_df['Open'][i]
            currentLow = r_df['Low'][i]
            if currentOpening - currentClosing > currentClosing * 0.09 and currentClosing > lowestClosing:
                firstlowestclosing = currentClosing
                firstlowestlow = currentLow
                for i in range(0, lengthOfTail):
                    currentClosing = r_df_lastfiveweeksdata.get('Close')[i]
                    currentLow = r_df_lastfiveweeksdata.get('Low')[i]
                    if (currentClosing > firstlowestclosing and currentClosing - firstlowestclosing < firstlowestclosing * 0.02)\
                            or (currentLow > firstlowestclosing and currentLow - firstlowestclosing < firstlowestclosing * 0.02):
                        print('Closing price is 2% more than closing range of open and close of 9%')
                        data = {}
                        data['lowestClose'] = round(firstlowestclosing, 2)
                        data['reco'] = 'BUY'
                        data['message'] = 'Closing price is 2% more than closing range of open and close of 9%'
                        data['closingprice'] = round(currentClosing, 2);
                        root['bestsupport'] = data


    print(root)
    return root
#
symbol = 'HDFCLIFE.NS'
getweeklydata(symbol)
