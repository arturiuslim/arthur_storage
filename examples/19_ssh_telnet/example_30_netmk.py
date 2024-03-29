from pprint import pprint
import netmiko
import paramiko
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException


def send_show_command(ip, user, password, command):
	print('Connection to', ip)
	try:
		with netmiko.ConnectHandler(
			device_type="juniper_junos", timeout=5,
			host=ip, username=user, 
			password=password) as ssh:
			output = ssh.send_command(command)
			return output
	except netmiko.ssh_exception.NetmikoTimeoutException:
		print('Was not able to connect to', ip, '\n')
	except netmiko.ssh_exception.NetMikoAuthenticationException as error:
		print(error)
	except ValueError as error:
		print(error)
	
if __name__ == "__main__":
	user = input("Username: ")
	passwd = getpass("Password: ")
	ip_list = ["10.254.254.1", "10.254.254.20", "10.254.254.2"]
	for ip in ip_list:
		out = send_show_command(ip, user, passwd, "show system alarms")
		pprint(out, width=120)
