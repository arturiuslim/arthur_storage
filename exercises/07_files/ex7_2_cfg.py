#!/usr/bin/python3
from sys import argv

o_file = argv[1]
with open(o_file) as config_file:
	for lines in config_file:
		if not lines.startswith('!'):
			print(lines.rstrip())

