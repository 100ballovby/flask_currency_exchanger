import requests
import json
from app import db
from models import *


url = 'https://api.coinbase.com/v2/currencies'
response = requests.get(url)  # подключаюсь к серверу
cur = json.loads(response.text)  # выгружаю ответ сервера
for i in cur['data']:
    c = Currencies()
    c.code = i['id']
    c.name = i['name']
    db.session.add(c)
    db.session.commit()