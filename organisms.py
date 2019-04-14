#!/usr/bin/env python3

import sys
import re
import pickle
#from gameclasses import livingThing

from shufflecipher import megacipher





#truemaster = set()
#typeslist = []




# produces a "set" to become the orglist that'll temporarily contain all organisms
orglist = set()

# Creates the regular expression to be used in identifying proper scientific names in the database being scraped
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

# Class given to all objects to exist in the game.
class gameObject(object):
	def __init__(self):
		self.name = name

#Class given to any living thing in the game; confers basic stats
class livingThing(gameObject):
	def __init__(self, name="Living Thing", HP = 0):
		self.name = name
		self.HP = HP
		self.alive = True
		self.safe = True
		self.listready = False
		self.truename = ""

# After livingThing, classes narrow into more specific groups that have unique traits, abilities, and roles in the game

class Animal(livingThing):
	def __init__(self):
		super().__init__()
		self.truename = ""
		self.type = ""
		self.listready = False
		self.type = "Test"
		self.truetype = ""
		self.hasatype = False


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

class Fungus(Animal):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Game Fungus"

class Fungus(Animal):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Game Fungus"

class Ascomycetes(Animal):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Game Ascomycetes"

class Fish(Animal):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Game Fish"

class Insect(Animal):
	def __init__(self):
		super().__init__()
		self.therm = "none"
		self.type = "Game Insect"


# Populates master list of organisms to be used in the game; can be later sorted
def populatemaster(masterlist):
	poptotal = []
	i = 0
	for element in masterlist:
		organism = Animal()
		organism.name = element
		organism.truename = organism.name
		poptotal.append(organism)

	for organism in poptotal:
 		megacipher(organism)


	#[print(element.name) for element in popmaster]
	return poptotal

orglist = sorted(orglist)

#print(orglist)

popmaster = populatemaster(orglist)



def scrapetypes(poplist):
	with open ('eukaryotes.txt', 'r') as file_stream:
		for line in file_stream:
			for organism in poplist:
				if organism.truename in line:
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

scrapetypes(popmaster)


#for organism in popmaster:
#	print(organism.truename, organism.type)


### DUMMY LIST TO BE USED IN DEBUGGING; CAN BE SUBSTITUTED FOR LARGER DATASET ###
somereptile = Reptile()
somereptile.type = "Reptiles"
somereptile.name = "Some Reptile"

somefrog = Amphibian()
somefrog.type = "Amphibians"
somefrog.name = "Some frog"

somefungus = Fungus()
somefungus.type = "Fungi"
somefungus.name = "Some Fungus"

secondfrog = Amphibian()
secondfrog.type = "Amphibians"
secondfrog.name = "Second Frog"

thirdfrog = Amphibian()
thirdfrog.type = "Amphibians"
thirdfrog.name = "Third Frog"

secondfungus = Fungus()
secondfungus.type = "Fungi"
secondfungus.name = "Second Fungus"

dummypop = [somereptile, somefrog, somefungus, secondfrog, thirdfrog, secondfungus]


# Assigns each organism a game class based on the Linnaean taxonomic group to which it belongs
# (And is most recognizable; e.g. "Reptile" over simply "Animal")
def givetype(poplist):
	typedict = {
	"Reptiles" : Reptile,
	"Amphibians" : Amphibian,
	"Birds" : Bird,
	"Mammals" : Mammal,
	"Fungi" : Fungus,
	"Ascomycetes" : Ascomycetes,
	"Insects" : Insect,
	"Fishes" : Fish,
	}
	

	holderlist = []
	tempnames = []
	i = 0


	### THIS WORKS NOW BECAUSE I'M INSTANTIATING EACH CLASS IN THE FOR LOOP INSTEAD OF ABOVE IN THE DICTIONARY--
	### I.E. IF YOU PUT () PARENTHESES IN THE DICTIONARY VALUES, IT ONLY INSTANTIATES EACH CLASS ONCE INSTEAD OF EACH TIME
	for org in poplist:
		holderlist.append(org)
		tempnames.append(org.name)
		for key in typedict.keys():
			if (holderlist[i].type.lower() in key.lower()):
				holderlist[i] = typedict[key]()
				holderlist[i].truename = tempnames[i]
				holderlist[i].name = tempnames[i]
				#print(holderlist[i], holderlist[i].type)
		i+=1

	return holderlist

	

#print("The length before giving types is: {0}".format(len(popmaster)))

popmaster = givetype(popmaster)


for animal in popmaster:
	print(animal.name, animal.truename, animal.type)

#print("The length after giving types is: {0}".format(len(popmaster)))

#for animal in popmaster:
#	print(animal.name, animal.type)

#print(popmaster)

#dummymaster = (givetype(dummypop))

#for animal in dummymaster:
#	print(animal.name, animal.type)

#popready = popmaster

#for organism in popmaster:
#	print(organism.name, organism.type)


#[print(organism.name, organism.type) for organism in popready]
#[print(organism.name, organism.type) for organism in popready]
#[print(organism.type) for organism in popmaster]


#populatemaster(megaorglist)




