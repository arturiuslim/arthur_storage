#!/usr/bin/python3
import netmiko
import paramiko
from sys import argv
import yaml
from getpass import getpass
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException

def send_show_command(net_dev, comm):
	ip = net_dev["host"]
	print(f"Connection to {ip}")
	jun_dev = netmiko
	try:
                with jun_dev.ConnectHandler(**net_dev) as ssh:
                        setssns = ssh.send_command(comm)
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
	with open(in_fl) as f:
		devices = yaml.safe_load(f)
	for dev in devices:
		print(send_show_command(dev, "show interfaces ge-0/0/5 terse"))
