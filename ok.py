from endpoint import GetInv, Trades, GetMoney
from settings import API, user_agent
import requests

payload = {'key': API}
response = requests.get(url=GetMoney, headers=user_agent, params=payload)
if response.status_code == 200:
    print(response.json())
