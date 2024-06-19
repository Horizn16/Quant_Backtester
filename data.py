import yfinance as yf
import pandas as pd

def download_historical_data(symbol,start_date,end_date,timeframe="1d"):
    """
    Parameters:
    symbol: The ticker symbol of the stock (e.g., 'RELIANCE.NS').
    start_date: Start date for the data in 'YYYY-MM-DD' format.
    end_date: End date for the data in 'YYYY-MM-DD' format.
    timeframe: The frequency of the data ('1d', '1wk', '1mo'), default is '1d'.
    Return: A pandas DataFrame containing the fetched data
    """

    data=yf.download(symbol, start=start_date, end=end_date,interval=timeframe)
    return data