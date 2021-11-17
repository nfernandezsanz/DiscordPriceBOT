from   pycoingecko import CoinGeckoAPI
import requests
import json


cg   = CoinGeckoAPI()
last = dict()

def get_coin_status(id):
    global last
    try:
        api_result = cg.get_price(ids=id, vs_currencies='usd', include_24hr_vol='true',include_24hr_change='true', include_last_updated_at='true')
        response   = dict()
        response['Price']  = round(api_result[id]['usd'],3)
        response['Change'] = round(api_result[id]['usd_24h_change'],2)
        response['Vol']    = round(api_result[id]['usd_24h_vol'],1)
        last = response
        return response
    except:
        print("Error Coingecko!")
        return last