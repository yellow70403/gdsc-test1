# 先導入後面會用到的套件
import requests
import time

# 要爬的股票
stock = ["1101", "2330", "1102"]

# 模擬一般瀏覽器
headers = {
    "User-Agent": "Mozilla/5.0"
}

for stockid in stock:

    # Yahoo Finance API
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{stockid}.TW"

    # 發送請求
    r = requests.get(
        url,
        params={
            "range": "1d",
            "interval": "1d"
        },
        headers=headers,
        timeout=20
    )

    # 如果請求失敗就直接報錯
    r.raise_for_status()

    # 取得 JSON
    data = r.json()

    # 取得股票資訊
    result = data["chart"]["result"][0]

    # 取得目前價格
    price = result["meta"]["regularMarketPrice"]

    print(f"股票 {stockid} 股價為 {price}")

    # 回報的訊息
    message = f"股票 {stockid} 即時股價為 {price}"

    # Telegram Bot
    token = "輸入你的 bot token"
    chat_id = "輸入你的 telegram id"

    # 傳送 Telegram 訊息
    telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"

    requests.get(
        telegram_url,
        params={
            "chat_id": chat_id,
            "text": message
        },
        timeout=20
    )

    # 每次停 3 秒
    time.sleep(3)
