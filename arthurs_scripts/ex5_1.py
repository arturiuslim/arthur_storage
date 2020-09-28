#!/usr/bin/python3
###5b
import sys
london_co = {
	    "r1": {
	       "location": "21 New Globe Walk",
	       "vendor": "Cisco",
	       "model": "4451",
	       "ios": "15.4",
	       "ip": "10.255.0.1",
		    },
	    "r2": {
               "location": "21 New Globe Walk",
               "vendor": "Cisco",
               "model": "4451",
               "ios": "15.4",
               "ip": "10.255.0.2",
		    },
	    "sw1": {
               "location": "21 New Globe Walk",
               "vendor": "Cisco",
               "model": "3850",
               "ios": "3.6.XE",
               "ip": "10.255.0.101",
               "vlans": "10,20,30",
               "routing": True,
		    },
	    }

dev = input('Etner device name: ')
cp_lndn = london_co.copy()[dev]
lkeys = ', '.join(cp_lndn.keys()) 
print('Enter parameter: ', lkeys, '\n')
param = input(': ')
val = cp_lndn.setdefault(param, 'Wrong key!')
print('\n' + '-' * 30)
print(val)
