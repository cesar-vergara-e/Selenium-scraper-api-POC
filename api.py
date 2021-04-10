from flask import Flask, Response, request
from flask_cors import CORS
import json
import requests


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
import os

CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')


options = Options()
options.binary_location = GOOGLE_CHROME_BIN
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.headless = True

print('Building chrome driver...')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)

print('Starting app...')


url = 'https://www.falabella.com/falabella-cl/product/14618594/Xbox-Series-X/14618594'

try:
    driver.get(url)

    el = driver.find_element_by_class_name('title6')
    print(el.text)
    if (el.text != "¡Qué mal! Justo se agotó"):
        print("REVISAR Falabella")
except:
    print("hubo un error en Falabella")
 

url = 'https://articulo.mercadolibre.cl/MLC-560235773-consola-xbox-series-x-_JM'

try:
    driver.get(url)

    el = driver.find_element_by_class_name('andes-message__text--warning')
    print(el.text)
    if (el.text != "Publicación pausada"):
        print("REVISAR ML")
except:
    print("hubo un error en ML")


url = 'https://www.abcdin.cl/tienda/es/abcdin/entretenimiento/videojuegos/consola-serie-x-xbox-1144969?fbclid=IwAR3xlq-fWsTh_hHpk16T5SjtB43goD44-B2J7Z8NgvAuceVBE86BlB6889c'
try:
    driver.get(url)

    el = driver.find_element_by_class_name('title-suscribir')
    print(el.text)

    if (el.text != "PRODUCTO AGOTADO"):
        print("Revisar ABCDIN")

except:
    print("hubo un error en ABCDIN")




def telegram_bot_sendtext(bot_message):
    
    bot_token = os.environ.get('TELEGRAM_TOKEN') 
    bot_chatID = os.environ.get('TELEGRAM_CHATID') 
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

