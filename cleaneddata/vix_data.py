import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr

# Name of File : vix.npy
# Date Range : 19900102 - 20220923
# Dimensions : (8247, 6)
# Columns : Date, Open, High, Low, Close, Adj Close
# Null Values : None


yf.pdr_override()
# data = pdr.get_data_yahoo("^VIX")[["Open", "High", "Low", "Close", "Adj Close"]]
data = pdr.get_data_yahoo("^VIX")[["Adj Close"]]
data.reset_index(inplace=True)

data["Date"] = data["Date"].dt.strftime("%Y%m%d")


np.save("vixclose.npy", data.to_numpy())

