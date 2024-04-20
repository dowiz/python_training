import telebot
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN2 = os.getenv("TOKEN2")
bot = telebot.TeleBot(TOKEN2, parse_mode=None)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(
        resize_keyboard=True)  # buttons
    keyboard.row('🔍 ЮВЕНАЛЬНА ПОЛІЦІЯ', '🗺 КАРТА', '💰 Курс валют')
    keyboard.row('🗣 ЧАТ', '🌎 ПОСИЛАННЯ НА ОФІЦІЙНІ СТОРІНКИ')

    bot.send_message(
        message.chat.id, """Вітаю, {0.first_name}!\nНатисніть відповідну кнопку 👇 щоб отримати інформацію.\n\n(примітка, для того щоб відобразилась повна назва кнопки, переверніть свій смартфон в горизонтальне положення для автоматичного повороту зображення на екрані (для користувачів з невеликими екранами))""" .format(message.from_user), reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def show(message):
    data = message.json
    print(f'message: ', data['from'])
    # print(f'message: ', data['text'])
    if message.text == '🔍 show spanning-tree | begin VLAN0005':
        print(message.text)
    elif message.text == '🗣 show ip interface brief':
        print(message.text)
    elif message.text == '💰 show vlan brief':
        print(message.text)
    elif message.text == '🌎 ':
        print(message.text)
    elif message.text == '🗺 КАРТА':
        print(message.text)
    else:
        print(message.text)


bot.polling()
