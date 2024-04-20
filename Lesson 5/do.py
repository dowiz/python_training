from telegram_bot import bot
from telegram_bot import start_message
from telegram_bot import show


@bot.message_handler(commands=['start'])
def start_message_handler(message):
    start_message(message)


@bot.message_handler(content_types=['text'])
def show_message_handler(message):
    show(message)


bot.polling(none_stop=True)
