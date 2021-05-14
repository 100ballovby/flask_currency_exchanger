from app import db


class Currencies(db.Model):
    '''Таблица для хранения валют и кодов валют'''
    __tablename__ = 'currencies'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(3), unique=True)
    name = db.Column(db.String(200), unique=True)

    def __repr__(self):
        return f'Code: {self.code}, name: {self.name}'
