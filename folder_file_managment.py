import os
import platform

from function import *
from library import dict_celeb

while True:
    print('Menu management folder and file directory:')
    print('1. Create new folder')
    print('2. Delete folder or file')
    print('3. Copy folder or file')
    print('4. Viewing the contents of the working directory')
    print('5. Viewing only folders')
    print('6. Viewing only files')
    print('7. View information about the operating system')
    print('8. Program creator')
    print('9. Play a victory')
    print('10.My bank account')
    print('11.Change working directory')
    print('12.Exit')

    choice = input('Select a menu item: ')
    if choice == '1':
        create_folder()
        pass
    elif choice == '2':
        delete_folder_file()
        pass
    elif choice == '3':
        copy_folder_file()
        pass
    elif choice == '4':
        path = os.getcwd()
        print(path)
        print(os.listdir(path))
        #  for root, dirs, files in os.walk(path):
        #      for dir in dirs:
        #          print('Каталог:', os.path.join(root, dir))
        #          for file in files:
        #              print('Файлы:', os.path.join(dir,file))
        pass
    elif choice == '5':
        print(view_folders())
        pass
    elif choice == '6':
        print(view_files())
        pass
    elif choice == '7':
        print(platform.platform())  # os.uname() - не работает
        pass
    elif choice == '8':
        print(os.getlogin())
        pass
    elif choice == '9':
        repeat_prog = 'да'
        while repeat_prog == 'да':
            count_names = int(input('Введите количество имен для угадывания: '))
            victory_birth(dict_celeb, count_names)
            repeat_prog = input('Если хотите начать игру сначала, введите - да, если не хотите - введите нет: ')
        pass
    elif choice == '10':
        history_transaction = []
        print('Добро пожаловать в ваш электроный кошелек!')

        while True:
            print('1. пополнение счета')
            print('2. покупка')
            print('3. история покупок')
            print('4. запросить баланс')
            print('5. выход')

            choice = input('Выберите пункт меню: ')
            if choice == '1':
                transaction(history_transaction, 1)
                balance_func(history_transaction)
                pass
            elif choice == '2':
                transaction(history_transaction, -1)
                balance_func(history_transaction)
                pass
            elif choice == '3':
                history_buy(history_transaction)
                pass
            elif choice == '4':
                balance_func(history_transaction)
                pass
            elif choice == '5':
                break
            else:
                print('Неверный пункт меню')
        pass
    elif choice == '11':
        print(
            f'The current path of your directory: {print(os.getcwd())}')  # текущая директория C:\Users\spiri\PycharmProjects\Console-file-manager
        path = input('Enter path new_dir:  ')  # work5_console_file_manager создавал для пробы
        while not os.path.exists(path):
            os.makedirs(path)  # - создаёт new directory
            print(f'New directory {path} create ')
        os.chdir(path)
        pass
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
