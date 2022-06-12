#!/usr/bin/python3
import csv
import random
from simple_term_menu import TerminalMenu

svensk = {}
with open('dict.csv', 'r') as csv_file:
	svensk = dict(filter(None, csv.reader(csv_file)))

#######################Function block####################################

def tmpdict(indict):
#Function creates temporal dictionary with 4 words
	loc_so = [random.choice(list(indict)) for i in range(4)]
	loc_ro = []
	for j in loc_so:
		loc_ro.append(indict.get(j))
	loc_dict = dict(zip(loc_so, loc_ro))
	nyord_loc = [random.choice(list(loc_dict))]
	return (loc_dict, loc_ro, nyord_loc)
#####################################################################

def dictMenu(my_list,my_word):
#Menu
	options = [my_list[0], my_list[1], my_list[2], my_list[3], "[q] Quit"]
	mainMenu = TerminalMenu(options)
	quitting = False
	print(my_word)
	while quitting == False:
		optionsIndex = 	mainMenu.show()
		optionsChoice = options[optionsIndex]

		if(optionsChoice == "[q] Quit"):
			quitting = True
		else:
			if(optionsChoice == svensk.get(my_word[0])):
				print(optionsChoice)
				print("det stämmer")
				my_list,my_word,tmp = tmpdict(svensk)
				dictMenu(my_word,tmp)
			else:
				print("det fel")

###########################################################################
newdict,ro,nyord = tmpdict(svensk)
dictMenu(ro,nyord)			

