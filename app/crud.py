from .models import User, Account, DebitCard


# User CRUD
def create_user(username):
    return User.create(username=username)


def get_user_by_id(user_id):
    return User.get_or_none(id=user_id)


def update_user(user, new_username):
    user.username = new_username
    user.save()
    return user


def delete_user(user):
    user.delete_instance()


# Account CRUD
def create_account(user, balance):
    return Account.create(user=user, balance=balance)


def get_account_by_id(account_id):
    return Account.get_or_none(id=account_id)


def update_account(account, new_balance):
    account.balance = new_balance
    account.save()
    return account


def delete_account(account):
    account.delete_instance()


# Debit Card CRUD
def create_debit_card(account, balance):
    return DebitCard.create(account=account, balance=balance)


def get_debit_card_by_id(card_id):
    return DebitCard.get_or_none(id=card_id)


def update_debit_card(debit_card, new_balance):
    debit_card.balance = new_balance
    debit_card.save()
    return debit_card


def delete_debit_card(debit_card):
    debit_card.delete_instance()
