import pandas as pd 
import matplotlib.pyplot as plt 
import yfinance as yf 
import datetime

# start_date : YYYY-MM-DD
# end_date : YYYY-MM-DD


def download_historical_data(symbol , start_date , end_date , timeframe = "1d"):

    get_data = yf.Ticker(symbol)
    pd.set_option('display.max_columns', None)  # None means unlimited columns will be displayed

    df = get_data.history(start=start_date,end=end_date, interval = timeframe)
    return df 