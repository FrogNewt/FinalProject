#!/usr/bin/env python3

import sys
import re
import pickle
import random
#from gameclasses import popmain


#poppop = popmain.popmaster

#for org in poppop:
#	print(org.truename, org.intername, org.meganame, org.type)


def genorgs(env, player):
	templist = []
	pickedlist = []
	newnum = 0
	# You'll want to use "choice" here from the builtin random module; choose(sequence) will pick something randomly from a list
	# This can be amended to operate within a range.
	for org in player.popmaster:
		if org.mobile == True:
			templist.append(org)
	for i in range(env.animalnum):
		newchoice = random.choice(templist)
		pickedlist.append(newchoice)
			
	return pickedlist

def assignstats(env, player):
	statorgs = []
	for org in player.popmaster:
		if org not in statorgs:
			statorgs.append(org)
			for stat in org.stats.keys():
				org.stats[stat] = org.stats[stat] * (random.randint((env.difficulty-2 if (env.difficulty-2 > 0) else 1), env.difficulty))
		if org.power:
			org.poweron()
	return statorgs




class basicEnv(object):
	def __init__(self):
		self.name = "A basic environment"
		self.difficulty = 1
		self.animalnum = 10
		self.occupants = []
		self.hasaquatics = False

	def genorgs(self, player):
		templist = []
		pickedlist = []
		newnum = 0
		# You'll want to use "choice" here from the builtin random module; choose(sequence) will pick something randomly from a list
		# This can be amended to operate within a range.
		for org in player.popmaster:
			if org.mobile == True:
				if (self.hasaquatics == False) and ((org.type == "Amphibian") or (org.type == "Fish")):
					pass
				else:
					templist.append(org)
		for i in range(self.animalnum):
			newchoice = random.choice(templist)
			pickedlist.append(newchoice)
				
		return pickedlist

	def assignstats(self, genlist):
		statorgs = []
		for org in genlist:
			if org not in statorgs:
				statorgs.append(org)
				for stat in org.stats.keys():
					org.stats[stat] = org.stats[stat] * (random.randint((self.difficulty-3 if (self.difficulty-2 > 0) else 1), self.difficulty))
			if org.power:
				org.poweron()
		return statorgs

class aquaEnv(basicEnv):
	def __init__(self):
		self.name = "a basic aquatic environment"
		self.difficulty = 1
		self.animalnum = 10
		self.hasaquatics = True


class Meadow(basicEnv):
	def __init__(self):
		super().__init__()
		self.name = "an inviting meadow"

class Bog(aquaEnv):
	def __init__(self):
		super().__init__()
		self.animalnum = 15
		self.difficulty = 5
		self.name = "a bog"

class Swamp(aquaEnv):
	def __init__(self):
		super().__init__()
		self.animalnum = 20
		self.difficulty = 7
		self.name = "a swamp"

class Forest(basicEnv):
	def __init__(self):
		super().__init__()
		self.name = "an expansive forest"
		self.difficulty = 10
		self.animalnum = 25

class Plain(basicEnv):
	def __init__(self):
		super().__init__()
		self.name = "rolling plains"
		self.difficulty = 12
		self.animalnum = 30

class darkForest(basicEnv):
	def __init__(self):
		super().__init__()
		self.name = "a dark and ominous forest"
		self.difficulty = 20
		self.animalnum = 40




#startarea = startArea()

#bog = Bog()

#startorgs = genorgs(startarea, poppop)

#bogorgs = genorgs(bog, poppop)

#newlist = assignstats(startarea, startorgs)

#biggerlist = assignstats(bog, bogorgs)

#for x in biggerlist:
#	for stat in x.stats.keys():
#		print(x.name, x.type, (stat, x.stats[stat]))


