import pandas as pd 
import matplotlib.pyplot as plt 
from data_fetch import download_historical_data # called from deat_fetch
from performance import plot_data  # Importing plot_data function from performance module


start_date = "2024-06-01"
end_date = "2024-06-19"
symbol = "HDFCLIFE.NS"

# Download historical data
# df = download_historical_data(symbol, start_date, end_date)

y_axis = "Close"  
x_axis = "Date"   

# Call plot_data function to plot and display the data

plot_data(symbol, x_axis, y_axis, start_date, end_date)  # here by default we take timeframe = 1d

# for getting many at a time 


