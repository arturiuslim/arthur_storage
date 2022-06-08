import csv
import random

svensk = {}
with open('dict.csv', 'r') as csv_file:
#	csv_reader = csv.DictReader(csv_file)
	svensk = dict(filter(None, csv.reader(csv_file)))
#	print(svensk.keys())
#	for line in csv_reader:
#		print(line)
so = [random.choice(list(svensk)) for i in range(4)]
ro = []
for i in so:
	ro.append(svensk.get(i))

tmp_dict = dict(zip(so, ro)) 
print([random.choice(list(tmp_dict))])
print(tmp_dict.values())
