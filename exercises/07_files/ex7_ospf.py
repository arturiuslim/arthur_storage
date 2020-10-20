#!/usr/bin/python3
keys1 = ['Prefix', "AD/Metric", 'Next-Hop', 'Last update', 'Outbound Interface']

with open('ospf.txt', 'r') as file_ospf:
	for line1 in file_ospf:
		list1 = line1.split()
		list1.pop(3)
		list1.pop(0)
		list1[1] = list1[1].strip('[]')
		dict1 = {}
		for keys in keys1:
			for itm in list1:
				dict1[keys] = itm
				list1.remove(itm)
				break
		print('/'*30)
		for key, value in dict1.items():	
			print("{:20} {:20}".format(key, value))

