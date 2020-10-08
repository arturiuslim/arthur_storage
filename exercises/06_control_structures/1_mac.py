#!/usr/bin/python3

mac_table = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

for mac in range(len(mac_table)):
	nmac = mac_table[mac].split(':')
	nmac = '.'.join(nmac)
	print(nmac)

