from pprint import pprint
import re

#regex = r"^(\S+) +(\S+ [\d/]+) +.+ (\S+ [\d/]+)$"
regex = r"^(\S+) *([A-Z]\S+ [\d/]+) +.+ (\S+ [\d/]+)$"

with open("sh_cdp_n_sw1.txt") as f:
	for line in f:
		m = re.search(regex, line)
		if m:
			pprint(m.groups())

