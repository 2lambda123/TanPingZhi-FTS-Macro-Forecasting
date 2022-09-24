# FTS-Macro-Forecasting
NUS Fintech Society Project AY22/23S1 

### Team Members (Add your name here!):
Tan Ping Zhi

# Motivations
Garbage stocks go up in bull market

Strong stocks go down in bear market

Idea: Be a macro trader instead

## Goal of the project:
Use ML to trade like a macro pro investor like [Ray Dalio](https://en.wikipedia.org/wiki/Ray_Dalio)

Terminologies
Monthly returns: percentage change from T - 20 market days to T for every trading day (rolling change). 

# To do
1.  Data collection (only vix and real estate prices are provided, the other data can be sourced from  yfinance (python library), [FRED](https://fred.stlouisfed.org/), [WRDS](https://wrds-www.wharton.upenn.edu/login/?next=/pages/get-data/)(lmk if you want access)
- [ ] SP500 (get data, get list of monthly returns, find the value of -1, -0.5, 0.5, 1 sigma monthly returns that will be used for classification later on)
- [ ] VIX and [WTI](https://fred.stlouisfed.org/series/DCOILWTICO) (get data, WTI monthly returns)
- [ ] [Real estate prices](https://fred.stlouisfed.org/series/WILLRESIND) (get data, monthly returns)
- [ ] [Rates](https://wrds-www.wharton.upenn.edu/pages/get-data/federal-reserve-bank-reports/interest-rates/data/)
2. Train LSTM
3. See if there's alpha
4. Fun with regression instead of ML if there is time
### Purpose
- We will use monthly return data instead of price as price does not follow any distribution
- Interest rates seems to have an upper bound so no need for data conversion.
