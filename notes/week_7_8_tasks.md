# Plan for the next 2 weeks

## 1. Final data preparation for the project

- Concatenate the arrays of npy data by the dates to give new npy array of columns (date, SP5000, WTI, real estate,
  <br> fed fund rate, usdx, vix)
  ( only include the pct_change ie monthly returns for SP500, WTI, real estate, the others use actual values ) - Main concern - Dates of each npy array do not match do to some unknown reason - Solution: - We will reference all the data to SP500
  <br> Drop the rows that dont have dates in SP500.
  <br> Drop rows in SP500 that have dates that other data do not have
  <br> Essentially create a bijection of data

## 2. Read up on AT-LSTM models

- LSTM is popularised in ~2010s for its translation ability
- It is a good ML model for time series that pars other time series models such as XGBoost (though it requires more data than XGB).
- Latest research into ML time series incorporates **Attention(AT)** with LSTM
  - Similar projects to ours
    - [Financial engineering paper by XJLU's](https://www.worldscientific.com/doi/epdf/10.1142/S2424786322500141)
    - We will be "improving" on where they left off by including indicators such as vix, bond rates, and dollar index to capture public sentiment and future outlook. We wont be following exactly what they did.
  - Attention is just a keras layer so no trouble implementing custom networks :)
- [What is LSTM?](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [Improving LSTM performance](https://medium.com/geekculture/10-hyperparameters-to-keep-an-eye-on-for-your-lstm-model-and-other-tips-f0ff5b63fcd4)
- [What is Attention?](https://www.analyticsvidhya.com/blog/2019/11/comprehensive-guide-attention-mechanism-deep-learning/)

## Briefing

The model that we will be **first** using will be LSTM classification model that takes in inputs of look-back of ~~size = 5~~ size = 40 (2 months) to predict the movements of the next 1,2,3,4,5,6 months ahead. (Note 5 is really not ideal but we need to see if we can get things working before putting in too much time waiting for model to train.)

Classification
0 - <= sigma 0.5 movements; < 70th percentile of monthly changes
1 - > sigma 0.5 movements; >70th percentile of monthly changes

we can do the classification through variance mean normalisation to N(0,1). Then we classify > 0.5 for 1 class for each month

the prediction will output a vector of size 6
<br> (0,0,1,0,0,1) This means that the 3rd and the 6th months will have a >0.5 sigma monthly returns while the rest do not
