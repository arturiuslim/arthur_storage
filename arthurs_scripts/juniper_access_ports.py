#!/usr/bin/python3
import sys
print(sys.argv)
in1 = input('Etner 1-st interface in the bundle: ')
in1 = int(in1)
in2 = input('Enter 2-nd interface in the bundle: ')
in2 = int(in2)
interface_template = [ 
			'delete interfaces ge-0/0/{} apply-groups SHUTDOWN',
			'set interfaces ge-0/0/{} unit 0 family ethernet-switching interface-mode access',
			'set interfaces ge-0/0/{} unit 0 family ethernet-switching vlan members 125',
			'set interfaces ge-0/0/{} unit 0 family ethernet-switching storm-control default',
			'set protocols rstp interface ge-0/0/{} edge',
			'set protocols rstp interface ge-0/0/{} no-root-port',
			'\n']
			
print(in1, in2)
i = in1
int(i)
for i in range(in2):
#	print(i)	
	for template in interface_template:
		print(template.format(i))
