import paramiko


def get_traffic():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname='10.7.103.103',
                       username='python', password='python')

    stdin, stdout, stdaddr = ssh_client.exec_command(
        f"/interface monitor-traffic interface=ether1")

    for item in stdout:
        print(item)

    ssh_client.close()


get_traffic()
