#!/usr/bin/env python3

import sys
import re
import pickle
from gameclasses import *
from shufflecipher import *


truemaster = set()
typeslist = []
with open ('eukaryotes.txt', 'r') as file_stream:
	for line in file_stream:
		# Note: Column 5 in Eukaryotes contains the "type" (Linnaean Class) of organism
		typeslist.append(line.split('\t')[5])
		org_line = line.strip()
		org_line = org_line.replace('[', '')
		org_line = org_line.replace(']', '')
		m = compiledclean.match(org_line)
		# You could also use if !m: effectively
		if m is None:
			truemaster.add(org_line)


[print(line.split('\t')[5]) for line in truemaster]


class Animal(livingThing):
	def __init__(self):
		super().__init__()

class Reptile(Animal):
	def __init__(self):
		super().__init__()
		self.therm="ecto"

newanimal = Reptile()

print(newanimal.therm)


def populatemaster(masterlist):
	popmaster = []
	i = 0
	for element in masterlist:
		organism = Animal()
		organism.name = element
		popmaster.append(organism)

	[print(element.name) for element in popmaster]
	return popmaster


#populatemaster(megaorglist)




