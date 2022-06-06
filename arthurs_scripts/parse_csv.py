import csv

svensk = {}
with open('dict.csv', 'r') as csv_file:
#	csv_reader = csv.DictReader(csv_file)
	svensk = dict(filter(None, csv.reader(csv_file)))
	print(svensk.keys())
#	for line in csv_reader:
#		print(line)

