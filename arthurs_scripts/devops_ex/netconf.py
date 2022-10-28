#!/usr/bin/python3


from sys import argv
import time
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException


def enable_netconf(net_device):
	print("{} Connecting to {}".format(time.asctime(), net_device['ip']))
	junos_device = ConnectHandler(**net_device)
	configure = junos_device.config_mode("private")
	print("{}Applying configuration to {}".format(time.asctime(), net_device['ip']))
	#setssns = junos_device.send_command("set system services netconf ssh")
	setssns = junos_device.send_command("delete system services netconf")
	print("{}Commiting configuration to{}".format(time.asctime(), net_device['ip']))
	junos_device.commit(comment='Enabled NETCONF service', and_quit=True)
	print("{}Closing connection to{}".format(time.asctime(), net_device['ip']))
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
			enable_netconf(net_device)

if __name__=='__main__':
	main()
