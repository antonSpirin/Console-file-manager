import os
import sys
import shutil
import random


def create_folder():
    folder_name = input('Enter folder name: ')
    # проверка на существование
    if not os.path.exists(folder_name):
        # создать папку передаем путь
        os.mkdir(folder_name)


def delete_folder_file():
    folder_file_name = input('Enter folder or file name: ')
    # проверка на существование
    if os.path.exists(folder_file_name):
        # удалить папку передаем путь
        os.rmdir(folder_file_name)


def copy_folder_file():
    folder_file_name = input('Enter folder or file name which for copy: ')
    new_folder_file_name = input('Enter new folder or file name: ')
    shutil.copy(folder_file_name, new_folder_file_name)

def victory_birth(dict_names, count_names):
    """случайный выбор имен для викторины (количество имён передаётся как параметр)"""
    select_names = random.sample(list(dict_names.keys()), count_names)
    print(select_names)
    for i in range(count_names):
        date_of_birth = input(f'Когда родился {select_names[i]} ? '
                              f'введите дату рождения в формате dd.mm.yyyy:')
        if date_of_birth == dict_names.get(select_names[i]):
            print(f'Вы угадали! {select_names[i]} родился {date_of_birth}!')
        else:
            print(f'Вы не угадали! {select_names[i]} родился {dict_names.get(select_names[i])}!')
    pass

def transaction(history_transaction, positiv_negativ_numb):
    balance = 0
    for i in range(len(history_transaction)):
        balance += history_transaction[i]
    if positiv_negativ_numb > 0:
        add_transaction = float(input('Ввведите сумму , которую вы хотите внести на ваш счёт: '))
        history_transaction.append(add_transaction)
    else:
        add_transaction = float(input('Ввведите сумму вашей покупки: '))
        if add_transaction <= balance:
            add_transaction = add_transaction * -1  # умножаем на -1 для того что бы сумма добавлялась с минусом, это покупка
            history_transaction.append(add_transaction)
        else:
            print('Сумма покупки превышает ваш баланс')
    # print(history_transaction)


def balance_func(history_transaction):
    balance = 0
    for i in range(len(history_transaction)):
        balance += history_transaction[i]
    print(f'Ваш баланс: {balance} $')
    return balance


def history_buy(history_transaction):
    buy_list=[]
    all_summ_buy = 0
    for i in range(len(history_transaction)):
        if history_transaction[i] < 0:
            buy_list.append(history_transaction[i])
            all_summ_buy += history_transaction[i]
            print(f'Покупка: {history_transaction[i]} $')

    print(f'Общая сумма покупок: {all_summ_buy * -1} $')
    return buy_list

