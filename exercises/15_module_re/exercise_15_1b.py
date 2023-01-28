#!/usr/bin/python
#"exercise_15_1b.py"
import re
from pprint import pprint
from sys import argv

def get_ip_from_cfg(infl):
	regexp = (
		r"(interface [\S+]+)|(ip address \d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+)"
		)
	result_list = []
	with open(infl) as f:
		for line in f:
			match = re.search(regexp, line)
			if match:
#				print(match.groups())
				if match.group(1) != None:
					result_list.append(match.group(1))
				if match.group(2) != None:
					result_list.append(match.group(2))
	return result_list

def main():
	in_fl = argv[1]
	output = get_ip_from_cfg(in_fl)
	pprint(output)

if __name__ == "__main__":
	main()
