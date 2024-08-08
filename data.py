import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


class DataHandler:
    def __init__(self,ticker, start_date, end_date):
        self.ticker=ticker
        self.start_date=start_date
        self.end_date=end_date
    
    def fetch_data(self):
        self.data=yf.download(self.ticker, start=self.start_date, end=self.end_date)
        return self.data
    
    
    def data_characteristics(self):
        summary = self.data.describe().T
        summary['median'] = self.data.median()
        summary['mode'] = self.data.mode().iloc[0]
        return summary
    
    def missing_value_handler(self):
        if self.data is None:
            self.data = self.fetch_data()
            
        self.data  = self.data.fillna(0)
        return self.data
    
    def performance_analysis(self):
        
        nifty_data = yf.download('^NSEI', start=self.start_date, end=self.end_date)
        
        log_returns=np.log(self.data['Adj Close']/self.data['Adj Close'].shift(1))
        cum_log_returns=log_returns.cumsum()
        
        nifty_log_returns=np.log(nifty_data['Adj Close']/nifty_data['Adj Close'].shift(1))
        cum_nif_returns=nifty_log_returns.cumsum()
        
        plt.figure(figsize=(12, 6))
        plt.plot(cum_log_returns, label=f'{self.ticker} Cumulative Returns')
        plt.plot(cum_nif_returns, label='Nifty Cumulative Returns')
        plt.title(f'Performance of {self.ticker} vs Nifty')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.legend()
        
        static_folder = os.path.join(os.path.dirname(__file__), 'static')
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)
        
        # Save plot to static folder
        file_name = f'{self.ticker}_performance_plot.png'
        file_path = f"static/{file_name}"
        plot_path = os.path.join(static_folder, file_name)
        plt.savefig(plot_path)
        plt.close() 
        
        return file_path