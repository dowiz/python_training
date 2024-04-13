import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Get the token and chat ID from the environment
telegram_bot_token = os.getenv("telegram_bot_token")
chat_id = os.getenv("chat_id")
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


# Delete messages with IDs
for message_id in range(110, 270):
    print(f"Result of deleting a message with ID #{
          message_id}: {delete_message(str(message_id))}")
