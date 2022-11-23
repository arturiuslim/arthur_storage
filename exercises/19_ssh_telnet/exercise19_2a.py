#!/usr/bin/python
import netmiko
import os
from sys import argv
import time
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
import yaml



def send_config_commands(net_dev, comlist):
	ip = net_dev["host"]
	print(f"Connection to {ip}")
	junos_device = netmiko
	try:
		with ConnectHandler(**net_dev) as junos_device:
			junos_device.config_mode('configure private')
			for com in comlist:
				junos_device.send_command(com)
			compr = junos_device.send_command_timing("show | compare")
			print(compr)			
			if compr:
				junos_device.commit()
				junos_device.disconnect()
			else:
				print("Nothing has changed \n")
				junos_device.disconnect()
			print("{} Closing connection to {}".format(time.asctime(), ip))
			junos_device.disconnect()
	except junos_device.ssh_exception.NetmikoTimeoutException:
		print(f"Was not able to connect to {ip} \n")
	except junos_device.ssh_exception.NetMikoAuthenticationException as error:
		print(error)
	except ValueError as error:
		print(error)


def main():
	in_fl = argv[1]
	commands = ['set interfaces ge-0/0/6 description test2 ', 'set interfaces ge-0/0/7 description test3', 'set interfaces ge-0/0/8 description test4 ' ] 
	with open(in_fl) as f:
		devices = yaml.safe_load(f)
	for dev in devices:
#		send_config_commands(dev,rm_int )
		send_config_commands(dev, commands)
#		print(print_compare(dev))


if __name__=='__main__':
	main()
