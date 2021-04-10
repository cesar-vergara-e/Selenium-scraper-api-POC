import json
import requests


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from apscheduler.schedulers.blocking import BlockingScheduler

import os
import time


sched = BlockingScheduler()

CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')


options = Options()
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True

print('Building chrome driver...')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)

print('Starting app...')

@sched.scheduled_job('interval', minutes=10)
def falabella():
    url = 'https://www.falabella.com/falabella-cl/product/14618594/Xbox-Series-X/14618594'
    url = 'https://www.falabella.com/falabella-cl/product/15136328/Control-Xbox-Series-X-Black/15136328'
    for i in range(10):
        try:
            driver.get(url)
            el = driver.find_element_by_class_name('price-0')
            if(el.text):
                telegram_bot_sendtext("REVISAR FALABELLA https://www.falabella.com/falabella-cl/product/14618594/Xbox-Series-X/14618594")
        # do thing
        except:
            time.sleep(10)
            print("exception")
        else:
            break   

@sched.scheduled_job('interval', minutes=10)
def ml():
    url = 'https://articulo.mercadolibre.cl/MLC-560235773-consola-xbox-series-x-_JM'
    #url = 'https://articulo.mercadolibre.cl/MLC-562836047-sony-playstation-ps5-version-disco-_JM'
    
    
    for i in range(10):
        try:
            driver.get(url)
            el = driver.find_element_by_class_name('ui-pdp-actions__container')
            if(el.text):
                telegram_bot_sendtext("REVISAR ML https://articulo.mercadolibre.cl/MLC-560235773-consola-xbox-series-x-_JM")
        except:
            time.sleep(10)
            print("exception")
        else:
            break   

@sched.scheduled_job('interval', minutes=10)
def abcdin():
    url = 'https://www.abcdin.cl/tienda/es/abcdin/entretenimiento/videojuegos/consola-serie-x-xbox-1144969?fbclid=IwAR3xlq-fWsTh_hHpk16T5SjtB43goD44-B2J7Z8NgvAuceVBE86BlB6889c'
    #url = 'https://www.abcdin.cl/tienda/es/abcdin/consola-nintendo-switch-lite-gris-1136581'

    for i in range(10):
        try:
            driver.get(url)
            print("intento abcdin")
            el = driver.find_element_by_id('productPageShoppingCart')
            if(el.text != "Producto Agotado"):
                telegram_bot_sendtext("REVISAR ABCDIN https://www.abcdin.cl/tienda/es/abcdin/entretenimiento/videojuegos/consola-serie-x-xbox-1144969?fbclid=IwAR3xlq-fWsTh_hHpk16T5SjtB43goD44-B2J7Z8NgvAuceVBE86BlB6889c")
        except:
            time.sleep(10)
            print("exception")
        else: 
            break




def telegram_bot_sendtext(bot_message):
    
    bot_token = os.environ.get('TELEGRAM_TOKEN') 
    bot_chatID = os.environ.get('TELEGRAM_CHATID') 
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


sched.start()
