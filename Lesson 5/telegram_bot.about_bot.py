import requests
from pprint import pprint as pp
from get_token import token


def get_bot_info(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    if response.status_code == 200:
        bot_info = response.json()
        return bot_info
    else:
        return None


bot_info = get_bot_info(token)

if bot_info:
    pp(bot_info['result'])
else:
    print("Failed to retrieve bot information.")
