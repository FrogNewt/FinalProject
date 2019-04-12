#!/usr/bin/env python3

import sys
import re
import pickle
from gameclasses import *
#from shufflecipher import *


truemaster = set()
typeslist = []





orglist = set()

cleanup = r"^[A-Z].+$"

compiledclean = re.compile(cleanup)


#temporglist = []
with open('scientificnames.txt', 'r') as file_stream:
	for line in file_stream:
		org_line = line.strip()
		org_name = org_line.split('\t')[0]
		#org_type = org_line.split('\t')[5]
		#temporglist.append(org_name)
		org_name = org_name.replace('[', '')
		org_name = org_name.replace(']', '')
		org_name = org_name.replace(' sp.', '')
		m = compiledclean.match(org_name)
		# You could also use if !m: effectively
		if m:
			#print(line)
			orglist.add(org_name)
			

# Reads the fifth column in a tab-delimited line
#[print(line.split('\t')[5]) for line in truemaster]


class Animal(livingThing):
	def __init__(self):
		super().__init__()
		self.truename = ""
		self.type = ""
		self.listready = False

class Reptile(Animal):
	def __init__(self):
		super().__init__()
		self.therm = "ecto"
		self.type = "Game Reptile"

class Amphibian(Animal):
	def __init__(self):
		super().__init__()
		self.therm = "ecto"
		self.type = "Game Amphibian"

class Bird(Animal):
	def __init__(self):
		super().__init__()
		self.therm = "endo"
		self.type = "Game Bird"

class Mammal(Animal):
	def __init__(self):
		super().__init__()
		self.therm = "endo"
		self.type = "Game Mammal"

newanimal = Reptile()



def populatemaster(masterlist):
	popmaster = []
	i = 0
	for element in masterlist:
		organism = Animal()
		organism.name = element
		organism.truename = organism.name
		popmaster.append(organism)

	#[print(element.name) for element in popmaster]
	return popmaster

orglist = sorted(orglist)

#print(orglist)

popmaster = populatemaster(orglist)


with open ('eukaryotes.txt', 'r') as file_stream:
	for line in file_stream:
		for organism in popmaster:
			if organism.name in line:
				organism.type = line.split('\t')[5]

		# Note: Column 5 in Eukaryotes contains the "type" (Linnaean Class) of organism
		#typeslist.append(line.split('\t')[5])
		#org_line = line.strip()
		#org_line = org_line.replace('[', '')
		#org_line = org_line.replace(']', '')
		#m = compiledclean.match(org_line)
		# You could also use if !m: effectively
		#if m is None:
			#truemaster.add(org_line)




#for organism in popmaster:
#	print(organism.truename, organism.type)

popready = []

def givetype(poplist):
	typedict = {
	"Reptiles" : Reptile(),
	"Amphibians" : Amphibian(),
	"Birds" : Bird(),
	"Mammals" : Mammal()
	}
	

	templist = []
	tempname = ""

	for organism in poplist:
		for key in typedict.keys():
			if key==organism.type:
				tempname = organism.name
				organism = typedict[key]
				organism.name = tempname
				print(organism.name, organism.type)

			




					


				


				
				#print(organism.name, organism.type)



givetype(popmaster)


#[print(organism.name, organism.type) for organism in popready]
[print(organism.name, organism.type) for organism in popready]
#[print(organism.type) for organism in popmaster]


#populatemaster(megaorglist)




