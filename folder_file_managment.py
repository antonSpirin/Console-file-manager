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
        os.getcwd()
        pass
    elif choice == '5':
        # !!!!!!!!!!!!!

        pass
    elif choice == '6':
        os.listdir()
        pass
    elif choice == '7':
        os.uname()
        pass
    elif choice == '8':
        os.getpid()
        pass
    elif choice == '9':
        repeat_prog = 'да'
        while repeat_prog == 'да':
            victory_birth(dict_celeb, 5)
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
        print(f'The current path of your directory: {print(os.getcwd())}') # текущая директория C:\Users\spiri\PycharmProjects\Console-file-manager
        path=input('Enter path new_dir:  ')
        while not os.path.exists(path):
            os.makedirs(path) #- создаёт new directory
            print(f'New directory {path} create ')
        os.chdir(path)
        break
    else:
        print('Неверный пункт меню')
