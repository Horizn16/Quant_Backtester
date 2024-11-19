import pandas as pd
import numpy as np
from data_fetch import download_historical_data

def calculate_macd(df, short_window=12, long_window=26, signal_window=9):
    df['EMA_12'] = df['Close'].ewm(span=short_window, adjust=False).mean()
    df['EMA_26'] = df['Close'].ewm(span=long_window, adjust=False).mean()
    df['MACD'] = df['EMA_12'] - df['EMA_26']
    df['MACD_Signal'] = df['MACD'].ewm(span=signal_window, adjust=False).mean()
    return df

def calculate_rsi(df, window=14):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

def strategy_build(symbol, start_date, end_date):
    # Fetch historical data
    df = pd.DataFrame(download_historical_data(symbol, start_date, end_date))
    
    # Ensure 'Date' is a column if it is an index
    if 'Date' not in df.columns:
        df.reset_index(inplace=True)
    
    # Calculate the 9-day and 20-day Simple Moving Averages (SMA)
    df['SMA_9'] = df['Close'].rolling(window=9).mean()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    # df['sma_50'] = df['Close'].rolling(window=50).mean()
    # df['sma_200'] = df['Close'].rolling(window=200).mean()
    # Calculate MACD and its signal line
    df = calculate_macd(df)
    
    # Calculate RSI
    df = calculate_rsi(df)
    
    # Initialize the 'signal' column with 0
    df['signal'] = 0
    
    # Create conditions for buy and sell signals
    buy_signal = (df['SMA_9'] > df['SMA_20']) & (df['MACD'] > df['MACD_Signal']) & (df['RSI'] < 30)
    sell_signal = (df['SMA_9'] < df['SMA_20']) & (df['MACD'] < df['MACD_Signal']) & (df['RSI'] > 70)
    
    # Debug: Print some rows to inspect the values
    # print(df[['Date', 'SMA_9', 'SMA_20', 'MACD', 'MACD_Signal', 'RSI']].tail(20))
    
    # Apply buy signals (1)
    df.loc[buy_signal, 'signal'] = 1
    
    # Apply sell signals (-1)
    df.loc[sell_signal, 'signal'] = -1
    
    # Forward fill the signals to account for hold (0)
    df['signal'] = df['signal'].replace(0, np.nan).ffill().fillna(0)
    
    # Remove rows with NaN values in SMA columns
    df.dropna(subset=['SMA_9', 'SMA_20'], inplace=True)
    
    # Debug: Print signal column to verify the signals
    # print(df[['Date', 'signal']].tail(20))
    
    return df

# Example usage (you need to implement the `download_historical_data` function):
# df = strategy_build('AAPL', '2023-01-01', '2023-12-31')



# start_date = "2016-01-01"
# end_date = "2024-07-05"
# symbol = "GANESHHOUC.NS"


# df_signals = strategy_build(symbol , start_date , end_date)
# print(df_signals[['Date', 'Close', 'SMA_9','SMA_20','signal']].tail(20))