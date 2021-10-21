from pycoingecko import CoinGeckoAPI
import requests
import json
from datetime import datetime

cg = CoinGeckoAPI()

def get_coin_status(id):
    api_result = cg.get_price(ids=id, vs_currencies='usd', include_24hr_vol='true',include_24hr_change='true', include_last_updated_at='true')
    response   = dict()
    response['Price']  = api_result['gamestarter']['usd']
    response['Change'] = round(api_result['gamestarter']['usd_24h_change'],2)
    response['Vol']    = round(api_result['gamestarter']['usd_24h_vol'],1)
    return response

#print(get_coin_status('gamestarter'))