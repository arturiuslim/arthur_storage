from pprint import pprint
import netmiko
import paramiko
from getpass import getpass

def send_show_command(ip, user, password, command):
	print(f"Connection to {ip}")
	try:
		with netmiko.ConnectHandler(
			device_type="junos", timeout=5,
			host=ip, username=user, 
			password=password) as ssh:
			output = ssh.send_command(command)
			return output
	except netmiko.ssh_exception.NetmikoTimeoutExceptiom:
		print(f"Was nat able to connect to {ip}")
	except netmiko.ssh_exception.NetmikoAuthentiacationException as error:
		print(error)
	
if __name__ == "__main__":
	user = input("Username: ")
	passwd = getpass("Password: ")
	ip_list = ["10.254.254.1", "10.254.254.20", "10.254.254.2"]
	for ip in ip_list:
		out = send_show_command(ip, user, passwd, "show system alarms")
		pprint(out, width=120)
