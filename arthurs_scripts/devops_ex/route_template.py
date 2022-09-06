#!/usr/bin/python3

from jnpr.junos import Device
from sys import argv
from getpass import getpass

if __name__ == '__main__':
	ip = input('Hostname: ')
	lgn = input('Login:')
	psw = getpass('Password:')
	dev = Device(host=ip, user=lgn, passwd=psw)
	dev.open()
	route_xml_element = dev.rpc.get_route_information(table="inet.0")
	list_of_routes = route_xml_element.findall('.//rt')
	for route in list_of_routes:
		print("Route: {} Protocol: {}".format(route.findtext('rt-destination').strip(), route.findtext('rt-entry/protocol-name').strip()))
	dev.close()
