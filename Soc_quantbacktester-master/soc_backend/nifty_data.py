import pandas as pd 
import matplotlib.pyplot as plt 
import yfinance as yf 
import datetime

def nifty_data(start_date , end_date ,symbol='^NSEI' , timeframe = "1d"):

    get_data = yf.Ticker(symbol)
    pd.set_option('display.max_columns', None)  # None means unlimited columns will be displayed

    df = get_data.history(start=start_date,end=end_date, interval = timeframe)

    initial_price = df['Close'].iloc[0]
    final_price = df['Close'].iloc[-1]
    df['cumulative_return'] = (final_price / initial_price - 1) * 100
    # Ensure the data is sorted by date
    df = df.sort_values(by='Date')
    df.reset_index(inplace=True)
    return df 

# start_date = "2024-06-01"
# end_date = "2024-07-02"

# dataset = pd.DataFrame(nifty_data(start_date, end_date))

# print(dataset.head())


