import telebot
import os
from dotenv import load_dotenv

load_dotenv()

telegram_bot_token = os.getenv("telegram_bot_token")
bot = telebot.TeleBot(telegram_bot_token, parse_mode=None)
