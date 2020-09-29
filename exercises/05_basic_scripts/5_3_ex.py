#!/usr/bin/python3
import sys
#-----------------------------------------------------
access_template = [
  "switchport mode access",
  "switchport access vlan {}",
  "switchport nonegotiate",
  "spanning-tree portfast",
  "spanning-tree bpduguard enable",
]

trunk_template = [
   "switchport trunk encapsulation dot1q",
   "switchport mode trunk",
   "switchport trunk allowed vlan {}",
]

int_tmpl = {
	'access': access_template,
	'trunk': trunk_template
	}
#------------------------------------------------------
inpt = input('Type of interface, access or trunk: ')
vlan = input('Type VLAN number: ')
intnum = input('Type interface: ')
print('\n' + '-' * 30 )

intf = int_tmpl[inpt]
conf = '\n'.join(intf)
print('Interface ', intnum)
print(conf.format(vlan))
print('\n' + '-' * 30 )
