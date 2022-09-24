from numpy import save
import yfinance as yf

spy = yf.Ticker("^GSPC")

hist = spy.history(period="max")[["Close"]]
hist.reset_index(inplace=True)
hist["Previous Month Close"] = hist["Close"].shift(20)
hist["Percentage"] = (hist["Close"] - hist["Previous Month Close"]) / hist["Previous Month Close"]

hist["SD"] = hist["Percentage"].rolling(20).std()
hist["SD -1"] = hist["Percentage"] - hist["SD"]
hist["SD -0.5"] = hist["Percentage"] - 1/2 * hist["SD"]
hist["SD 0.5"] = hist["Percentage"] + 1/2 * hist["SD"]
hist["SD 1"] = hist["Percentage"] + hist["SD"]

hist["Date"] = hist["Date"].dt.strftime("%Y%m%d")

del hist["Previous Month Close"]
del hist["SD"]

print(hist)

save('cleaneddata/data.npy', hist.to_numpy())
