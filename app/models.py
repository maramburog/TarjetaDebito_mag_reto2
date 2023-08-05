from peewee import Model, CharField, DecimalField, ForeignKeyField, SqliteDatabase

db = SqliteDatabase('debit_card.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)


class Account(BaseModel):
    user = ForeignKeyField(User, backref='accounts')
    balance = DecimalField(max_digits=10, decimal_places=2)


class DebitCard(BaseModel):
    account = ForeignKeyField(Account, backref='debit_cards')
    balance = DecimalField(max_digits=10, decimal_places=2)
