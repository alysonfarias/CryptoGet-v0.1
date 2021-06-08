import requests
import schedule
import time
from datetime import datetime

# Step 1: Get your API on https://coinmarketcap.com/api/

# free plan give [333 per days] [10.000 per month] requests
# API call rate limit: 30 requests a minute
# You could see the api documentation on https://coinmarketcap.com/api/documentation/v1/

# insert your apykey from CoinMarketCap [step 1]
apyKey = '0b6af46b-a6cc-4d71-808f-3aa94eeb05cf'
myBTCBalance = 1  # insert your BTC value here

headers = {
    'X-CMC_PRO_API_KEY': apyKey,
    'Accepts': 'application/json'
}

parameters = {
    'start': '1',
    # this could be a future issue, cause this get limit paremet only get top 5(actual variable but could be until 5000) coins right now(where the btc is the first one 19/05/2021), however possibily future code upgrade, like additioniting more coin
    'limit': '5',
    'convert': 'USD'
}

# function to transform a tuple in string
def convert_Tuple(tup):
    str = ''.join(tup)
    return str


def insert_Value():
# API url from CoinMarketCap
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# requesting info and transforming in .json
    json = requests.get(url, params=parameters, headers=headers).json()

    coins = json['data']
    arquivo = open("coinHistoric.txt", "a")

    for coin in coins:
        if coin['symbol'] == 'BTC':
        # the actual value from btc multiplied from your actual balance value
            value_Format = "%.2f" % (
            coin['quote']['USD']['price'] * myBTCBalance)
        # symbol coin
            symbol = coin['symbol']
        # get the hours and date
            actual_date = datetime.now()
            actual_date_and_hour = actual_date.strftime('%d/%m/%Y %H:%M')
            tuple = '[ ', actual_date_and_hour, " : ", symbol, ' value = $', value_Format, ' USD', ' ]'
        # tuple to string
            finalString = convert_Tuple(tuple)
        # writing all infos got in the local document
            arquivo.write(finalString)
            print(finalString)
            arquivo.write('\n')

#Free api only give 333 request per day, then we can get the value of BTC every 5 minutes, so we don't exceed the requirements limit
schedule.every(300).seconds.do(insert_Value) #get info every 5 minutes

while True:
    schedule.run_pending()
    time.sleep(1)
