from flask import Flask  # импорт библиотеки
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# создаем переменную сайта, отключаем автоматический сбор конфигурации
app.config['SECRET_KEY'] = 'try-to-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import *
from routes import *

if __name__ == '__main__':  # инструкция запуска сайта
    app.run(debug=True)