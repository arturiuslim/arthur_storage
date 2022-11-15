#!/usr/bin/python3

import os
from sys import argv
import time
import netmiko
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException



def show_logs(net_device):
	jun_dev = netmiko
	try:
		with jun_dev.ConnectHandler(**net_device) as ssh:
			setssns = ssh.send_command("show interfaces ge* terse")
			return setssns
			jun_dev.disconnect()
	except jun_dev.ssh_exception.NetmikoTimeoutException:
	        print(f"Was not able to connect to {ip} \n")
	except jun_dev.ssh_exception.NetMikoAuthenticationException as error:
		print(error)
	except ValueError as error:
		print(error)


if __name__=='__main__':
	in_fl = argv[1]
	user_login = input('Username: ')
	user_pass = getpass('Password: ')
	with open(in_fl) as f:
		device_list = f.read().splitlines()
		for device in device_list:
			print(device)
			net_device = {
				'device_type': 'juniper',
				'ip': device,
				'username': user_login,
				'password': user_pass,
				}
			logs = show_logs(net_device)
			print("Connection to - ...", device)
			print(logs)

