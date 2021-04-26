#!/usr/bin/python3
import sys
print(sys.argv)
in1 = input('Etner 1-st interface: ')
in1 = int(in1)
in2 = input('Enter last interface: ')
in2 = int(in2)
vlan = input('Enter vlan number')
vlan=int(vlan)
interface_template = [ 
			'delete interfaces ge-0/0/{in1} apply-groups SHUTDOWN',
			'set interfaces ge-0/0/{in1} unit 0 family ethernet-switching interface-mode access',
			'set interfaces ge-0/0/{in1} unit 0 family ethernet-switching vlan members {vlan}',
			'set interfaces ge-0/0/{in1} unit 0 family ethernet-switching storm-control default',
			'set protocols rstp interface ge-0/0/{in1} edge',
			'set protocols rstp interface ge-0/0/{in1} no-root-port',
			'\n']
			
print(in1, in2)
i = in1
int(i)
for i in range(in2):
	for template in interface_template:
		print(template.format(in1=i, vlan=vlan))
