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


    # Ensure the data is sorted by date
    df = df.sort_values(by='Date')

    # Calculate daily returns
    df['Daily_Return'] = df['Close'].pct_change() * 100

    # Calculate cumulative returns
    df['Cumulative_Return'] = (df['Close'] / df['Close'].iloc[0] - 1) * 100


    initial_price = df['Close'].iloc[0]
    final_price = df['Close'].iloc[-1]
    df['cumulative_return'] = (final_price / initial_price - 1) * 100

    

    # Drop the first row since it will have NaN for daily return
    df = df.dropna()
    df.reset_index(inplace=True)
    return df 


# start_date = "2024-07-01"
# end_date = "2024-07-05"
# symbol = "GAIL.BO"


# dataset = pd.DataFrame(download_historical_data(symbol , start_date, end_date , ))

# print(dataset[['Date','Close']].tail(5))



# THIS IS DOWNLOAD HISTORICAL DATA FUNCTION 