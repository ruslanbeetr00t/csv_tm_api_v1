import requests
import time

from settings import API, user_agent
from endpoint_for_work_bot import GetItemsToGive, Trades


def checking_status_item():
    while True:
        try:
            time.sleep(3)
            payloads = {'key': API}
            """url=GetItemsToGive"""
            response = requests.get(url=GetItemsToGive, params=payloads, headers=user_agent)
            if response.status_code == 200:
                # print(response.json()['success'])
                if response.json()['success'] is True:
                    # status_item = response.json()['offers']
                    # print('ok')
                    """url=Trades"""
                    response = requests.get(url=Trades, params=payloads, headers=user_agent)
                    if response.status_code == 200:
                        status_item = response.json()
                        """url = url_ItemRequest"""
                        if status_item['ui_status'] == "4":
                            url_ItemRequest_4 = f"https://market.csgo.com/api/ItemRequest/out/{status_item['ui_bid']}/?key={API}"
                            response = requests.post(url=url_ItemRequest_4, headers=user_agent)
                            if response.status_code == 200:
                                return response.json()
                        elif status_item['ui_status'] == "2":
                            url_ItemRequest_2 = f"https://market.csgo.com/api/ItemRequest/in/1/?key={API}"
                            response = requests.post(url=url_ItemRequest_2, headers=user_agent)
                            if response.status_code == 200:
                                return response.json()
                        else:
                            continue
            else:
                continue

        except Exception as msg_err:
            print(msg_err)


checking_status_item()

"""
Возможные статусы:

    "ui_status" = 1 — Вещь выставлена на продажу.
    "ui_status" = 2 — Вы продали вещь и должны ее передать боту.
    "ui_status" = 3 — Ожидание передачи боту купленной вами вещи от продавца.
    "ui_status" = 4 — Вы можете забрать купленную вещь. 

"""