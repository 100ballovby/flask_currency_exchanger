from app import app
from models import *
from flask import render_template, redirect, url_for


@app.route('/')
def main_page():
    cur_list = Currencies.query.order_by(Currencies.code).all()
    # выгружаю все валюты из базы данных и передаю их в шаблон
    return render_template('index.html', title='Main page', curr=cur_list)

