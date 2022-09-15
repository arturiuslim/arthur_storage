#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.fs import FS
from jnpr.junos.exception import ConnectError
from sys import argv
from getpass import getpass

#ip = input('Hostname: ')
fl = argv[1]
lgn = input('Login:')
psw = getpass('Password:')
with open(fl, 'r') as f:
	f = f.read().splitlines()
	print(f)
	for ipaddr in f:
		ip = str(ipaddr)
		try:
			with Device(host=ip, user=lgn, passwd=psw) as dev:
				print("-> Performig system cleanup on,", ip," please be patient")
				fs = FS(dev)
				print(fs.storage_cleanup_check())
		except ConnectError as err:
				print(err)
