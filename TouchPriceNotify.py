# =============================================================================
# yfinance  0.1.63 requests 2.25.1 pandas 1.1.4
# =============================================================================

# =============================================================================
# 施工中
# =============================================================================

import requests
import yfinance as yf
import pandas as pd
from datetime import date, timedelta

def lineNotifyMessage(token, msg):

    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

#yyyy-MM-dd
StartDate = date.today()
EndDate = date.today()+timedelta(days=1)  

#Get Today's price
StockNumber = "2330"+".TW"
data = yf.download("2330.TW", start=StartDate, end=EndDate)
StockClosed=data.iloc[0,4]
print(StockClosed)

#Line Notify Message
token = ' Your Line Notify Token '
message = StockClosed
lineNotifyMessage(token, message)