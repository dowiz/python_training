from get_token import token
import telebot
from telebot import types

bot = telebot.TeleBot(token)
types = telebot.types

# global_sup_district = ''


def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True)  # buttons
    keyboard.row('ℹ️ Інформація про мене', '💱 Курс валют')

    bot.send_message(
        message.chat.id, 'Вітаю, {0.first_name}!\nНатисніть відповідну кнопку 👇 щоб отримати інформацію.' .format(
            message.from_user),
        reply_markup=keyboard)


def show(message):
    message_data = message.json
    print('\n')
    for key, value in message_data.items():
        print(key, value)
    username = write_info(message_data, 'username')
    id = write_info(message_data, 'id')
    first_name = write_info(message_data, 'first_name')
    last_name = write_info(message_data, 'last_name')
    chat_id = message_data['chat']['id']
    text = message_data['text']
    message_id = message.message_id
    message_to_reply = 'іd повідомлення: ' + str(message_id) + '\n\nusername: ' + username + '\nid: ' + \
        str(id) + '\nІм\'я: ' + first_name + \
        '\nПрізвище: ' + last_name

    if message.text == 'ℹ️ Інформація про мене':
        bot.send_message(id, message_to_reply)
        if message.chat.type != 'private':
            bot.send_message(chat_id, 'Відповідь у приватній розмові')
    elif message.text == '💱 Курс валют':
        keyboard = types.ReplyKeyboardMarkup(
            resize_keyboard=True)
        keyboard.row('🇺🇦🔄🇺🇸', '🇺🇦🔄🇪🇺')
        keyboard.row('Назад')
        bot.send_message(
            message.chat.id, 'Оберіть валюту:', reply_markup=keyboard)
    elif message.text == '🇺🇦🔄🇺🇸':
        bot.send_message(message.chat.id, 'exchange_rates[USD]')
    elif message.text == '🇺🇦🔄🇪🇺':
        bot.send_message(message.chat.id, 'exchange_rates[EUR]')
    elif message.text == 'Назад':
        start_message(message)
    else:
        bot.send_message(message.chat.id, 'Я не розумію, що ви хочете')


def write_info(message_data, variable):
    try:
        return message_data['from'][variable]
    except KeyError:
        return 'Немає данних'
