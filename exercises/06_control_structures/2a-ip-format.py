#!/usr/bin/python3
import sys

addr = raw_input('Please type an ip address: ')
#if '.' not in addr:
#	print('Wrong format, tyoe again: ')
ip = addr.split('.')
#print(ip[0])
ip_ok = False
octet_ok = False

while not ip_ok:
	if len(ip) == 4 and '.' in addr :
		ip_ok = True
	else:
		print('Wrong lenght!')
		addr = raw_input('Type ip again: ')
		ip = addr.split('.')
while not octet_ok:
	for i in range(len(ip)):
		if ip[i].isdigit() and int(ip[i]) in range(256):
			octet_ok = True
		else:	
			octet_ok = False
			
			addr = raw_input('WRONG! Type ip address: ')
			ip = addr.split('.')
if ip_ok and octet_ok:
	print(len(ip))
	print('Length and format are ok')

						       

