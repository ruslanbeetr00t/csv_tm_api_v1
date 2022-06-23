import requests
from loguru import logger
import time
import random

from settings import API, user_agent
from endpoint import PingPong

# logger.add('file_{time}.txt', format='{time} {level} {messages}', level='ERROR', rotation="10 KB",
#            compression='zip')


def ping_pong_connect():
    try:
        while True:
            time.sleep(35)
            payloads = {'key': API}
            response = requests.get(url=PingPong, headers=user_agent, params=payloads)
            if response.status_code == 200:
                print(f"{response.json()}:- {time.ctime()}")
            else:
               print(f"{response.json()}:- {time.ctime()}")
    finally:
        return ping_pong_connect


ping_pong_connect()
