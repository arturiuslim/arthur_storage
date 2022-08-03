#!/usr/bin/python3
import csv
import random
from simple_term_menu import TerminalMenu
from sys import argv

infile = argv[1]
svensk = {}
with open(infile, 'r') as csv_file:
	svensk = dict(filter(None, csv.reader(csv_file)))

#######################Function block####################################

def tmpdict(indict):
#Function creates temporal dictionary with 4 words
	not_repeat = False
	while not_repeat == False:
		loc_so = [random.choice(list(indict)) for i in range(4)]
		if len(set(loc_so)) == 4:
			not_repeat = True
	loc_ro = []
	for j in loc_so:
		loc_ro.append(indict.get(j))
	loc_dict = dict(zip(loc_so, loc_ro))
	nyord_loc = [random.choice(list(loc_dict))]
	return (loc_dict, loc_ro, nyord_loc)
#####################################################################
def ordlist(indict):
	not_repeat = False
	while not_repeat == False:
		loc_lst = [random.choice(list(indict))for i in range(10)]
		if len(set(loc_lst)) == 10:
			not_repeat = True
	return(loc_lst)
#####################################################################
def tmplist(inord,indict):
	not_repeat = False
	loc_trs = []
	while not_repeat == False:
		loc_lst = [random.choice(list(indict)) for i in range(3)]
		if len(set(loc_lst)) == 3:
			not_repeat = True
	for i in loc_lst:
		loc_trs.append(indict.get(i))
	loc_trs.append(indict.get(inord))
	random.shuffle(loc_trs)
	return(loc_trs)
#####################################################################

def dictMenu(my_list,my_word):
#Menu
	options = [my_list[0], my_list[1], my_list[2], my_list[3], "[q] Quit"]
	mainMenu = TerminalMenu(options)
	quitting = False
	print('\n', my_word, '\n')
	while quitting == False:
		optionsIndex = 	mainMenu.show()
		optionsChoice = options[optionsIndex]

		if(optionsChoice == "[q] Quit"):
			quitting = True
		else:
			print(svensk.get(my_word))
			if(optionsChoice == svensk.get(my_word)):
				print(my_word, '\t', optionsChoice, '\n')
				print('\t', "det stämmer", '\n')
				quitting = True
			else:
				print('\t', "det fel", '\n')

###########################################################################
chk_now = []
chk_lst = ordlist(svensk)
for i in chk_lst:
	chk_now = tmplist(i,svensk)
	dictMenu(chk_now,i)
#for i in range(10):
#	gamla_ord = []
#	newdict,ro,nyord = tmpdict(svensk)
#	if newdict != gamla_ord:
#		print(i)
#		dictMenu(ro,nyord)			
#	else:
#		newdict,ro,nyord = tmpdict(svensk)


