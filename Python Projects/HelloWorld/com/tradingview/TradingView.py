from tradingview_ta import TA_Handler, Interval, Exchange
from TradingViewMovingAverages import *

stockList = {"MARUTI": 'MARUTI.NS'}
for stock in stockList:
    getstockdata(stock, stockList[stock])
