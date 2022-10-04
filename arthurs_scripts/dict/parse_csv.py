#!/usr/bin/python3
import csv
import random
import os
from simple_term_menu import TerminalMenu
from sys import argv


infile = argv[1]
svensk = {}
with open(infile, 'r') as csv_file:
	svensk = dict(filter(None, csv.reader(csv_file)))

#######################Function block####################################

def ordlist(indict):
	not_repeat = False
	while not_repeat == False:
		loc_lst = [random.choice(list(indict))for i in range(10)]
		if len(set(loc_lst)) == 10:
			not_repeat = True
	return(loc_lst)
#####################################################################
def tmplist(inord,indict):
	not_rpt = False
	loc_trs = []
	while not_rpt == False:
		loc_lst = [random.choice(list(indict)) for i in range(3)]
		if len(set(loc_lst)) == 3 and inord not in loc_lst:
			not_rpt = True
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
	clear = lambda: os.system('clear')
	quitting = False
	print('\n', my_word, '\n')
	while quitting == False:
		optionsIndex = 	mainMenu.show()
		optionsChoice = options[optionsIndex]

		if(optionsChoice == "[q] Quit"):
			quitting = True
		else:
			if(optionsChoice == svensk.get(my_word)):
				clear()
				print(my_word, '\t', optionsChoice, '\n')
				print('\t', "det stämmer", '\n')
				quitting = True
			else:
				clear()
				print(my_word, '\t', optionsChoice, '\n')
				print('\t', "det fel", '\n')

###########################################################################
if __name__ == '__main__':
	chk_now = []
	chk_lst = ordlist(svensk)
	for i in chk_lst:
		chk_now = tmplist(i,svensk)
		dictMenu(chk_now,i)


