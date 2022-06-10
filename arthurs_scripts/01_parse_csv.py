#!/usr/bin/python3
import csv
import random
from simple_term_menu import TerminalMenu

svensk = {}
with open('dict.csv', 'r') as csv_file:
	svensk = dict(filter(None, csv.reader(csv_file)))

#so = [random.choice(list(svensk)) for i in range(4)]
#ro = []
#for i in so:
#	ro.append(svensk.get(i))
#tmp_dict = dict(zip(so, ro)) 
#nyord = [random.choice(list(tmp_dict))]
#print(nyord)

def tmpdict(indict):
	loc_so = [random.choice(list(indict)) for i in range(4)]
	loc_ro = []
	for j in loc_so:
		loc_ro.append(indict.get(j))
	loc_dict = dict(zip(loc_so, loc_ro))
	nyord_loc = [random.choice(list(loc_dict))]
	return (loc_dict, loc_ro, nyord_loc)

newdict,ro,nyord = tmpdict(svensk)
print(nyord)

#options = [ro[0], ro[1], ro[2], ro[3], "[q] Quit"]
#mainMenu = TerminalMenu(options)
#quitting = False
#
#while quitting == False:
#	optionsIndex = mainMenu.show()
#	optionsChoice = options[optionsIndex]
#
#	if(optionsChoice == "[q] Quit"):
#		quitting = True
#	else:
#		if(optionsChoice == svensk.get(nyord[0])):
#			print(optionsChoice)
#			print("det stämmer")
#		else:
#			print("det fel")

def dictMenu(my_list,my_word):
	options = [my_list[0], my_list[1], my_list[2], my_list[3], "[q] Quit"]
	mainMenu = TerminalMenu(options)
	quitting = False

	while quitting == False:
		optionsIndex = 	mainMenu.show()
		optionsChoice = options[optionsIndex]

		if(optionsChoice == "[q] Quit"):
			quitting = True
		else:
			if(optionsChoice == svensk.get(my_word[0])):
				print(optionsChoice)
				print("det stämmer")
			else:
				print("det fel")

dictMenu(ro,nyord)			

