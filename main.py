import matplotlib.pyplot as plt
from datetime import datetime
from performance import *
from data import *

symbol="RELIANCE.NS"
start_date="2024-06-01"
end_date=datetime.today().strftime("%Y-%m-%d")
timeframe="1d"

# print(end_date)
data=download_historical_data(symbol,start_date,end_date,timeframe)
# print(data)

plot_data(data,title=f"Crypto price of symbol: {symbol}",xlabel="Date",ylabel="Closing Price")

# plt.figure(figsize=(80,80))
# plt.plot(data.index,data["Close"],label="Closing price vs Date")
# plt.xlabel("Date")
# plt.ylabel("Closing Price")
# plt.legend()
# plt.grid("True")
# plt.show()