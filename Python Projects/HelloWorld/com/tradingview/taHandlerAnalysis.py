import json

from tradingview_ta import TA_Handler, Interval, Exchange, Analysis

intervalList = [Interval.INTERVAL_1_DAY, Interval.INTERVAL_1_WEEK, Interval.INTERVAL_1_MONTH, Interval.INTERVAL_15_MINUTES]

for interval in intervalList:
    print(interval)
    taHandler = TA_Handler(
        symbol='MARUTI',
        screener="india",
        exchange="NSE",
        interval=interval
    )
    print(taHandler)
    print(taHandler.get_analysis())
    indicators = taHandler.get_analysis().indicators
    print(indicators)
    movingAverage = taHandler.get_analysis().moving_averages
    print(movingAverage)
