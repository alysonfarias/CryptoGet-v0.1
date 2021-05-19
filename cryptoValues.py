import requests
from datetime import datetime

# Step 1: Get your API on https://coinmarketcap.com/api/    

# free plan give [333 per days] [10.000 per month] requests
# API call rate limit: 30 requests a minute
# You could see the api documentation on https://coinmarketcap.com/api/documentation/v1/

apyKey ='' #insert your apykey from CoinMarketCap [step 1]
myBTCBalance = 1	# insert your BTC value here

headers = {
    'X-CMC_PRO_API_KEY': apyKey, 
    'Accepts': 'application/json'
}

parameters = {
  'start': '1',
  'limit': '5', # this could be a future issue, cause this get limit paremet only get top 5(actual variable but could be until 5000) coins right now(where the btc is the first one 19/05/2021), however possibily future code upgrade, like additioniting more coin 
  'convert': 'USD'
}

#API url from CoinMarketCap
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#requesting info and transforming in .json
json = requests.get(url, params=parameters, headers=headers).json()

coins = json['data']
arquivo = open("coinHistoric.txt", "a")


#function to transform a tuple in string
def convertTuple(tup):
    str =  ''.join(tup)
    return str

for coin in coins:
    if coin['symbol'] == 'BTC':
        # the actual value from btc multiplied from your actual balance value
        valueFormat = "%.2f" %(coin['quote']['USD']['price'] * myBTCBalance)
        #symbol coin
        symbol = coin['symbol']
        # get the hours and date
        actual_date = datetime.now()
        actual_date_and_hour = actual_date.strftime('%d/%m/%Y %H:%M')
        tuple = '[ ', actual_date_and_hour, " : ", symbol, ' value = $', valueFormat ,' USD', ' ]'
        # tuple to string
        finalString = convertTuple(tuple)
        # writing all infos got in the local document 
        arquivo.write(finalString)
        arquivo.write('\n')

    
