from forex_python.bitcoin import BtcConverter
from forex_python.converter import CurrencyRates
from pycoingecko import CoinGeckoAPI
from telebot import TeleBot
import json
import telegram
import requests

BOT_TOKEN = '6287557426:AAEFwbJWWyctTUMgCQFpu7FFMpyYyW2a6p8'
bot = TeleBot(token=BOT_TOKEN)
coin_client = CoinGeckoAPI()
FOREX_API_URL = 'https://openexchangerates.org/api/latest.json?app_id=be648e683c1f42c28adce69304bb2bb9'

forex_currencies_list = {
    'EUR' : 'Euro Member Countries',
    'IDR' : 'Indonesia Rupiah',
    'BGN' : 'Bulgaria Lev',
    'ILS' : 'Israel Shekel',
    'GBP' : 'United Kingdom Pound ',
    'DKK' : 'Denmark Krone ',
    'CAD' : 'Canada Dollar', 
    'JPY' : 'Japan Yen ',
    'HUF' : 'Hungary Forint', 
    'RON' : 'Romania New Leu', 
    'MYR' : 'Malaysia Ringgit', 
    'SEK' : 'Sweden Krona', 
    'SGD' : 'Singapore Dollar' ,
    'HKD' : 'Hong Kong Dollar', 
    'AUD' : 'Australia Dollar', 
    'CHF' : 'Switzerland Franc' ,
    'KRW' : 'Korea (South) Won', 
    'CNY' : 'China Yuan Renminbi', 
    'TRY' : 'Turkey Lira', 
    'HRK' : 'Croatia Kuna' ,
    'NZD' :' New Zealand Dollar ',
    'THB' : 'Thailand Baht', 
    'USD' : 'United States Dollar', 
    'NOK' : 'Norway Krone', 
    'RUB' : 'Russia Ruble', 
    'INR' : 'India Rupee', 
    'MXN' : 'Mexico Peso', 
    'CZK' : 'Czech Republic Koruna', 
    'BRL' : 'Brazil Real', 
    'PLN' : 'Poland Zloty', 
    'PHP' : 'Philippines Peso', 
    'ZAR' : 'South Africa Rand'
}

def get_forex_prices():
    response = requests.get(FOREX_API_URL)
    data = json.loads(response.text)
    return data
    
@bot.message_handler(content_types=['text'])
def crypto_price_message_handler(message):
    crypto_id = message.text
    chat_id = message.chat.id
    price_response = coin_client.get_price(ids=crypto_id, vs_currencies='usd')
    data = get_forex_prices()
    currency_pairs = ['USD', 'EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF' ,'KRW', 'CNY' ,'TRY' ,'HRK' ,'NZD' ,'THB' ,'NOK' ,'RUB' ,'INR' ,'MXN' ,'CZK' ,'BRL' ,'PLN' ,'PHP' ,'ZAR']
    
    message = "Here are today's forex prices:\n\n"
    for pair in currency_pairs:
        price = data['rates'][pair]         
        message += f"{pair}: {price}$\n"

    if price_response:
        price = price_response[crypto_id]['usd']
        if crypto_id == 'forex':
            bot.send_message(chat_id=chat_id, text=message)
        else:
            bot.send_message(chat_id=chat_id, text=f"Price of {crypto_id} : {price}$ USD")
        if crypto_id == 'bitcoin':
            b = BtcConverter() 
            bitc_EUR = b.get_latest_price('EUR')
            bitc_INR = b.get_latest_price('INR')
            bitc_MXN = b.get_latest_price('MXN')
            bitc_CZK = b.get_latest_price('CZK')
            bitc_IDR = b.get_latest_price('IDR')  
            bitc_BGN = b.get_latest_price('BGN')  
            bitc_ILS = b.get_latest_price('ILS')  
            bitc_GBP = b.get_latest_price('GBP')  
            bitc_HKD = b.get_latest_price('HKD')  
            bitc_AUD = b.get_latest_price('AUD')  
            bitc_CHF = b.get_latest_price('CHF')  
            bitc_KRW = b.get_latest_price('KRW')  
            bitc_CNY = b.get_latest_price('CNY')  
            bitc_SGD = b.get_latest_price('SGD')  
            bitc_SEK = b.get_latest_price('SEK')  
            bitc_MYR = b.get_latest_price('MYR')  
            bitc_RON = b.get_latest_price('RON')  
            bitc_HUF = b.get_latest_price('HUF')  
            bitc_JPY = b.get_latest_price('JPY')  
            bitc_CAD = b.get_latest_price('CAD')  
            bitc_DKK = b.get_latest_price('DKK')  
            bitc_TRY = b.get_latest_price('TRY')  
            bitc_HRK = b.get_latest_price('HRK')  
            bitc_NZD = b.get_latest_price('NZD')  
            bitc_THB = b.get_latest_price('THB')  
            bitc_RUB = b.get_latest_price('RUB')  
            bitc_BRL = b.get_latest_price('BRL')  
            bitc_PLN = b.get_latest_price('PLN')
            bitc_PHP = b.get_latest_price('PHP')  
            bitc_ZAR = b.get_latest_price('ZAR')  

            bot.send_message(chat_id=chat_id, text=f"Price of bitcoin in forex currrencies:\n{bitc_EUR}$ EUR\n{bitc_INR}$ INR\n{bitc_MXN}$ MXN\n{bitc_CZK}$ CZK\n{bitc_IDR}$ IDR\n{bitc_BGN}$ BGN\n{bitc_ILS}$ ILS\n{bitc_GBP}$ GBP\n{bitc_HKD}$ HKD\n{bitc_AUD}$ AUD\n{bitc_CHF}$ CHF\n{bitc_KRW}$ KRW\n{bitc_CNY}$ CNY\n{bitc_SGD}$ SGD\n{bitc_SEK}$ SEK\n{bitc_MYR}$ MYR\n{bitc_RON}$ RON\n{bitc_HUF}$ HUF\n{bitc_JPY}$ JPY\n{bitc_CAD}$ CAD\n{bitc_DKK}$ DKK\n{bitc_TRY}$ TRY\n{bitc_HRK}$ HRK\n{bitc_NZD}$ NZD\n{bitc_THB}$ THB\n{bitc_BRL}$ BRL\n{bitc_PLN}$ PLN\n{bitc_PHP}$ PHP\n{bitc_ZAR}$ ZAR\n\nFor List of Supported Currency codes just type “help”\nFor todays forex prices just type “forex”")
    else:
        if crypto_id == '/start':
            bot.send_message(chat_id=chat_id, text='Welcome to CryptoForexBot ask me any CryptoCurrency name like bitcoin or ethereum\n\nFor todays forex prices just type “forex”\nFor List of Supported Currency codes just type “help”')
        elif crypto_id == 'help':
            bot.send_message(chat_id=chat_id, text=f'List of Supported Currency codes \n{forex_currencies_list}')
        else:
            bot.send_message(chat_id=chat_id, text=f"Crypto name : {crypto_id}  was not found")


if __name__ == '__main__':    
    bot.polling()