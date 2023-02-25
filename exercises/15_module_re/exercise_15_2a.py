#!/usr/bin/python
#exercise_15_2a.py

import re
from pprint import pprint
from sys import argv

def convert_to_dict(inlst, inct):
	regexp = r"(?P<interface>\S+\d)\s+(?P<address>\S+)\s+\S+\s+\S+\s+(?P<status>up|\S+ \S+)\s+(?P<protocol>\S+)"
	int_list = []
	int_dict = {}
	for line in inct.split("\n"):
		match = re.search(regexp, line)
		if match:
			int_list.append(match.groupdict())
	return(int_list)

def main():
	in_fl = argv[1]
	headers = ["interface", "address", "status", "protocol"]
	with open(in_fl, "r") as f:
		content = f.read()
		output = convert_to_dict(headers, content)	
		pprint(output)


if __name__ == '__main__':
	 main()
