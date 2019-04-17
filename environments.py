#!/usr/bin/env python3

import sys
import re
import pickle
import random
from organisms import popmaster


poppop = popmaster

#for org in poppop:
#	print(org.truename, org.intername, org.meganame, org.type)


def genorgs(env, poplist):
	templist = []
	pickedlist = []
	newnum = 0
	# You'll want to use "choice" here from the builtin random module; choose(sequence) will pick something randomly from a list
	# This can be amended to operate within a range.
	for org in poplist:
		if org.mobile == True:
			templist.append(org)
	for i in range(env.animalnum):
		newchoice = random.choice(templist)
		pickedlist.append(newchoice)
			
	return pickedlist

def assignstats(env, orgs):
	pass



class basicEnv(object):
	def __init__(self):
		self.name = "A basic environment"
		pass


class startArea(basicEnv):
	def __init__(self):
		super().__init__()
		self.animalnum = 10
		self.difficulty = 1


startarea = startArea()

demolist = genorgs(startarea, poppop)

for x in demolist:
	print(x.name, x.type)


