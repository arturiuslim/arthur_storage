#!/usr/bin/python3
access = {'0/1': 15, '0/5': 30, '0/7':100}
access_template = ['switchport mode access',
					'switchport access vlan',
					'spanning-tree portfast',
					'spanning-tree bpduguard enable']

for intf in access:
	print('interface Fa{}'.format(intf))
	for command in access_template:
		if 'vlan' in command:
				print(command, access[intf])
		else:
				print(command)
