import twstock
import time
import requests

import gspread
from oauth2client.service_account import ServiceAccountCredentials

auth_json_path = 'PythonUpload.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials) 

#開啟 Google Sheet 資料表
spreadsheet_key = '1OzXkaZua1zAUKcIUmAuUVu9qEx-sweyE1gI1E-Pu6wQ' 
sheet = gss_client.open_by_key(spreadsheet_key).sheet1

for r in  sheet.get_all_values():
    if r[1] != '股票代號':
        print(r[1]+'目標價:'+r[2])
        counterLine = 0  #儲存發送次數
        counterError = 0  #儲存錯誤次數
        print('程式開始執行！')
        while True:
            realdata = twstock.realtime.get(r[1])  #即時資料
            if realdata['success']:
                realprice = realdata['realtime']['latest_trade_price']  #目前股價
                if float(realprice) >= float(r[2]):
                    print(r[0]+'目前股價：' + realprice)
                    counterLine = counterLine + 1
                    url_ifttt ='https://maker.ifttt.com/trigger/最新股價/with/key/dHTXnHZ-g1MoDxhMaS7_61?value1=' + realprice+'&value2='+r[0]+'&value3='+r[1]  #發送LINE訊息網址
                    res1 = requests.get(url_ifttt)  #發送請求
                    print('第' + str(counterLine) + '次發送LINE回傳訊息：' + res1.text)
                if counterLine >= 3:  #最多發送3次就結束程式
                    print('程式結束！')
                    break  
                else:
                    break
            else:
                print('twstock 讀取錯誤，錯誤原因：' + realdata['rtmessage'])
                counterError = counterError + 1
                if counterError >= 3:  #最多錯誤3次
                    print('程式結束！')
                    break
                time.sleep(300)  #每5分鐘讀一次     
    