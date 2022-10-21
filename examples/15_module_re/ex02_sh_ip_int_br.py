from pprint import pprint

result_list = []

with open ("sh_ip_int_br.txt", "r") as f:
	for line in f:
		line_list = line.split()
		if line_list and line_list[0][-1].isdigit():
			intf_ip_list = line_list[:2] + line_list[-2:]
			result_list.append(intf_ip_list)


pprint(result_list)
