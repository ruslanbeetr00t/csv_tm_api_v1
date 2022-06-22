import requests
from pprint import pprint

from endpoint import GetInv, Trades, GetMoney, GoOffline, GetToken, GetWSAuth, UpdateInventory, InventoryItems, \
    GetDiscounts, GetCounters, GetMyProfileHash, GetMySellOffers, GetItemsToGive, QuickItems, Test, GetChatLog, \
    StatusOrders, DeleteOrders, RemoveAll
from settings import API, user_agent
from program_messages import endpoint_messages, user_can_messages


def user_change_endpoint():
    endpoint_dict = {1: GetInv, 2: Trades, 3: GetMoney, 4: GoOffline, 5: GetToken, 6: GetWSAuth, 7: UpdateInventory,
                     8: InventoryItems, 9: GetDiscounts, 10: GetCounters, 11: GetMyProfileHash, 12: GetMySellOffers,
                     13: GetItemsToGive, 14: QuickItems, 15: Test, 16: GetChatLog, 17: StatusOrders, 18: DeleteOrders,
                     19: RemoveAll}
    user_input = int(input(endpoint_messages))
    if user_input in endpoint_dict.keys():
        return endpoint_dict.get(user_input)


def send_user_url():
    user_url = user_change_endpoint()
    print(f'You choose\n{user_url}')
    payload = {'key': API}
    response = requests.get(url=user_url, headers=user_agent, params=payload)
    if response.status_code == 200:
        pprint(response.json())
    else:
        print(user_can_messages)


send_user_url()
