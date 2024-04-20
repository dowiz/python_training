import os


# Get the devices from the environment variables
def get_devices():
    devices = os.getenv('devices')
    print(devices)
    devices = devices.split(',')

    return devices


# Get the location from the environment variables
def get_location():
    location = os.getenv('connection_location')

    return location


# Get the device information from the environment variables
def get_device_information(device_name, connection_location):

    remote_host = os.getenv(f'{device_name}.{connection_location}.host')
    remote_port = os.getenv(f'{device_name}.{connection_location}.port')
    specify_user = os.getenv(f'{device_name}.{connection_location}.user')
    password = os.getenv(f'{device_name}.{connection_location}.password')

    return remote_host, remote_port, specify_user, password


def get_commands_device(received_show_comands):

    commands_device = {}

    for row in received_show_comands.split('\n'):
        print(f'row.strip(): \'{row.strip()}\'')
        if row.strip() == '<cr>':
            print('Умова спрацювала \'<cr>\'')
            continue

        elif row != '':
            command = row.split(maxsplit=1)
            command_name = command[0]
            description = command[1]
            commands_device[command_name] = description

        else:
            break

    return commands_device


def save_tmp_show_commands(device_name, commands_device):
    os.environ[f'{device_name}.tmp_show_commands'] = commands_device
