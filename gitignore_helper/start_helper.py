import subprocess
import os
import time

"""Створюємо файли які знаходятся в файлі .gitignore"""


def create_file():
    git_ignore_file_names = ['settings', 'endpoint', 'program_messages', 'endpoint_for_work_bot']
    for file in git_ignore_file_names:
        time.sleep(1)
        subprocess.run(["touch", f"{file}.py"])
        """5 це кількість файлів (4 створені програмою) і 5 це start_helper.py"""
        if len(os.listdir()) == 5:
            return os.listdir()
        else:
            continue


"""В кожен файл записуємо данні для коректної роботи програми"""


def write_info_in_file():
    files = create_file()
    for info in files:
        print(info)
        if info == 'settings.py':
            with open('settings.py', 'w') as file_py:
                file_py.write('API = ""\n\n\nuser_agent = {"User-Agent": ""}\n\n\nTOKEN = ""\n\n\nabsolute_path_get_inv = ""\n\n\nstandart_price = 100')
        elif info == 'endpoint.py':
            with open('endpoint.py', 'w') as file_py:
                file_py.write('GetInv = ""\n\nTrades = ""\n\nGetMoney = ""\n\nGoOffline = ""\n\nGetToken = '
                              '""\n\nGetWSAuth = ""\n\nUpdateInventory = ""\n\nInventoryItems = ""\n\nGetDiscounts = '
                              '""\n\nGetCounters = ""\n\nGetMyProfileHash = ""\n\nGetMySellOffers = '
                              '""\n\nGetItemsToGive = ""\n\nQuickItems = ""\n\nTest = ""\n\nGetChatLog = '
                              '""\n\nStatusOrders = ""\n\nDeleteOrder = ""\n\nRemoveAll = ""\n\nPingPong = ""\n\n')
        elif info == 'program_messages.py':
            with open('program_messages.py', 'w') as file_py:
                file_py.write('endpoint_messages = """Start program:-\n1 - GetInv\n2 - Trades\n3 - GetMoney\n4 - '
                              'GoOffline\n5 - GetToken\n6 - GetWSAuth\n7 - UpdateInventory\n8 - InventoryItems\n9 - '
                              'GetDiscounts\n10 - GetCounters\n11 - GetMyProfileHash\n12 - GetMySellOffers\n13 - '
                              'GetItemsToGive\n14 - QuickItems\n15 - Test\n16 - GetChatLog\n17 - StatusOrders\n18 - '
                              'DeleteOrder\n19 - RemoveAll\n"""\n\nuser_can_messages = "Problem with connect or technical work on the web site. Wait or try again..."')
        elif info == 'endpoint_for_work_bot.py':
            with open('endpoint_for_work_bot.py', 'w') as file_py:
                file_py.write('GetInv = ""\n\nSetPrice = ""\n\nSellOffers = ""\n\nMassSetPrice = ""')
        else:
            continue
    if len(os.listdir()) == 5:
        lift_file_on_directory = os.listdir()
        lift_file_on_directory.remove('start_helper.py')
        for file in lift_file_on_directory:
            subprocess.run(["mv", f"{file}", ".."])
            print(f'Create this file:- {file}')
        print('Program END work.\nRemember to add information to these files!!!')


"""Головне не забути додати свої данні для роботи програми і додати url для коректної роботи endopointів"""

if __name__ == "__main__":
    write_info_in_file()
