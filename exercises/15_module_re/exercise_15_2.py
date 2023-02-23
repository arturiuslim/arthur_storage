#!/usr/bin/python
#exercise_15_2.py

import re
from pprint import pprint
from sys import argv

def parse_sh_ip_int_br(intfl):
	regexp = r"(\S+\d)\s+(\S+)\s+\S+\s+\S+\s+(up|\S+ \S+)\s+(\S+)"
	output = re.findall(regexp, intfl)
	return output

def main():
	in_fl = argv[1]
	with open (in_fl, "r") as f:
		content = f.read()
		pprint(parse_sh_ip_int_br(content))

if __name__  == "__main__":
	main()
