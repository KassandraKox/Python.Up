'''Программа банкомат'''
import sys
START_SUM = 0

def check_input(message):
    while True:
        inp = int(input(message))
        if inp % 50 != 0:
            print('Error. Сумма должна быть кратна 50 у.е.')
        else:
            return inp
def addition_money(bal, op):
    deposit = check_input('Введите сумму пополнения: ')
    if op % 3 == 0:
        bal += bal * 0.3
    bal += deposit
    if bal > 5_000_000:
        bal -= bal // 10
    print(f'Вы внесли {deposit} у.е. На вашем счету {bal} у.е.')
    return bal, op

def withdraw_money(bal, op):
    if bal > 5_000_000:
        bal -= bal // 10
    withdraw = check_input('Введите сумму снятия: ')
    percent = withdraw * 0.015
    if percent < 30:
        percent = 30
    elif percent > 600:
        percent = 600
    withdraw += percent
    if bal > withdraw:
        bal -= withdraw
        print(f'Вы сняли {withdraw} у.е. На вашем счету {bal} у.е.')
    else:
        print('Недостаточно средств.')
    if op % 3 == 0:
        bal += bal * 0.3
    return bal, op

def user_interface():
    balance = START_SUM
    operations = 1
    while True:
        step = int(input('Какую операцию вы хотите провести?\n1 - Внести у.е.\n2 - Снять у.е.\n3 - Выйти.\n>>> '))
        match step:
            case 1:
                balance, operations = addition_money(balance, operations)
            case 2:
                balance, operations = withdraw_money(balance, operations)
            case 3:
                sys.exit()
            case _:
                print('error')

def greeting():
    print('Добро пожаловать в банк Кидалово!\n'
          'Допустимые действия:\n- пополнить счет на сумму кратную 50 у.е.\n- снять сумму кратную 50 у.е.\n- выйти.\n'
          'Комиссия за снятие - 1,5%, но не менее 30 и не более 600 у.е.\nПосле каждой третьей операции начисляется 3%.\nНе забудьте про налог на богатсво, 10%, при превышениие суммы 5 млн.у.е.')


greeting()
user_interface()
