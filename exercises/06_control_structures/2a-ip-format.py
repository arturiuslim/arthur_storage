#!/usr/bin/python3
import sys

addr = raw_input('Please type an ip address: ')
#if '.' not in addr:
#	print('Wrong format, tyoe again: ')
ip = addr.split('.')
#print(ip[0])
ip_ok = False

while not ip_ok:
	if len(ip) != 4 and '.' not in addr :
		print('Wrong lenght!')
		addr = raw_input('Type ip again: ')
		ip = addr.split('.')
	else:
		ip_ok = True

	for i in range(len(ip)):
        	if int(ip[i]) not in range(256):
			ip_ok = False	
			print('Out of range')
			addr = raw_input('Type ip address: ')
			ip = addr.split('.')
print('Length and format are ok')

						       

