#!/usr/bin/python3
import yaml
import os
from sys import argv
import time
#import paramiko
import netmiko
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
#from paramiko.ssh_exception import NoValidConnectionsError


def show_logs(net_device):
	jun_dev = netmiko
	try:
		with jun_dev.ConnectHandler(**net_device) as ssh:
			setssns = ssh.send_command("show interfaces ge* terse")
			return setssns
			jun_dev.disconnect()
#	except jun_dev.paramiko.ssh_exception.NoValidConnectionsError as error:
	except paramiko.ssh_exception.NoValidConnectionsError as error:
		print(f"Was not able to connect to {ip} \n")
#	except jun_dev.ssh_exception.NetmikoTimeoutException as error:
	except netmiko.ssh_exception.NetmikoTimeoutException as error:
	        print(f"Was not able to connect to {ip} \n")
	except jun_dev.ssh_exception.NetMikoAuthenticationException as error:
		print(error)
	except ValueError as error:
		print(error)


if __name__=='__main__':
	in_fl = argv[1]
	with open(in_fl) as f:
		device_list = yaml.safe_load(f)
		for device in device_list:
			logs = show_logs(device)
			print("Connection to - ...", device)
			print(logs)

