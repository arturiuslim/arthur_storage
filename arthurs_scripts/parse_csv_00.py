#!/usr/bin/python3
import csv
import random
from simple_term_menu import TerminalMenu

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
nyord = [random.choice(list(tmp_dict))]
print(nyord)
#print(tmp_dict.values())
options = [ro[0], ro[1], ro[2], ro[3], "[q] Quit"]

mainMenu = TerminalMenu(options)

quitting = False

while quitting == False:
	optionsIndex = mainMenu.show()
	optionsChoice = options[optionsIndex]

	if(optionsChoice == "[q] Quit"):
		quitting = True
	else:
		if(optionsChoice == svensk.get(nyord[0])):
			print("det stämmer")
		else:
			print("det fel")
				

