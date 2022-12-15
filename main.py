import requests
import json
from telegram import Bot
from tabulate import tabulate
import time
from urllib3 import HTTPSConnectionPool


 #Send Message to Telegram
def sendMessage(data):
    tg_bot = Bot('TOKEN')
    channel = 'CHANNEL'
    try:
        print('--->Sending message to telegram')
        tg_bot.sendMessage(
            channel,
            data,
            parse_mode="MARKDOWN",
        )
        return True
    except KeyError:
        print('--->Key error - sending error to telegram')
        tg_bot.sendMessage(
            channel,
            data,
            parse_mode="MARKDOWN",
        )
    except Exception as e:
        print("[X] Telegram Error:\n>", e)
    return False


#handles the python code this is Automatically call by Pip dream Management system      
def handler(pd: "pipedream"):
  headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }


  # jsonPayload = pd.steps["trigger"]["event"]["body"]["text"]
  # requests.post(f'https://api.telegram.org/bot5971347619:AAEFW--U4dvA2TE4UPAYaigx3WECFCfsCN8/sendMessage?chat_id=-1001567924918&text={jsonPayload}')
  # repl_url = "https://AyoCryptAlgo.ayobamiakinlolu.repl.co/webhook?jsonRequest=true"
  # requests.post(repl_url, data=json.dumps(jsonPayload, sort_keys= True, default=str), headers=headers)
   
  # address = pd.steps["trigger"]["event"]["headers"]["from"]["value"][0]["address"]
  address =pd.steps["trigger"]["event"]["headers"]["from"]["value"][0]["address"]

  # repl_url = "https://AyoCryptAlgo.ayobamiakinlolu.repl.co/webhook?jsonRequest=true"
  # requests.post(repl_url, data=json.dumps(pay, sort_keys= True, default=str), headers=headers)
  TV = ["noreply@tradingview.com"]
  if address in TV:
    # jsonPayload=pd.steps["trigger"]["event"]["body"]["html"]
    # jsonPayload = BeautifulSoup(jsonPayload, "html.parser")
    # jsonPayload = list(jsonPayload.find_all("p"))[1].text
    
    jsonPayload = pd.steps["trigger"]["event"]["body"]["text"]
    jsonPayload =json.loads(jsonPayload)
    entry =float(jsonPayload["Entry"])  
    if jsonPayload["Direction"] == "SHORT":
      hash="#"
      payload = f"""
          
Excahnge: {jsonPayload['Exchanges']}

🦅🦅 #{jsonPayload["ticker"]} 🦅🦅
Direction: SHORT 

✅Entry Orders:
1) {round(float(entry),9)}
2) {round(float((entry/100)*0.5+entry),9)}

✅Take-Profit Orders:
1) {round(float(entry-(entry/100)*0.5),9)}
2) {round(float(entry-(entry/100)*1),9)}
3) {round(float(entry-(entry/100)*2),9)}
4) {round(float(entry-(entry/100)*3),9)}
5) {round(float(entry-(entry/100)*4),9)}
6) {round(float(entry-(entry/100)*5),9)}
7) 🚀🚀🚀🚀🚀🚀🚀🚀🚀

🚨Stop Orders: 
1) {round(float((entry/100)*13 + entry),9)} 
‼️Use Oppossite Signals as stop-loss‼️

Trailing Configuration:
Stop: Breakeven -
  Trigger: Target (1)
"""
      
      
      opens = round(float(jsonPayload["open"]), 7)
      high = round(float(jsonPayload["high"]), 7)
      low = round(float(jsonPayload["low"]), 7)
      close = round(float(jsonPayload["close"]), 7)
      time_now = jsonPayload["time"][11:19]
      date = jsonPayload["time"][0:10]
      data = {
      "Market Vol": jsonPayload["volume"],
      "Close Price": close,
      "Open Price": opens,
      "High Price": high,
      "Low Price": low,
      "TimeFrame": "5 Min",
      "Time[GMT]": time_now,
      "Date": date
      }

      # data = pd.DataFrame(data, index=[1]).transpose()
      headers_ = ["Desc.", "Details"]
      rows = [[key, values] for key,values in data.items()]
      Table = "`" +tabulate(rows, headers_, tablefmt="simpl_grid")+"`" 



      message = f"""Please Wait...🏄🏻\n\nI am Accessing tradingview.com To ScreenShot 👉#{jsonPayload["ticker"]}👈\n\nBeside you could check the table below for Market Analysis\n\n{Table}
            """

      
      
      sendMessage(payload)
      # time.sleep(0.1)
      sendMessage(message)
      # r= requests.post(f'https://api.telegram.org/bot5971347619:AAEFW--U4dvA2TE4UPAYaigx3WECFCfsCN8/sendMessage?chat_id=-1001567924918&text={payload}&parse_mode= MARKDOWN')
      # TRIGGER RPLIT EMAIL>>> TO LOAD CHART

      try:
        repl_url = "https://AyoCryptAlgo.ayobamiakinlolu.repl.co/webhook?jsonRequest=true"
        r = requests.post(repl_url, data=json.dumps(jsonPayload, sort_keys= True, default=str), headers=headers, timeout=10)
       
        # for i in range(6):
        #     time.sleep(1)
        
        # if i== 5 and r.status_code != 200:
        #     sendMessage(errorMessage)
        # else:
        #     sendMessage(f"status{r.status_code}")
      except Exception as e:
        errorMessage = f""" Please I will be Unable To send you  the Chart at this time\nIn other not to waste your time\nPlease visit https://www.tradingview.com/chart/RR480ozx/?symbol={jsonPayload["ticker"]}
        reason REQUEST TIMEOUT
        """
        sendMessage(errorMessage)
        
    else:

      payload = f"""
          
Excahnge: {jsonPayload['Exchanges']}

🦅🦅 #{jsonPayload["ticker"]} 🦅🦅
Direction: LONG 

✅Entry Orders:
1) {round(float(entry),9)}
2) {round(float(entry - (entry/100)*0.5), 9)}

✅Take-Profit Orders:
1) {round(float(entry+(entry/100)*1),9)}
2) {round(float(entry+(entry/100)*2),9)}
3) {round(float(entry+(entry/100)*3),9)}
4) {round(float(entry+(entry/100)*4),9)}
5) {round(float(entry+(entry/100)*5),9)}
6) {round(float(entry+(entry/100)*6),9)}
7)  🚀🚀🚀🚀🚀🚀🚀


👩‍🚒Stop Orders:
1) {round(float(entry - (entry/100)*13),9)}
‼️Use Oppossite Signals as stop-loss‼️

Trailing Configuration:
Stop: Breakeven -
  Trigger: Target (1)

"""  
      opens = round(float(jsonPayload["open"]), 7)
      high = round(float(jsonPayload["high"]), 7)
      low = round(float(jsonPayload["low"]), 7)
      close = round(float(jsonPayload["close"]), 7)
      time_now = jsonPayload["time"][11:19]
      date = jsonPayload["time"][0:10]
      data = {
      "Market Vol": jsonPayload["volume"],
      "Close Price": close,
      "Open Price": opens,
      "High Price": high,
      "Low Price": low,
      "TimeFrame": "5 Min",
      "Time[GMT]": time_now,
      "Date": date
      }

      headers_ = ["Desc.", "Details"]
      rows = [[key, values] for key,values in data.items()]
      Table = "`" +tabulate(rows, headers_, tablefmt="simpl_grid")+"`" 



      message = f"""Please Wait...🏄🏻\n\nI am Accessing tradingview.com To ScreenShot 👉#{jsonPayload["ticker"]}👈\n\nBeside you could check the table below for Market Analysis\n\n{Table}
            """

      sendMessage(payload)
      # time.sleep(0.1)
      sendMessage(message)
      # r= requests.post(f'https://api.telegram.org/bot5971347619:AAEFW--U4dvA2TE4UPAYaigx3WECFCfsCN8/sendMessage?chat_id=-1001567924918&text={payload}&parse_mode= MARKDOWN')
      # TRIGGER RPLIT EMAIL>>> TO LOAD CHART
    #   repl_url = "https://AyoCryptAlgo.ayobamiakinlolu.repl.co/webhook?jsonRequest=true"
    #   r= requests.post(repl_url, data=json.dumps(jsonPayload, sort_keys= True, default=str), headers=headers)
      try:
        repl_url = "https://AyoCryptAlgo.ayobamiakinlolu.repl.co/webhook?jsonRequest=true"
        r = requests.post(repl_url, data=json.dumps(jsonPayload, sort_keys= True, default=str), headers=headers, timeout=10)
        errorMessage = f""" Please I will be Unable To send the Chart at time\n In other not to waste your time
        please visit https://www.tradingview.com/chart/RR480ozx/?symbol={jsonPayload["ticker"]}
        R =={r}
        """
        # for i in range(6):
        #     time.sleep(1)
        
        # if i== 5 and r.status_code != 200:
        #     sendMessage(errorMessage)
        # else:
        #     sendMessage(f"status{r.status_code}")
        # if r.status_code ==200:
        #     sendMessage(f"status{r.status_code}")
        # else:
        #     sendMessage(errorMessage)
      except Exception as e:
        errorMessage = f""" Please I will be Unable To send you  the Chart at this time\nIn other not to waste your time\nPlease visit https://www.tradingview.com/chart/RR480ozx/?symbol={jsonPayload["ticker"]}
        reason REQUEST TIMEOUT
        """
        sendMessage(errorMessage)

        
         
