#!/usr/bin/python3
#Adds descriptions to the interface range on juniper switch.
from sys import argv
i_file = argv[1]
j = input('Etner 1-st interface: ')
j = int(j)
interface_template = 'set interfaces ge-0/0/{j} description {i} '
			
i = 0
with open(i_file, 'r') as f:
	for i in f:
		print(interface_template.format(j=j, i=i))
		j=j+1
