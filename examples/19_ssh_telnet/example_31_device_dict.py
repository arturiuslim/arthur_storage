from pprint import pprint
import netmiko
import paramiko
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
import yaml


def send_show_command(device_params, command):
	ip = device_params["host"]
	print(f"Connection to {ip}")
	try:
		with netmiko.ConnectHandler(**device_params) as ssh:
			output = ssh.send_command(command)
			return output
	except netmiko.ssh_exception.NetmikoTimeoutException:
		print(f"Was not able to connect to {ip} \n")
	except netmiko.ssh_exception.NetMikoAuthenticationException as error:
		print(error)
	except ValueError as error:
		print(error)
	
if __name__ == "__main__":
	with open("jun_devices.yaml") as f:
		devices = yaml.safe_load(f)
	for dev in devices:
		pprint(send_show_command(dev, "show system alarms"))
