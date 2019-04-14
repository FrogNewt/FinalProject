#!/usr/bin/env python3

import sys
import re
import pickle
import random
from organisms import popmaster


poppop = popmaster

#for org in poppop:
#	print(org.truename, org.intername, org.meganame, org.type)


def assignstats(env, poplist):
	pickedlist = []
	newnum = 0
	# You'll want to use "choice" here from the builtin random module; choose(sequence) will pick something randomly from a list
	# This can be amended to operate within a range.
	for i in range(env.animalnum):
		newchoice = random.choice(poppop)
		pickedlist.append(newchoice)
	return pickedlist

		

class basicEnv(object):
	def __init__(self):
		self.name = "A basic environment"
		pass


class startArea(basicEnv):
	def __init__(self):
		super().__init__()
		self.animalnum = 10


startarea = startArea()

demolist = assignstats(startarea, poppop)

for x in demolist:
	print(x.name, x.type)