#!/usr/bin/python
#"exercise_15_1a1.py"
import re
from pprint import pprint

def parse_cdp(output):
	regex = re.compile(
       		r"interface (?P<interface>\S+)\n"
		r".*?\n{0,3}"
		r".*?\n{0,3}"
	        r"(?P<ip>(\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+))"
	)
	result = {}
	m_all = regex.finditer(output)
#	print(m_all)
	for m in m_all:
		m_dict = (m.groupdict())
#		print(m_dict)
		interface = m_dict.pop("interface")
		result[interface] = m_dict
	return result
if __name__ == "__main__":
	with  open("config_r1.txt") as f:
		content = f.read()
	pprint(parse_cdp(content))
