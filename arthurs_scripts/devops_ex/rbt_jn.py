#!/usr/bin/python3

from jnpr.junos import Device
from sys import argv
from getpass import getpass
from jnpr.junos.utils.sw import SW
from jnpr.junos.exception import ConnectError

if __name__ == '__main__':
	ip = input('Hostname: ')
	lgn = input('Login:')
	psw = getpass('Password:')
	try:		
		with Device(host=ip, user=lgn, passwd=psw) as dev:
			sw = SW(dev)
			print(sw.reboot())
	except ConnectError as err:
		print(err)
