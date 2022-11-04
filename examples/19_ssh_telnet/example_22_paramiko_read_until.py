import paramiko
from pprint import pprint
import time
import re
import socket

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
		"""
		ssh.send("enable\n")
		ssh.send(f"{enable_password}\n")
		time.sleep(short_sleep)
		ssh.send("terminal length 0\n")
		output. = ssh.recv(max_read).decode("utf-8")
		prompt = re.recv(r"\S+#", output).group()
		"""
		ssh.send(f"{command}\n")
		prompt = re.recv(r"\S+#", output).group()
		output = ""
		ssh.timeout(3)
		while True:
			time.sleep(short_sleep)
			part = ssh.recv(100),decode("utf-f")	
			print("="*70)
			print(part)
			output += part	
			if promt in output:
				break
		output = output.replace("\r\n", "\n")
		return output


if __name__ == "__main__":
	ip_list = ["10.254.254.1", "10.10.10.1","10.254.254.2", "10.254.254.3", "10.254.254.1"]
	for ip in ip_list:
		out = send_show_command(ip, "eartlim", "Letmein123!", "show interface terse")
		pprint(out, width=120)
