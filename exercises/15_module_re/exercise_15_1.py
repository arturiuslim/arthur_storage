#!/usr/bin/python
#"exercise_15_1.py"
import re
from pprint import pprint
from sys import argv

def get_ip_from_cfg(infl):
	regexp = r"(\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)"
	result_list = []
	for line in infl.split("\n"):
		m = re.search(regexp, line)
		if m:
			groups = tuple(m.groups())
			result_list.append(groups)
	return result_list

def main():
	in_fl = argv[1]
	with open (in_fl, "r") as f:
		content = f.read()
		pprint(get_ip_from_cfg(content))


if __name__ == "__main__":
	main()
