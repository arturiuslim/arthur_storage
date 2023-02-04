#!/usr/bin/python
#"exercise_15_1b.py"
import re
from pprint import pprint
from sys import argv

def get_ip_from_cfg(infl):
	regexp = (
		r"(interface [\S+]+)|(ip address \d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+)" #////working one
#		r"interface (?P<interface>[\S+]+)|ip address (?P<ip>\d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+)"
		)
	result_list = []
#	result_list = {}
	with open(infl) as f:
		for line in f:
			match = re.search(regexp, line)
			if match:
				"""
				### Doesn't work because of lastgroup does not catch 2 IPs
				group = match.lastgroup
				value = match.group(group)
				print(group)
				print(value)
				if group == "interface":
#					print(group)
					result_list[value] = {}
					interface = value
				elif group == "ip":
					tmp = value.split()
					value = tuple(tmp)
					result_list[interface]["ip"] = value
#					print(group)

#					print(type(value))
				"""
#//////////	Works as a list
#				print(type(match.groups()))
				if match.group(1) != None:
					result_list.append(match.group(1))
				elif match.group(2) != None:
					tmp = match.group(2).split()
					result_list.append(tuple(tmp))
#/////////////////////////////////////////////////////////////////////////////////
	return result_list

def main():
	in_fl = argv[1]
	output = get_ip_from_cfg(in_fl)
	pprint(output)

if __name__ == "__main__":
	main()
