#!/usr/bin/python3
from sys import argv
#print(sys.argv)
i_file = argv[1]
in1 = input('Etner 1-st interface: ')
in1 = int(in1)
in2 = input('Enter last interface: ')
in2 = int(in2)
interface_template = 'set interfaces xe-0/0/{in10} description{f}'
			
print(in1, in2)
i = in1
int(i)
int(in1)
int(in2)
with open(i_file, 'r') as f:
	for i in range(in2):
		print(interface_template.format(in10))
#		for lines in f:
#			for template in interface_template:
#			print(i)
#			print(interface_template.format(in1=i, f=lines))
#			print(lines)
