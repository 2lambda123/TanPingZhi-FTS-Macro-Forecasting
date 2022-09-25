import pandas as pd
import numpy as np
import yfinance as yf

# data obtained from https://www.macrotrends.net/2015/fed-funds-rate-historical-chart
ffr = pd.read_csv("fed-funds-rate-historical-chart.csv")
np.save('fed_funds_rate.npy', ffr.to_numpy())

fyty = yf.download("^FVX")
fyty.reset_index(inplace=True)
fyty = fyty[["Date", "Close"]]
fyty["Date"] = fyty["Date"].dt.strftime("%Y-%m-%d")
np.save('five_year_treasury_yield_rate.npy', fyty.to_numpy())