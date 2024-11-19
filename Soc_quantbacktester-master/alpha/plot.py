import matplotlib.pyplot as plt
from ticker_fetch import get_nse_tickers
from data_fetcher import download_historical_data

# PLOTS in Same plot 

def plot_data(symbols, x_axis, y_axis, start_date, end_date, timeframe="1d"):
    plt.figure(figsize=(10, 6))  # Adjust figure size if needed
    
    for symbol in symbols:
        # Download historical data for current symbol
        df = download_historical_data(symbol, start_date, end_date, timeframe)
        
        # Plot data
        df.reset_index(inplace=True)
        plt.plot(df[x_axis], df[y_axis], label=symbol)
    
    # Customize plot
    plt.title(f'{y_axis} vs {x_axis} for Multiple Symbols')
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Example usage
start_date = "2024-01-01"
end_date = "2024-06-19"
x_axis = "Date"  # Assuming 'Date' is a column after resetting index
y_axis = "Close"  # Assuming 'Close' is the column name for price data

symbols = get_nse_tickers()


plot_data(symbols, x_axis, y_axis, start_date, end_date)


# unique plot for all 

def plot_each(symbol , x_axis , y_axis , start_data , end_date , timeframe ="1d"):

    df.reset_index(inplace=True)
    
    X = df[x_axis]
    Y = df[y_axis]

    plt.plot(X, Y)
    plt.title(f'{y_axis} vs {x_axis} for {symbol}')
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.grid(True)
    return plt.show()

symbols = get_nse_tickers
start_date = "2024-06-01"
end_date = "2024-06-19"
x_axis = "Date" 
y_axis = "Open"

for symbol in symbols:
    plot_each(symbol , start_date, end_date , x_axis , y_axis)






