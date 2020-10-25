#!/usr/bin/python3

from sys import argv

i_file = argv[1]

with open(i_file) as mactbl:
	for lines in mactbl:
#		lists = lines.split()
		if 'DYNAMIC' in lines:
			print(lines.rstrip())
