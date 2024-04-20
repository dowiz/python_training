from dotenv import load_dotenv
import os
from netmiko import ConnectHandler
import time
from functions import get_device_information, get_location


# Load the environment variables
load_dotenv()

connection_location = get_location()


# Define a function to print text
def p(text):
    print(text)


# Define a function to get logs from a Cisco device
def get_cisco_info(device_name, request):

    # Get the device information
    ip, port, username, password = get_device_information(
        device_name, connection_location)

    # Define the device
    device = {
        'device_type': 'cisco_ios',
        'ip':   ip,
        'port': port,
        'username': username,
        'password': password,
        'secret': password,
    }

    # Connect to the device
    connection = ConnectHandler(**device)

    # Enter enable mode
    connection.enable()

    # Get information
    info = connection.send_command(request)

    connection.disconnect()

    return info


# devices = os.getenv('devices').split(',')

# # Get logs from each device
# for device_name in devices:
#     p(f'\nGetting logs from {device_name}...')
#     start_time = time.time()
#     logs = get_cisco_logs(device_name)
#     with open(f'storage folder/devices info/{device_name}_logs.txt', 'w') as f:
#         f.write(logs)
#     f.close()
#     p(f'Logs from {device_name} retrieved in {
#       time.time() - start_time} seconds.')
