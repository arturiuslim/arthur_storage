#!/usr/bin/python3
import sys
#print(sys.argv)
in1 = input('Etner 1-st interface in the bundle: ')
in2 = input('Enter 2-nd interface in the bundle: ')
ae = input('Enter ae number')
interface_template = [ 'set interface {int1} gigether-options 802.3ad ae{ae}',
			'set interface {int2} gigether-options 802.3ad ae{ae}',
			'set interface ae{ae} agragated-ether-options lacp periodic fast']
#print(in1, in2, ae)	 
print('\n'.join(interface_template).format(int1=in1, int2=in2, ae=ae))
