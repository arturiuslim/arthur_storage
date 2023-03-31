#!/usr/bin/python
#ex17_1.py

import re
import csv
from sys import argv
from pprint import pprint

def write_dhcp_snooping_to_csv(new_file, dhcp):
	with open(new_file, 'w') as f:
		writer = csv.writer(f)
		for row in dhcp:
			writer.writerow(row)
	

def main():
	regexp = r"([\S+]+:[\S+]+)[\s]+(\d+\.\d+\.\d+\.\d+)[\s]+[\d]+[\s]+[\S]+[\s]+[\d]+[\s]+([\S]+)"
	in_fl = argv[1]
	with open (in_fl, "r") as f:
		content = f.read()
		dhcp_out = re.findall(regexp, content)
	write_dhcp_snooping_to_csv('new_dhcp.csv', dhcp_out)

if __name__ == "__main__":
	main()

