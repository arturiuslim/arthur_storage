#!/usr/bin/python3

from sys import argv

i_file = argv[1]
maclist = []
mc_keys = []

with open(i_file) as mactbl:
	for lines in mactbl:
		if 'DYNAMIC' in lines:
			list1 = lines.split()
			list1.remove('DYNAMIC')
			mc_keys.append(int(list1[0]))
			maclist.append(list1)

			
vlans = set(mc_keys)
mc_keys = list(vlans)
mc_keys.sort()			
for j in mc_keys:
	for i in maclist:
		if j == int(i[0]):
			print("{:<8} {:<20} {:<5}".format(i[0],i[1],i[2]))



