#!/usr/bin/python3
import sys
print(sys.argv)
in1 = input('Etner 1-st interface: ')
in1 = int(in1)
in2 = input('Enter last interface: ')
in2 = int(in2)
vlan0 = input('Enter native vlan number:	')
vlan0=int(vlan0)
vlan1 = input('Enter first vlan number:	')
vlan1=int(vlan1)
vlan2 = input('Enter second vlan number:	')
vlan2=int(vlan2)
interface_template = [ 
			'delete interfaces ge-0/0/{in1} disable',
			'set interfaces ge-0/0/{in1} native-vlan-id {vlan0}',
			'set interfaces ge-0/0/{in1} unit 0 family ethernet-switching interface-mode trunk',
			'set interfaces ge-0/0/{in1} unit 0 family ethernet-switching vlan members VLAN0{vlan1}_VPN01769',
			'set interfaces ge-0/0/{in1} unit 0 family ethernet-switching vlan members VLAN0{vlan2}_VPN01769',
			'set interfaces ge-0/0/{in1} unit 0 family ethernet-switching storm-control default',
			'set protocols rstp interface ge-0/0/{in1} edge',
			'set protocols rstp interface ge-0/0/{in1} no-root-port',
			'\n']
			
print(in1, in2)
i = in1
int(i)
for i in range(in2):
	for template in interface_template:
		print(template.format(in1=i, vlan0=vlan0, vlan1=vlan1, vlan2=vlan2))
