import numpy as np
import pandas as pd

def strategy_build(df):
    df['9day Sma'] = df['Close'].rolling(window=9, min_periods=1).mean()
    df['20day Sma'] = df['Close'].rolling(window=20, min_periods=1).mean()
    
    # Generate signals
    df['Signal'] = 0
    df['Signal'] = np.where((df['9day Sma'] > df['20day Sma']) & (df['9day Sma'].shift(1) <= df['20day Sma'].shift(1)), 1, df['Signal'])
    df['Signal'] = np.where((df['9day Sma'] < df['20day Sma']) & (df['9day Sma'].shift(1) >= df['20day Sma'].shift(1)), -1, df['Signal'])
    

    return df

class Trading_Execution:
    def __init__(self, df, ticker_name, start_date, end_date):
        self.df = df
        self.start_date = start_date
        self.end_date  = end_date
        self.ticker = ticker_name
        return
        
    def run(self):  # takes in cleaned data frame with SMA signal
        
        position = 0
        trade_open_price = 0
        self.df['returns'] = 0.0
        self.start_date = pd.Timestamp(self.start_date)
        self.end_date = pd.Timestamp(self.end_date)
        
        for i in range(len(self.df)):
            if self.df.index[i] >= self.start_date and self.df.index[i] <= self.end_date:
                if self.df['Signal'].iloc[i] == 1:
                    if position == 0:
                        position = 1
                        trade_open_price = self.df['Close'].iloc[i]
                elif self.df['Signal'].iloc[i] == -1:
                    if position == 1:
                        position = 0
                        trade_close_price = self.df['Close'].iloc[i]
                        self.df.loc[self.df.index[i], 'returns'] = (trade_close_price - trade_open_price) / trade_open_price
                        trade_open_price = 0

                if position == 1 and self.df['Close'].iloc[i] <= trade_open_price * 0.95:
                    position = 0
                    trade_close_price = self.df['Close'].iloc[i]
                    self.df.loc[self.df.index[i], 'returns'] = (trade_close_price - trade_open_price) / trade_open_price
                    trade_open_price = 0
                    
        
        returns = self.df.loc[self.df['returns']!=0.0,'returns'].copy()
        print(returns)
        
        return returns




