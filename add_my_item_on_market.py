import requests
import json
import time
from pprint import pprint

from settings import API, user_agent, absolute_path_get_inv
from endpoint_for_work_bot import SetPrice


with open(f'{absolute_path_get_inv}/get_inv.json', 'r', encoding='utf-8') as file_json:
    box_info = json.load(file_json)


def add_item_on_market():
    for item in box_info:
        if item["on_market"] == 1:
            time.sleep(3)
            payloads = {"key": API}
            """тут передача аргументів про предмет через params=payload не працює"""
            url_add_item_om_market = f'{SetPrice}{item["i_classid"]}_{item["i_instanceid"]}/{int(item["max_price"]) * 100}'
            response = requests.post(url=url_add_item_om_market, params=payloads, headers=user_agent)
            if response.status_code == 200:
                pprint(response.json())
            else:
                print(f'Something wrong:- {response.json()}')
                continue
        else:
            continue


add_item_on_market()
