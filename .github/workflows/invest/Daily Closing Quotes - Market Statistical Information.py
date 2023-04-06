import requests as req    #股票爬蟲,可以設定時間每天幫你把股票資訊傳給你
import  pandas as pd
import time
import schedule


def get_stock_dailytrade():
    res=req.get("https://openapi.twse.com.tw/v1//exchangeReport/MI_INDEX")
    df=pd.DataFrame(res.json())
    localtime = time.localtime()
    now= time.strftime("%Y-%m-%d %I-%M-%S", localtime)
    df.to_csv(f"{now}.csv",encoding="utf_8_sig",index=False)
    print(f"{now}取得股票資訊")

schedule.every().day.at("18:00:00").do(get_stock_dailytrade)


while True:
    schedule.run_pending()
    time.sleep(1)






def get_stock_everytrade():
    res=req.get("https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL")
    df=pd.DataFrame(res.json())
    localtime = time.localtime()
    now= time.strftime("%Y-%m-%d %I-%M-%S", localtime)
    df.to_csv(f"{now}.csv",encoding="utf_8_sig",index=False)
    print(f"{now}取得股票資訊")

schedule.every().day.at("06:00:00").do(get_stock_everytrade)
while True:
    schedule.run_pending()
    time.sleep(1)
