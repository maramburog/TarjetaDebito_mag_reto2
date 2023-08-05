from app import crud
from app.crud import create_user, create_account, create_debit_card, delete_user, delete_account, get_account_by_id, \
    update_user, get_user_by_id
from app.models import db, User, Account, DebitCard

if __name__ == "__main__":
    db.connect()
    db.create_tables([User, Account, DebitCard])

    #### Example Create - se necesita nuevo user o comentar las lines estas
    #user = create_user("test 12111")
    #account = create_account(user, 55552)
    #debit_card = create_debit_card(account, 55552)

    ### EXAMPLE PRINT
    # print("User:", user.username)
    # print("Account balance:", account.balance)
    # print("Debit Card balance:", debit_card.balance)



    #### Actualizar un usuario
    #user = get_user_by_id(1)
    #if user:
    #    updated_user = update_user(user, "nuEVO NOMBRE")

    ##### Eliminar una cuenta
    #account = get_account_by_id(1)
    #if account:
    #    delete_account(account)


    ### mostrar info de todas las tarjetas
    for i in DebitCard.select():
        #print(i.account.user, i.account.user.username, i.balance)
        print("User:", i.account.user)
        print("Username:", i.account.user.username)
        print("DebitCard balance:", i.balance)


    db.close()
