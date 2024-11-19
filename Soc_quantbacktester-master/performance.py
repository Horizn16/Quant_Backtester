import matplotlib.pyplot as plt 
from data_fetch import download_historical_data

def plot_data(symbol, x_axis, y_axis, start_date, end_date, timeframe="1d"):
    # Download historical data
    df = download_historical_data(symbol, start_date, end_date, timeframe)
    
    # Reset index to make 'Date' a column
    df.reset_index(inplace=True)
    
    X = df[x_axis]
    Y = df[y_axis]
    
    plt.plot(X, Y)
    plt.title(f'{y_axis} vs {x_axis} for {symbol}')
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.grid(True)
    return plt.show()



# start_date = "2024-06-01"
# end_date = "2024-06-19"
# symbol = "RELIANCE.NS"
# x_axis = "Date" 
# y_axis = "Open"
# done for 1wk
# plot_data(symbol, x_axis, y_axis, start_date, end_date,"1d")
