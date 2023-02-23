#!/usr/bin/python
#exercise_15_2a.py

import re
from pprint import pprint
from sys import argv

def convert_to_dict(inlst, inct):
	regexp = r"(\S+\d)\s+(\S+)\s+\S+\s+\S+\s+(up|\S+ \S+)\s+(\S+)"
	int_list = []
	int_dict = {}
	for line in inct.split("\n"):
		match = re.search(regexp, line)
		if match:
			int_dict[inlst[0]] = match.group(1)
			int_dict[inlst[1]] = match.group(2)
			int_dict[inlst[2]] = match.group(3)
			int_dict[inlst[3]] = match.group(4)
			int_list.append(int_dict)
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
