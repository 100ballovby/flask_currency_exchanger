from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from models import *
from app import db


class ExchangeForm(FlaskForm):
    from_currency = SelectField('From')
    to_currency = SelectField('To')
    amount = IntegerField('Amount')
    submit = SubmitField('Exchange')
