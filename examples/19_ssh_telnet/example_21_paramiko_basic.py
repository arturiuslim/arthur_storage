import paramiko
from pprint import pprint
import time
import socket
from getpass import getpass

def send_show_command(ip, user, password,
		 	command,
			short_sleep=0.2,
			max_read=100000,
			long_sleep=2
):
	try:
		cl = paramiko.SSHClient()
		cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		cl.connect(
			hostname=ip,
			username=user,
			password=password,
			look_for_keys=False,
			allow_agent=False,
		)
	except socket.timeout:
		print(f"Was not able to connect tp {ip} ")
		return
	except paramiko.SSHexception as error:
		print(f"Arised error {error} on {ip}")
		return

	with cl.invoke_shell() as ssh:
		ssh.send("\n")
		time.sleep(short_sleep)
               # ssh.send("terminal length 0\n")
		ssh.send(f"{command}\n")
		time.sleep(long_sleep)
		output = ssh.recv(max_read).decode("utf-8").replace("\r\n", "\n")
		return output


if __name__ == "__main__":
	u_login = input("username: ")
	u_passwd = getpass("Password: ")
	ip_list = ["10.254.254.1", "10.254.254.2", "10.254.254.3", "10.254.254.1"]
	for ip in ip_list:
		out = send_show_command(ip, u_login, u_passwd, "show system alarm")
		#pprint(out, width=120)
		print("="*50)
		print(f"Checking {ip}")
		print(out)
		print("="*50)
