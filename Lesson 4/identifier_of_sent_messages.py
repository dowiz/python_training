import telebot
import os
from dotenv import load_dotenv

load_dotenv()

telegram_bot_token = os.getenv("telegram_bot_token")
bot = telebot.TeleBot(telegram_bot_token, parse_mode=None)


# Обробник команди /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Привіт! Я бот, який надсилає ID отриманих повідомлень.')


# Обробник усіх отриманих повідомлень
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f'ID цього повідомлення: {
                     message.message_id}')


# Запуск бота
bot.polling()
