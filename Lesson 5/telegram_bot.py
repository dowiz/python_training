from get_token import token
import telebot

bot = telebot.TeleBot(token)
types = telebot.types

# global_sup_district = ''


def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True)  # buttons
    keyboard.row('🔍 Кнопка 1', '🗺 Кнопка 2')
    keyboard.row('🗣 ЧАТ', '🌎 Кнопка 4')

    bot.send_message(
        message.chat.id, """Вітаю, {0.first_name}!\nНатисніть відповідну кнопку 👇 щоб отримати інформацію.
            \n\n(примітка, для того щоб відобразилась повна назва кнопки, переверніть свій смартфон в горизонтальне
            положення для автоматичного повороту зображення на екрані (для користувачів з невеликими екранами))""" .format(message.from_user),
        reply_markup=keyboard)


def show(message):
    data = message.json
    username = data['from']['username']
    id = data['from']['id']
    first_name = data['from']['first_name']
    last_name = data['from']['last_name']
    chat_id = data['chat']['id']
    # text = data['text']
    message_id = message.message_id
    message_to_reply = "Message_id(" + str(message_id) + ")\nІнформація про користувача:\n\nusername: " + username + "\nid: " + \
        str(id) + "\nІм'я: " + first_name + "\nПрізвище: " + last_name

    # print(message_to_reply)
    bot.send_message(chat_id, message_to_reply)
    # print(f'message: ', data['from'])
    # print(f'message: ', data['text'])
