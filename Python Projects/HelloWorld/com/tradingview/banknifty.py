from tradingview_ta import TA_Handler, Interval, Exchange
from bankniftymovingaverage import *
import datetime

stockList = {"M_M": 'M&M.NS'}
count = 0
openingRSI = 0
lowestRSI = False
for stock in stockList:
    while(True):
        json_data = getstockdata(stock, stockList[stock])
        vwma = json_data["15m"]["vwma"]
        cmp = json_data["15m"]["cmp"]
        rsi = float(json_data["15m"]["rsi"])
        boughtPrice = 0

        if count == 0:
            openingRSI = rsi

        count = count + 1

        print("\n")
        print("CMP: " + str(cmp) + ", VWMA: " + str(vwma) + ", RSI: " + str(rsi) + ", at : " + str(datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")))

        if openingRSI > 60 and rsi < 60:
            lowestRSI = True

        if (rsi > 60 and cmp > vwma and openingRSI < 60) or (lowestRSI and rsi > 60 and cmp > vwma):
            print("Buy " + stock + " at " + str(cmp) + " at : " + str(datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")))
            # Find Sector is Strong or Not.
            boughtPrice = cmp
            lowestRSI = False
            break

        if cmp >= boughtPrice + 30:
            print("Sell - " + stock + " at " + str(cmp) + " at : " + str(datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")))

