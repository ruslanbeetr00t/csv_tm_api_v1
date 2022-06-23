import requests
import json
import time
import sys

from settings import API, user_agent, absolute_path_get_inv
from endpoint_for_work_bot import SellOffers, MassSetPrice

with open(f'{absolute_path_get_inv}/get_inv.json', 'r', encoding='utf-8') as file_json:
    my_items_on_market = json.load(file_json)


def sell_bot():
    try:
        while True:
            for item_on_market in my_items_on_market:
                time.sleep(3)
                if item_on_market["on_market"] == 1:
                    get_enemy_price_url = f'{SellOffers}{item_on_market["i_classid"]}_{item_on_market["i_instanceid"]}'
                    payloads = {'key': API}
                    response = requests.get(url=get_enemy_price_url, params=payloads, headers=user_agent)
                    if response.status_code == 200:
                        """максимально деревяний варіант"""
                        item_box_price = response.json()
                        if item_on_market['min_price'] >= item_box_price['best_offer']:
                            continue
                        else:
                            if int(item_box_price['offers'][0]['price']) > int(item_on_market['min_price'] * 100) and int(item_box_price['offers'][0]['price']) < int(item_on_market['max_price'] * 100):
                                url_mass_set_price = f'{MassSetPrice}{item_on_market["i_classid"]}_{item_on_market["i_instanceid"]}'
                                response = requests.post(url=url_mass_set_price, params=payloads, headers=user_agent)
                                if response.status_code == 200:
                                    print(f"{response.json()['items'][0]['market_hash_name']}:- {response.json()['items'][0]['price']}")
                            else:
                                if int(item_box_price['offers'][0]['price']) < int(item_on_market['min_price'] * 100):
                                    print(f"Price changes{response.json()['items'][0]['market_hash_name']}")
                else:
                    continue
    except requests.exceptions.Timeout as msg_err:
        print(f'Time out error:-> {msg_err}')
    except requests.exceptions.TooManyRedirects as msg_err:
        print(f'TooManyRedirects:-> {msg_err}')
    except requests.exceptions.ConnectionError as msg_err:
        sys.exit(f'Problem with DNS or internet:-> {msg_err}')
    except requests.exceptions.HTTPError as msg_err:
        print(f'Status code not correct or Error:-> {msg_err}')
    except KeyboardInterrupt as msg_err:
        print(f'Stop script:-> {msg_err}')
    finally:
        sell_bot()


if __name__ == "__main__":
    sell_bot()

