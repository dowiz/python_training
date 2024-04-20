from get_token import token
import telebot
from telebot import types
from functions import get_devices, get_commands_device
from get_cisco_info import get_cisco_info
from pprint import pprint
import json


bot = telebot.TeleBot(token)
types = telebot.types
devices = get_devices()
tmp_commands_device = 'show'
device = ''


# Start message
def start_message(message):

    # Keyboard
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True)  # buttons
    keyboard.row('ℹ️ Інформація про мене',
                 'ℹ️ Інформація про обладнання', '💱 Курс валют')

    # Send message
    bot.send_message(
        message.chat.id, 'Вітаю, {0.first_name}!\nНатисніть відповідну кнопку 👇 щоб отримати інформацію.' .format(
            message.from_user),
        reply_markup=keyboard)


def show(message):

    # Get the message data
    message_data = message.json

    # Print the message data
    print('\n')
    for key, value in message_data.items():
        print(key, value)

    # Get the message data
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

        # Send a private message
        bot.send_message(id, message_to_reply)

        # Send a non-private message
        if message.chat.type != 'private':
            bot.send_message(chat_id, 'Відповідь у приватній розмові')

    elif message.text == 'ℹ️ Інформація про обладнання':

        keyboard = types.ReplyKeyboardMarkup(
            resize_keyboard=True)
        keyboard.row(*devices)
        keyboard.row('Назад')

        bot.send_message(
            message.chat.id, 'Оберіть пристрій:', reply_markup=keyboard)

    elif message.text in devices:

        global device_name
        device_name = message.text
        received_show_comands = get_cisco_info(device_name, 'show ?')
        commands_device = get_commands_device(received_show_comands)

        keyboard = types.ReplyKeyboardMarkup(
            resize_keyboard=True)
        i = 0
        buttons = []

        for command, description in commands_device.items():

            if i < 5:
                buttons.append(command)
                i += 1
            else:
                keyboard.row(*buttons)
                buttons = []
                i = 0

        keyboard.row('Назад')

        bot.send_message(
            message.chat.id, 'Оберіть команду:', reply_markup=keyboard)

        global tmp_commands_device
        tmp_commands_device = commands_device
        pprint(tmp_commands_device)

    elif message.text in tmp_commands_device:

        command_name = message.text
        command_description = tmp_commands_device[command_name]
        received_show_comands = get_cisco_info(
            device_name, f'show {command_name} ?')
        commands_device = get_commands_device(received_show_comands)

        print(f'{command_description}\n{received_show_comands}')
        print(len(f'{command_description}\n{received_show_comands}'))

        bot.send_message(message.chat.id, f'{
                         command_description}\n{received_show_comands}')

        get_comands_show = get_cisco_info(
            device_name, f'show {command_name} ?')
        commands_device = {}

        for row in get_comands_show.split('\n'):
            if row != '':
                command = row.split(maxsplit=1)
                command_name = command[0]
                description = command[1]
                commands_device[command_name] = description
            else:
                break

        keyboard = types.ReplyKeyboardMarkup(
            resize_keyboard=True)
        i = 0
        buttons = []

        for command, description in commands_device.items():

            if i < 5:
                buttons.append(command)
                i += 1
            else:
                keyboard.row(*buttons)
                buttons = []
                i = 0

        keyboard.row('Назад')

        bot.send_message(
            message.chat.id, 'Оберіть команду:', reply_markup=keyboard)

    #    save_tmp_show_commands(device_name, commands_device.items())
    #   tmp_commands_device = commands_device
    #   pprint(tmp_commands_device)

    # elif message.text in devices:/

    #     device_name = message.text
    #     get_comands_show = get_cisco_info(device_name, 'show ?')
    #     commands_device = []

    #     for row in get_comands_show.split('\n'):
    #         if row != '':
    #             command = row.split(maxsplit=1)
    #             command_name = command[0]
    #             description = command[1]
    #             commands_device.append({command_name: description})
    #         else:
    #             break

    #     keyboard = types.ReplyKeyboardMarkup(
    #         resize_keyboard=True)
    #     i = 0
    #     buttons = []

    #     for command, description in commands_device:

    #         if i < 5:
    #             buttons.append(list(command.items())[0][0])
    #             i += 1
    #         else:
    #             keyboard.row(*buttons)
    #             buttons = []
    #             i = 0

    #     keyboard.row('Назад')

    #     bot.send_message(
    #         message.chat.id, 'Оберіть команду:', reply_markup=keyboard)

    #     if message.text in devices:
    #         bot.send_message(
    #             message.chat.id, get_cisco_info(device_name, 'show ?'))

    #     bot.send_message(message.chat.id, get_cisco_info(device_name, f'show {} ?'))

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
