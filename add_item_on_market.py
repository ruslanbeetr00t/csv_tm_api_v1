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
                if item_on_market["on_market"] == 1:
                    get_enemy_price_url = f'{SellOffers}{item_on_market["i_classid"]}_{item_on_market["i_instanceid"]}'
                    payloads = {'key': API}
                    response = requests.get(url=get_enemy_price_url, params=payloads, headers=user_agent)
                    if response.status_code == 200:
                        item_best_offer = response.json()["best_offer"]
                        if int(item_best_offer) > int(item_on_market['min_price'] * 100) and int(item_best_offer) < int(item_on_market['max_price'] * 100):
                            my_price = int(item_best_offer) - 10
                            item_on_market['bot_my_price'] = my_price
                            url_mass_set_price = f'{MassSetPrice}{item_on_market["i_classid"]}_{item_on_market["i_instanceid"]}/{my_price}'
                            response = requests.post(url=url_mass_set_price, params=payloads, headers=user_agent)
                            if response.status_code == 200:
                                print(f"{response.json()['items'][0]['market_hash_name']}:- {response.json()['items'][0]['price']}")
                        elif int(item_best_offer) > int(item_on_market['min_price'] * 100):
                            print(f"Need to change the price:- {item_on_market['i_market_name']}, ui_id:- {item_on_market['ui_id']}")
                            continue
                        time.sleep(3)
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

