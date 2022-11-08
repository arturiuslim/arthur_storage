import paramiko
from pprint import pprint
import time
import re
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
	except paramiko.SSHException as error:
		print(f"Arised error {error} on {ip}")
		return

	with cl.invoke_shell() as ssh:
		"""
		#This part is for Cisco
		ssh.send("enable\n")
		ssh.send(f"{enable_password}\n")
		time.sleep(short_sleep)
		ssh.send("terminal length 0\n")
		output. = ssh.recv(max_read).decode("utf-8")
		prompt = re.recv(r"\S+#", output).group()
		"""
		ssh.send("\n")
		time.sleep(long_sleep)
		output = ssh.recv(max_read).decode("utf-8")
#		print("Output is: ", output)
		prompt = re.search(r"\S+>", output).group()
#		print("Prompt is: ", prompt)
		ssh.send(f"{command}\n")
		output = read_until(ssh, prompt)
		return output
	
def read_until(ssh_connect, prompt, short_sleep=0.2):
		output = ""
		ssh_connect.settimeout(3)
		while True:
			time.sleep(short_sleep)
			try:
				part = ssh_connect.recv(100).decode("utf-8")	
			except socket.timeout:
				break
			print("/"*70)
			print(part)
			output += part	
			if prompt in output:
				break
#		output = output.replace("\r\n", "\n")	#for Cisco
		return output


if __name__ == "__main__":
        u_login = input("username: ")
        u_passwd = getpass("Password: ")
#        ip_list = ["10.254.254.1", "10.254.254.2", "10.254.254.3", "10.254.254.1"]
        ip_list = [ "10.254.254.3", "10.254.254.1"]
        for ip in ip_list:
#                out = send_show_command(ip, u_login, u_passwd, "show interfaces terse | no-more")
                out = send_show_command(ip, u_login, u_passwd, "ping 10.254.254.1 count 5")
                #pprint(out, width=120)
                print("="*50)
                print(f"Checking {ip}")
                print(out)
                print("="*50)

