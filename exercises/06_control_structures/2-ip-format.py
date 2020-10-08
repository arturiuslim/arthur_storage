#!/usr/bin/python3
import sys

addr = raw_input('Please type an ip address: ')

ip = addr.split('.')
#print(ip[0])
if int(ip[0]) in list(range(1, 224)):
	print('Unicast')
elif int(ip[0]) in list(range(224, 240)):
	print('Multicast')
elif ip == ['255', '255', '255', '255']:
	print('Broadcast')
elif ip == ['0', '0', '0', '0']:
	print('Unassigned')
else:
	print('Unused')
#print(ip)

