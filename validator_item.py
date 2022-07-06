import json

from settings import standart_price, absolute_path_get_inv

"""отримання url і витягування двох параметрів more_info[0] це classid , more_info[1] instanceid"""


def add_skin_ur():
    url = input('add skins url:- ')
    print(url)
    info = url.split('/')
    print(info)
    more_info = str(info[4]).split('-')
    print(more_info)
    classid = more_info[0]  # якщо потрібен тип int замість str потрібно записати так classid = int(more_info[0])
    instanceid = more_info[1]  # якщо потрібен тип int замість str потрібно записати так instanceid = int(more_info[1])
    print(classid, instanceid)
    return more_info


"""ціна премета від користувача з автоматичним умноженням на 100 (1 = 100)"""


def add_you_are_item_price():
    item_price = float(input('add you are skin price:- ')) * standart_price
    print(item_price)
    if type(item_price) == float:
        print(type(item_price))
        return item_price
    else:
        print('Error use number')
        return add_you_are_item_price()


"""створення словника з інформаціею про премет"""


def formation_dict_with_skin_info():
    skins_classid_instanceid = add_skin_ur()
    price = add_you_are_item_price()
    print(skins_classid_instanceid)
    get_url_skins = {'classid': skins_classid_instanceid[0],
                     'instanceid': skins_classid_instanceid[1],
                     'price': price}  # також непогана ідея використати цей варіант 'price': int(price) перевести тип foat в int .
    return get_url_skins

def open_json_file():
    with open(f'{absolute_path_get_inv}/buy_list.json', 'w', encoding='utf-8') as file_json:
        json.dump(formation_dict_with_skin_info(), file_json, indent=4)


open_json_file()