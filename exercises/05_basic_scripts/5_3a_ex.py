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
int_type = {
	'access': "Enter VLAN number: ",
	'trunk': "Enter VLANs range: "
	}

#------------------------------------------------------
inpt = input('Type of interface, access or trunk: ')
print(int_type[inpt])
vlan = input()
intnum = input('Interface number: ')

print('\n' + '-' * 30 )

intf = int_tmpl[inpt]
conf = '\n'.join(intf)
print('Interface ', intnum)
print(conf.format(vlan))
print('\n' + '-' * 30 )
