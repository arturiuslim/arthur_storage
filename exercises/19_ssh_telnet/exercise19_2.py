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
			junos_device.send_config_set(comlist)
#			setssns = junos_device.send_command("show | compare")
#			print(setssns)
			print("{} Commiting configuration to{}".format(time.asctime(), ip))
			junos_device.commit(comment='ge-0/0/7 and ge-0/0/8 famili inet and iso added', and_quit=True)
			print("{} Closing connection to{}".format(time.asctime(), ip))
			junos_device.disconnect()
#			return setssns
	except junos_device.ssh_exception.NetmikoTimeoutException:
		print(f"Was not able to connect to {ip} \n")
	except junos_device.ssh_exception.NetMikoAuthenticationException as error:
		print(error)
	except ValueError as error:
		print(error)
def main():
	in_fl = argv[1]
	commands = ['set interfaces ge-0/0/7 unit 0 family inet', 
			'set interfaces ge-0/0/7 unit 0 family iso', 
			'set interfaces ge-0/0/8 unit 0 family inet', 
			'set interfaces ge-0/0/8 unit 0 family iso']
	rm_int = ['delete interfaces ge-0/0/7 unit 0 ',
			'delete interfaces ge-0/0/8 unit 0 ']
	with open(in_fl) as f:
		devices = yaml.safe_load(f)
	for dev in devices:
#		send_config_commands(dev,rm_int )
		send_config_commands(dev, commands)



if __name__=='__main__':
	main()
