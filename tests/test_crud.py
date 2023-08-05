from app.models import db, User, Account
from app.crud import create_user, create_account, update_account

def test_update_account_balance():
    # Crear un usuario y una cuenta
    user = create_user("test_user")
    account = create_account(user, 1000)

    # Actualizar el saldo de la cuenta
    new_balance = 1500
    updated_account = update_account(account, new_balance)

    # Verificar que el saldo se haya actualizado correctamente
    assert updated_account.balance == new_balance