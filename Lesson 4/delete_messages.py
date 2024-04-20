import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Get the token and chat ID from the environment
telegram_bot_token = os.getenv("telegram_bot_token")
chat_id = 757862717  # os.getenv("chat_id")
telegram_bot_url = f"https://api.telegram.org/bot{telegram_bot_token}/"


# Delete a message by its ID
def delete_message(message_id):
    method = "deleteMessage"
    params = f"?chat_id={chat_id}&message_id={
        message_id}&delete_chat_photo=True"  # Add delete_chat_photo parameter

    response = requests.get(telegram_bot_url + method + params).json()
    if response["ok"]:
        return "Message deleted"
    else:
        # Use single quotes for nested double quotes
        return f"Not deleted due to error: {response['error_code']}, description: {response['description']}"


# # Delete messages with IDs
# for message_id in range(110, 400):
#     print(f"Result of deleting a message with ID #{
#           message_id}: {delete_message(str(message_id))}")


def get_message(message_id):
    method = "getMessage"
    params = f"?chat_id={chat_id}&message_id={message_id}"

    response = requests.get(telegram_bot_url + method + params).json()
    print(telegram_bot_url + method + params)
    print(response)
    if response["ok"]:
        return response["result"]
    else:
        return f"Error: {response['error_code']}, description: {response['description']}"


# Get information about a message by its ID
for message_id in range(370, 500):
    print(delete_message(message_id))
