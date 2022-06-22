import requests
import json

from settings import API, user_agent, absolute_path_get_inv
from endpoint_for_work_bot import GetInv


def get_inv_info():
    item_box = []
    payload = {'key': API}
    response = requests.get(url=GetInv, headers=user_agent, params=payload)
    if response.status_code == 200:
        if response.json()["ok"] is True:
            for item in response.json()["data"]:
                """методом pop удаляємо непотрібну інформацію про предмет, для подальшої обробки інформації"""
                item.pop("i_descriptions")
                item.pop("i_market_price_text")
                """в кожний словник з інформацією про предмет додаємо наші параметри"""
                item["min_price"] = 0.00
                item["max_price"] = 0.00
                item["on_market"] = 0
                item_box.append(item)
        with open(f'{absolute_path_get_inv}/get_inv.json', 'w', encoding='utf-8') as file_json:
            json.dump(item_box, file_json, ensure_ascii=False, indent=4)
    else:
        print('Something wrong...\nTry again.')


get_inv_info()
