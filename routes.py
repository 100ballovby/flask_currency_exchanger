from app import app
from models import *
from forms import ExchangeForm
from flask import render_template, redirect, url_for


@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = ExchangeForm()
    form.from_currency.choices = [(cur.code, cur.name) for cur in Currencies.query.all()]
    form.to_currency.choices = [(cur.code, cur.name) for cur in Currencies.query.all()]

    # выгружаю все валюты из базы данных и передаю их в форму
    return render_template('index.html', title='Main page', form=form)

