# -*- coding: utf-8 -*-
"""
Python	3.8.5, quandl	3.5.3 ,numpy	1.19.4, pandas	1.1.4
matplotlib	3.3.2, pystan	2.19.1, pytrends	4.7.3
plotly	4.12.0 ,yfinance	0.1.55
"""
import pandas as pd
import yfinance as yf
from StockerV2_Maple import Stocker

##StockNum.區域
stockNo = "2330.TW"
##起始日期
start_date = '2020-01-01'
df = yf.download(stockNo, start=start_date)
df = df.reset_index()

##使用 Stocker 預測股價
stock = Stocker(stockNo, df)
## 畫出歷史股價
stock.plot_stock()
## 使用Prophet 預言家模型預測股價
model, model_data = stock.create_prophet_model(days=10)

#資料驗證
stock.evaluate_prediction()
 
#調整參數
stock.changepoint_prior_analysis(changepoint_priors=[0.001, 0.05, 0.1, 0.2])
stock.changepoint_prior_scale = 0.5
stock.evaluate_prediction()

