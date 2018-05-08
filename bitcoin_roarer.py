import logging
import requests
import time
from pygame import mixer


ENDPOINT = "https://www.binance.com"
mixer.init()
mixer.music.load('./you_suffer.mp3')

def request(method, path, params=None):
    resp = requests.request(method, ENDPOINT + path, params=params)
    data = resp.json()
    if "msg" in data:
        logging.error(data['msg'])
    return data

def prices():
    """Get latest prices for all symbols."""
    data = request("GET", "/api/v1/ticker/allPrices")
    return {d["symbol"]: d["price"] for d in data}



if __name__ == '__main__':
    while True:
        btcusdt = float(prices()['BTCUSDT'])
        print('time: {0}, BTCUSDT: {1}'.format(time.time(), btcusdt))
        if btcusdt < 9000 or btcusdt > 10000:
            mixer.music.play()
        time.sleep(60)