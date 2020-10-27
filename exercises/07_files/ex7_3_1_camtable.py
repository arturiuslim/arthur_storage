#!/usr/bin/python3

from sys import argv

i_file = argv[1]

with open(i_file) as mactbl:
	for lines in mactbl:
#		lists = lines.split()
		if 'DYNAMIC' in lines:
			vlan, mac, _, intf = lines.split()
			print("{:8} {:20} {:5}".format(vlan, mac, intf))
