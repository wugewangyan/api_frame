import paramiko
from datetime import  date, timedelta

def set_time(hostname):
    ssh = paramiko.SSHClient()
    # 把要连接的机器添加到known_hosts文件中
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=hostname, port=22, username='root', password='pwd@123')
    #设置两天后的时间
    afterDay = date.today() + timedelta(days=+2)

    cmd = f'date -s "{afterDay}";hwclock -w'  # 设置时间并写入bios
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stdout.read() or stderr.read()
    ssh.close()
    print(hostname, " : ", result.decode())

if __name__ == "__main__":
    host_list = '192.168.10.38'

    set_time(host_list)