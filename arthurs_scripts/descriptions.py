#!/usr/bin/python3
import sys
print(sys.argv)
in1 = input('Etner 1-st interface: ')
in1 = int(in1)
in2 = input('Enter last interface: ')
in2 = int(in2)
interface_template = [ 
			'set interfaces xe-0/0/{in1} description ']
			
print(in1, in2)
i = in1
int(i)
for i in range(in2):
	for template in interface_template:
		print(template.format(in1=i))
