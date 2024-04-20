import requests
import os
from dotenv import load_dotenv

load_dotenv()

telegram_bot_token = os.getenv("telegram_bot_token")
chat_id = os.getenv("chat_id")

telegram_bot_url = f"https://api.telegram.org/bot{telegram_bot_token}/"


def send_message(chat_id, message):
    method = "sendMessage"
    params = f"?chat_id={chat_id}/&text={message}"
    requests.get(telegram_bot_url + method + params)


send_message(chat_id, "🗣🔥🔥🔥I deleted all my messages)🔥🔥🔥")
