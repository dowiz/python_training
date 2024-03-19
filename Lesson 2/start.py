import paramiko
import settings

hostname = settings.hostname
port = settings.port
username = settings.username
password = settings.password
columns = {}
cap_users = {}


def get_info(request):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, port=port,
                       username=username, password=password)

    stdin, stdout, stdaddr = ssh_client.exec_command(request)

    return stdout


def get_values():
    request = "/caps-man registration-table print proplist=mac-address,uptime,bytes,packets"
    i_row = 1

    for item in get_info(request):
        if i_row == 1:
            i_row = 1
        elif i_row == 2:
            i = 0
            for column in item.strip().split():
                columns[i] = column
                i += 1
        else:
            i = 0
            for value in item.strip().split():
                if i == 0:
                    i = 0
                elif i == 1:
                    user = value
                    cap_users[user] = {columns[i]: value}
                else:
                    cap_users[user][columns[i]] = value

                i += 1

        i_row += 1


get_values()

for x in cap_users.values():
    print(x)
