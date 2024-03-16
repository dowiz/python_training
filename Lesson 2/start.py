import paramiko

users = {}


def get_traffic():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname='10.7.103.103',
                       username='python', password='python')

    stdin, stdout, stdaddr = ssh_client.exec_command(
        f"/caps-man registration-table print proplist=mac-address")

    namecolumns = list()
    columns = {}

    for item in stdout:
        if item.find('Columns:') != -1:
            for column in item.strip('Columns: ').strip().split():
                namecolumns.append(column)
        elif item.find(namecolumns[0]) != -1:
            i = 0
            for column in item.strip().split():
                columns[i] = column
                i += 1
        else:
            i = 0
            for value in item.strip().split():
                if i == 0:
                    i = 0
                else:
                    users[value] = {columns[i]: value}

                i += 1

    ssh_client.close()


get_traffic()

print(users)
