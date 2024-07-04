# [Python] 預測股票 用Stocker 預言家模型

###### tags: `Python` `ML` `MachineLearning` `Stock`

# System Version Setting
Anaconda3-2020.07-Windows-x86_64.exe

| package     | Version |
| ------------| ------- |
| Python      | 3.8.5   |
| quandl      | 3.5.3   |
| numpy       | 1.19.4  |
| pandas      | 1.1.4   |
| matplotlib  | 3.3.2   |
| pystan      | 2.19.1  |
|pytrends     | 4.7.3   |
| plotly      | 4.12.0  |
| yfinance    | 0.1.55  |




# Install Sth package

==需要依照順序安裝==

安裝Anaconda3 with Python 3.8 

python istall
```python=
pip install -U quandl numpy pandas matplotlib pystan pytrends plotly yfinance
```
conda install
```python=
conda install -c conda-forge fbprophet
```


# Code

```python=
import pandas as pd
import yfinance as yf
from StockerV2_Maple import Stocker

##鼓號.區域
stockNo = "2330.TW"
##起始日期
start_date = '2020-01-01'
df = yf.download(stockNo, start=start_date)
df = df.reset_index()

##使用 Stocker 預測股價
stock = Stocker(stockNo, df)
## 畫出歷史股價
#stock.plot_stock()
## 使用Prophet 預言家模型預測股價
# model, model_data = stock.create_prophet_model(days=10)



```

## 資料驗證 (接上)
想要看看我們的模型好不好，我們可以使用 stock.evaluate_prediction() 函式，
將最近一年的資料當成測試資料，
看看如果使用過去三年的資料來訓練我們的模型，
那在這一年的測試資料上表現如何。
看看下圖…乾那賽。紅線左邊是訓練資料，紅線右邊是模型預測出來的。
可以看出來完全偏離黑色的真實資料。
```python=
 stock.evaluate_prediction()

```
## 調整參數
可以試著調整參數讓模型預測有不同的表現，
調整不同的 changepoint_prior，讓模型以不同的強度去 fit 訓練資料，
可以看到 changepoint_prior 越高 (黃色) 會越貼近黑色的真實資料，
但也越容易產生過度擬合 (overfitting)，
changepoint_prior 越低 (藍色) 則較容易反應長期的趨勢，但也越容易產生欠擬合 (underfitting)。
```python=
 stock.changepoint_prior_analysis(changepoint_priors=[0.001, 0.05, 0.1, 0.2])
 stock.changepoint_prior_scale = 0.5
 stock.evaluate_prediction()
```

![](https://i.imgur.com/FPfQDxP.png)


training set、validation set、test set
詳細
https://towardsdatascience.com/stock-prediction-in-python-b66555171a2


# Problem
![](https://i.imgur.com/6B6rT5A.png)
AttributeError: 'DataFrame' object has no attribute 'ix'


//都會阿罵可以用
https://github.com/grandma-tutorial/Stocker/blob/master/stocker.py



# Paper

Forecasting at Scale
Sean J. Taylor
Facebook, Menlo Park, California, United States
https://peerj.com/preprints/3190.pdf

## 架構
![](https://d1dwq032kyr03c.cloudfront.net/upload/images/20181107/20111390lwYBwCpKAp.png)

Modeling：建立時間序列的模型。這邊使用股票來做模型。
Forecast Evaluation：模型評估。
Surface Problems：呈現問題。
Visually Inspect Forecasts：以視覺化的方式呈現預測結果。

## equation 方程式

y(t) = g(t)+s(t)+h(t)+et

g(t)趨勢函數
s(t)週期變化 ex(每週和每季)
et 非常規變化


f(t) = year(t) + season(t) + week(t) + trend(t)


# Reference

超簡單用Python預測股價

https://www.finlab.tw/%E8%B6%85%E7%B0%A1%E5%96%AE-Machine-Learning-%E9%A0%90%E6%B8%AC%E8%82%A1%E5%83%B9/
https://weikaiwei.com/python/stocker/
https://github.com/WillKoehrsen/Data-Analysis/tree/master/stocker

都會阿罵的sotcker.py可以用

https://github.com/grandma-tutorial/Stocker
https://github.com/grandma-tutorial/Stocker/blob/master/stocker.py

論文 模型 演算法
https://peerj.com/preprints/3190.pdf
