#!/usr/bin/python3

from sys import argv

i_file = argv[1]
maclist = []
vlan = argv[2]
with open(i_file) as mactbl:
	for lines in mactbl:
		if 'DYNAMIC' in lines:
			list1 = lines.split()
			list1.remove('DYNAMIC')
			maclist.append(list1)

			
for i in maclist:
	if int(vlan) == int(i[0]):
		print("{:<8} {:<20} {:<5}".format(i[0],i[1],i[2]))



