from pprint import pprint
import re 

result_list = []

def parse_sh_ip_int_br(output):
#	regex = r"(\S+) +(\S+) +\w+ +\w+ +(up|down) +(up|down)"
	regex = (
	r"(\S+) +([\d.]+|unassigned) +"
	r"\S+ +\w+ +(\S+) +(\S+)"
	)
	result_list = []
	for line in output.split("\n"):
		m = re.search(regex, line)
		if m:	
			groups = list(m.groups())
			result_list.append(groups)
	return result_list
if __name__ == "__main__":
	with open ("sh_ip_int_br.txt", "r") as f:
		content = f.read()
		pprint(parse_sh_ip_int_br(content))
