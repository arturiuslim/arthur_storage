#!/usr/bin/python3

import os
from sys import argv
import time
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException



def show_logs(net_device):
#	print("{} Connecting to {}".format(time.asctime(), net_device['ip']))
	junos_device = ConnectHandler(**net_device)
#	setssns = junos_device.send_command("show log messages | except ssh ")
	setssns = junos_device.send_command("show interfaces ge* | display xml")
#	print("{} Closing connection to{}".format(time.asctime(), net_device['ip']))
	return setssns
	junos_device.disconnect()

def main():
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

if __name__=='__main__':
	main()
