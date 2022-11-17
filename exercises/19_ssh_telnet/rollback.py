#!/usr/bin/python
#rollback.py
import netmiko
import os
from sys import argv
import time
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException 
from netmiko.ssh_exception import NetMikoAuthenticationException
import yaml



def send_config_commands(net_dev):
	ip = net_dev["host"]
	print(f"Connection to {ip}")
junos_device = netmiko
	try:
		with ConnectHandler(**net_dev) as junos_device:
			configure = junos_device.config_mode()
			setssns = junos_device.send_command("rollback 1")
			junos_device.commit(comment='Enabled NETCONF service', and_quit=True)
			junos_device.disconnect()
			return setssns
	except junos_device.ssh_exception.NetmikoTimeoutException:
		print(f"Was not able to connect to {ip} \n")
	except junos_device.ssh_exception.NetMikoAuthenticationException as error:
		print(error)
	except ValueError as error:
		print(error)
def main():
	in_fl = argv[1]
	with open(in_fl) as f:
		devices = yaml.safe_load(f)
	for dev in devices:
		send_config_commands(dev)



if __name__=='__main__':
	main()
