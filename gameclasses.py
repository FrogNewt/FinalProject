#!/usr/bin/env python3

import sys
import re
import pickle

# Creates an object in-game with just a name (mostly exists just to allow for the cultivation of new fixed elements later)
class gameObject(object):
	def __init__(self):
		self.name = name


class livingThing(gameObject):
	def __init__(self, name, HP = 0):
		self.name = name
		self.HP = HP
		self.alive = True
		self.safe = True

class Actor(livingThing):
	def __init__(self, name, HP = 0, MP = 0):
		self.name = name
		self.HP = HP
		self.alive = True
		self.safe = True

class Player(Actor):
	def quitsave(self, namedfile="newgame1"):
			choice = input("Are you sure you want to quit? ")
			if "y" in choice:
				save = input("Save game? (y/n)\n")
				if "y" in save:
					print("Choose a filename! (Default is '{0}') ".format(namedfile))
					userinput = input("")
					if not userinput:
						with open(namedfile+'.pickle', 'wb') as handle:
							pickle.dump(self, handle)
							print("Game Saved to default!")
					elif userinput:	
						with open(userinput+'.pickle', 'wb') as handle:
							pickle.dump(self, handle)
							print("Game Saved!")
				else:
					print("Game not saved!")
				print("Shutting it down!")
				quit()
			else:
				pass

	def __init__(self):
		super().__init__(name = "Unknown Player")

		