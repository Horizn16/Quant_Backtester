import matplotlib.pyplot as plt

def plot_data(data,title="Crypto price",xlabel="Date",ylabel="Closing Price"):
    plt.figure(figsize=(80,80))
    plt.plot(data.index,data["Close"],label="Closing price vs Date")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.legend()
    plt.grid("True")
    plt.show()