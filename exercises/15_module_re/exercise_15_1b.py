#!/usr/bin/python
#"exercise_15_1b.py"
import re
from pprint import pprint
from sys import argv

def get_ip_from_cfg(infl):
#	regexp = r"([.\d]+)"
	regexp = (
#		r"interface [\S+]+\n"
		r"interface (?P<interface>[\S+]+)\n"
		r".*?"
#		r"(?P<ip> ip address (\d+\.\d+\.\d+\.\d+))"
		r"((\d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+))\n+"
	)
	result_list = []
	m_all = re.findall(regexp, infl, re.DOTALL)
	print(m_all)
	for m  in m_all:
#		print(m[1])
		result_list.append(m[0])
		result_list.append(m[1])
#		result_list.append(group_tp)
	return result_list

def main():
	in_fl = argv[1]
	with open (in_fl, "r") as f:
		content = f.read()
		pprint(get_ip_from_cfg(content))


if __name__ == "__main__":
	main()
