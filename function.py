import os
import sys
import shutil
import random
import datetime


def decorate_complete(func):
    def inner(*args, **kwargs):
        print('-' * 45)
        print('Пожалуйста подождите, операция выполняется..\n')
        result = func(*args, **kwargs)
        print(result)
        print('-' * 45)
        return result

    return inner()


def create_folder(folder_name='new folder'):
    if folder_name == 'new folder':
        folder_name = input('Enter folder name: ')
    # проверка на существование
    if not os.path.exists(folder_name):
        # создать папку передаем путь
        os.mkdir(folder_name)
        print('Папка создана')
        return True
    else:
        print('Уже есть папка с таким же именем, введите другое имя')
        return False



def delete_folder_file(folder_file_name='new_name'):
    if folder_file_name == 'new_name':
        folder_file_name = input('Enter folder or file name: ')
    # проверка на существование

    if os.path.exists(folder_file_name):
        # удалить папку передаем путь
        shutil.rmtree(folder_file_name) if os.path.isdir(folder_file_name) == True else os.remove(folder_file_name)
        print('The folder or files has been deleted successfilly ')
    else:
        print('A file this is name does not exist, try again enter name ')


def copy_folder_file(folder_file_name=0, new_folder_file_name=0):
    if folder_file_name == 0 and new_folder_file_name == 0:
        folder_file_name = input('Enter folder or file name which for copy: ')
        new_folder_file_name = input('Enter new folder or file name: ')
    if os.path.isdir(folder_file_name) == True:
        result = shutil.copytree(folder_file_name, new_folder_file_name)
    else:
        result = shutil.copy(folder_file_name, new_folder_file_name)
    return result


def view_folders():
    list_dir = os.listdir()
    # for i in range(len(list_dir)):
    #     if os.path.isdir(list_dir[i]) == True:
    #         list_folder.append(list_dir[i])
    list_folder = [i for i in list_dir if os.path.isdir(i) == True]
    return list_folder


def view_files():
    list_dir = os.listdir()
    list_files = []
    # for i in range(len(list_dir)):
    #     if os.path.isfile(list_dir[i]) == True:
    #         list_files.append(list_dir[i])
    list_files = [i for i in list_dir if os.path.isfile(i) == True]
    return list_files


def victory_birth(dict_names, count_names):
    """случайный выбор имен для викторины (количество имён передаётся как параметр)"""
    # select_names = random.sample(list(dict_names.keys()), count_names)
    # print(select_names)
    select_names = random_names(dict_names, count_names)
    for i in range(count_names):
        date_of_birth = input(f'Когда родился {select_names[i]} ? '
                              f'введите дату рождения в формате dd.mm.yyyy:')
        if date_of_birth == dict_names.get(select_names[i]):
            print(f'Вы угадали! {select_names[i]} родился {date_of_birth}!')

        else:
            print(f'Вы не угадали! {select_names[i]} родился {dict_names.get(select_names[i])}!')
    pass


def random_names(dict_names, count_names):
    select_names = random.sample(list(dict_names.keys()), count_names)
    print(select_names)
    return select_names


def transaction(history_transaction, positiv_negativ_numb,
                add_transaction=0):  # add_transaction=0 - добавлен параметр для возможности тестирования
    # positiv_negativ_numb - параметр показывает какую операцию хошет выполнить пользователь, пополнить счет или совершить покупку
    # balance = 0
    dt_now = str(datetime.datetime.now())  # время транзакзии
    if positiv_negativ_numb > 0:
        if add_transaction == 0:
            while True:
                try:
                    add_transaction = {dt_now: float(input('Ввведите сумму , которую вы хотите внести на ваш счёт: '))}
                except ValueError:
                    print('Вы ввели не числовое значение, введите сумму цифрами снова ')
                else:
                    history_transaction.append(add_transaction)
                    break
        else:
            add_transaction = {dt_now: add_transaction}
            history_transaction.append(add_transaction)
            # for i in history_transaction:
            #     summ = list(i.values())  # dict_values из пары транзакция и дата
            #     balance += summ[0]
        balance = sum((list(i.values()))[0] for i in history_transaction)
        return balance
    else:
        # for i in history_transaction:
        #     summ = list(i.values())  # dict_values из пары транзакция и дата
        #     # balance += summ[0]
        balance = sum((list(i.values()))[0] for i in history_transaction)
        if add_transaction == 0:
            while True:
                try:
                    add_transaction = {dt_now: float(input('Ввведите сумму вашей покупки: '))}
                except ValueError:
                    print('Вы ввели не числовое значение, введите сумму цифрами снова ')
                else:
                    break
        else:
            add_transaction = {dt_now: add_transaction}
        if add_transaction[dt_now] <= balance:
            add_transaction[dt_now] *= -1  # умножаем на -1 для того что бы сумма добавлялась с минусом, это покупка
            history_transaction.append(add_transaction)
            return True
        else:
            print('Сумма покупки превышает ваш баланс')
            return False


def balance_func(history_transaction):
    # balance = 0
    # for i in history_transaction:
    #     summ = list(i.values())  # dict_values из пары транзакция и дата
    #     balance += summ[0]
    balance = sum((list(i.values()))[0] for i in history_transaction)
    print(f'Ваш баланс: {balance} $')
    return balance


def history_buy(history_transaction):
    buy_list = [i for i in history_transaction if (list(i.values()))[0] < 0]
    [print(f'Покупка: {i} $', sep='\n') for i in buy_list]
    all_summ_buy = sum((list(i.values()))[0] for i in history_transaction if (list(i.values()))[0] < 0)
    print(f'Общая сумма покупок: {all_summ_buy * -1} $')
    return buy_list
