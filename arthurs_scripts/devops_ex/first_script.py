#!/usr/bin/python3

from jnpr.junos import Device
from sys import argv
from getpass import getpass

if __name__ == '__main__':
	ip = input('Hostname: ')
	lgn = input('Login:')
	psw = getpass('Password:')
	dev = Device(host=ip, user=lgn, passwd=psw)
	dev.open()
	print(dev.facts)
	dev.close()
