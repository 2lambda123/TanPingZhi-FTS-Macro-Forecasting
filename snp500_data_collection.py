from numpy import save
import yfinance as yf

spy = yf.Ticker("^GSPC")

hist = spy.history(period="max")[["Close"]]
hist.reset_index(inplace=True)
hist["Previous Month Close"] = hist["Close"].shift(20)
hist["Percentage"] = (hist["Close"] - hist["Previous Month Close"]) / hist["Previous Month Close"]

hist["Date"] = hist["Date"].dt.strftime("%Y%m%d")

del hist["Previous Month Close"]

print(hist)

save('cleaneddata/snp500.npy', hist.to_numpy())
