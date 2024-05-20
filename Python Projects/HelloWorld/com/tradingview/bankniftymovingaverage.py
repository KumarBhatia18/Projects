import json

from tradingview_ta import TA_Handler, Interval, Exchange, Analysis
from yearlyhighlow import get52week
# from weekly import getweeklydata
from yahoofinancials import YahooFinancials

# stockList = {"MARUTI": 'MARUTI.NS', 'LT': 'LT.NS'}
intervalList = [Interval.INTERVAL_15_MINUTES]


def getstockdata(tradingviewsymbol, yahoosymbol):
    # print('Stock Name is ' + tradingviewsymbol)
    root = {}
    root['name'] = tradingviewsymbol
    #
    # # Map 52 Week High and Low for a Stock - Starts
    # json_data = get52week(yahoosymbol)
    # for key, value in json_data.items():
    #     root[key] = value
    # # Map 52 Week High and Low for a Stock - Ends
    #
    # # Map Support for a Stock to Indicate a Buy Signal - Starts
    # json_data = getweeklydata(yahoosymbol)
    # for key, value in json_data.items():
    #     root[key] = value
    # # Map Support for a Stock to Indicate a Buy Signal - Ends

    for interval in intervalList:
        taHandler = TA_Handler(
            symbol=tradingviewsymbol,
            screener="india",
            exchange="NSE",
            interval=interval
        )
        indicators = taHandler.get_analysis().indicators
        data = {}
        data['high'] = str(indicators.pop('high'))
        data['low'] = str(indicators.pop('low'))
        data['rsi'] = str(round(indicators.pop('RSI'), 2))
        data['vwma'] = str(round(indicators.pop('VWMA'), 2))

        yf = YahooFinancials(yahoosymbol)
        data['cmp'] = str(round(yf.get_current_price(), 2))

        # movingAverage = taHandler.get_analysis().moving_averages.pop('COMPUTE')
        #
        # dataMovingAverageEma10 = {}
        # dataMovingAverageEma10['price'] = str(round(indicators.pop('EMA10'), 2))
        # dataMovingAverageEma10['reco'] = str(movingAverage.pop('EMA10'))
        # data['ema10'] = dataMovingAverageEma10
        #
        # dataMovingAverageEma20 = {}
        # dataMovingAverageEma20['price'] = str(round(indicators.pop('EMA20'), 2))
        # dataMovingAverageEma20['reco'] = str(movingAverage.pop('EMA20'))
        # data['ema20'] = dataMovingAverageEma20
        #
        # dataMovingAverageEma30 = {}
        # dataMovingAverageEma30['price'] = str(round(indicators.pop('EMA30'), 2))
        # dataMovingAverageEma30['reco'] = str(movingAverage.pop('EMA30'))
        # data['ema30'] = dataMovingAverageEma30
        #
        # dataMovingAverageEma50 = {}
        # dataMovingAverageEma50['price'] = str(round(indicators.pop('EMA50'), 2))
        # dataMovingAverageEma50['reco'] = str(movingAverage.pop('EMA50'))
        # data['ema50'] = dataMovingAverageEma50
        #
        # dataMovingAverageEma100 = {}
        # dataMovingAverageEma100['price'] = str(round(indicators.pop('EMA100'), 2))
        # dataMovingAverageEma100['reco'] = str(movingAverage.pop('EMA100'))
        # data['ema100'] = dataMovingAverageEma100
        root[interval] = data

    # json_data = json.dumps(root)
    return root