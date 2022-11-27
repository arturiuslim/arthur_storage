#!/usr/bin/python
#"exercise_15_1a.py"
import re
from pprint import pprint
from sys import argv

def get_ip_from_cfg(infl):
#	regexp = r"([.\d]+)"
	regexp = (
		r"interface (?P<interface>[\S+]+)\n"
		r".*?\n{0,3}"
		r"(?P<ip>(\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+))"
	)
	result_list = {}
	m_all = re.finditer(regexp, infl)
	for m  in m_all:
		m_dict = (m.groupdict())
		intr = m_dict.pop("interface")
		result_list[intr] = m_dict
	return result_list

def main():
	in_fl = argv[1]
	with open (in_fl, "r") as f:
		content = f.read()
		pprint(get_ip_from_cfg(content))


if __name__ == "__main__":
	main()
