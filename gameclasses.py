#!/usr/bin/env python3

import sys
import os
import re
import pickle
import organisms
from shufflecipher import *
from environments import *




def begingame():
		welcome = input("Welcome back!  Would you like to start a new game or load an existing game? ")
		if "n" in welcome.lower():
			popmain.shufflebegin()
			newplayer = Player()
			newplayer.popmaster = popmain.popmaster
			smalllist = bog.genorgs(newplayer)
			biggerlist = bog.assignstats(newplayer)
			for org in smalllist:
				for stat in org.stats:
					print(org.name, org.type, stat, org.stats[stat])
			return newplayer
		elif "l" in welcome.lower():
			path = "Saves/"
			filelist = []
			for item in os.listdir(path):
					if item.endswith(".pickle"):
						filelist.append(item[:-7])
			if filelist:
				while True:
					print("These are the available files: ")
					for item in filelist:
						print(item)
					choosefile = input("What's your filename? (Give the exact filename!) ")
					if choosefile in filelist:
						truepath = os.path.join("Saves", choosefile+".pickle")
						with open(truepath, 'rb') as handle:
							newplayer = pickle.load(handle)
							return newplayer
					else:
						print("I can't find that file!")
			else:
				print("There are no saved files--starting a new game!")
				newplayer = Player()
				popmain.shufflebegin()
				return newplayer

def choosenext(self):
	while True:
		print("What would you like to do next?  You can choose from any of these:")
		for key in self.optionlist.keys():
			print(key.title())
		usrinput = input("")
		for option in self.optionlist.keys():
			if (usrinput.lower() in option):
				self.optionlist[option]()

def shufflebegin(poplist):
	opened = organisms.openitup()
	popmaster = organisms.shuffleboth(organisms.givetype(organisms.scrapetypes(organisms.populatemaster(opened))))
	[print(thing.name, thing.type) for thing in popmaster]

	for organism in popmaster:
		organism.name = organism.meganame
	return popmaster
### TURN BACK ON AFTER DEBUGGING ###
#shufflebegin(popmaster)


# Creates an object in-game with just a name (mostly exists just to allow for the cultivation of new fixed elements later)
class Population(object):
	def __init__(self):
		self.name = "Population Master"
		self.popmaster = []
	def shufflebegin(self, poplist = ""):
		opened = organisms.openitup()
		self.popmaster = organisms.shuffleboth(organisms.givetype(organisms.scrapetypes(organisms.populatemaster(opened))))
		[print(thing.name, thing.type) for thing in self.popmaster]

class gameObject(object):
	def __init__(self):
		self.name = name

# Anything alive gets this class
class livingThing(gameObject):
	def __init__(self, name="Living Thing", HP = 1):
		self.name = name
		self.HP = HP
		self.alive = True
		self.safe = True

# A class that represents anything that can take action
class Actor(livingThing):
	def __init__(self, name, HP = 0, MP = 0):
		self.name = name
		self.HP = HP
		self.alive = True
		self.safe = True

# Captures all actions and abilities unique to the player
class Player(Actor):
	def __init__(self, name = "Unknown"):
		self.name = name
		self.popmaster = []
		
	# Links categories and related activities
		self.activitydict = {"fitness" : {"walk" : 5, "run" : 10}, "intellect" : {}, "intellect" : {}, "happiness" : {}}

	# Aggregates experience by category
		self.expdict = {"fitness" : 0, "intellect" : 0, "naturalism": 0, "happiness" : 0}

	# Creates list of all options for a player to choose
		self.optionlist = {
			"add new activities" : self.getactivities,
			"[demo] print all animals" : self.printanimals,
			"play the game" : self.fourohfour,
			"capture" : self.capture,
			"go exploring" : self.explore,
			"check my exp" : self.checkexp,
			"quit game" : self.quitsave
		}

	# Stuff the player has
		self.inventory = []
		self.gold = 0
		self.equipment = []
		self.bestiary = []

	#  Now-defunct mechanism for beginning the game
	#def opener(self):
	#	print("Hi, and welcome!")
	#	i = 0
	#	while i==0:
	#		print("What would you like to do first? (You can choose from these things: ")
	#		for key in self.optionlist.keys():
	#			print(key.title())
	#		
	#		newinput = input("")
	#		newinput = newinput.lower()
	#
	#		for thing in self.optionlist.keys():
	#			if newinput in thing:
	#				self.optionlist[thing]()
	#				i += 1
	#				break


	
	

	# Attempts to capture the current target
	def capture(self, organism):
		self.bestiary.append(organism)
		print("You've captured a wild {0}--it looks like it might be a {1}!".format(organism.name, organism.type))
		print(self.bestiary)

	# Checks to see how much experience the user has in each area
	def checkexp(self):
		print(self.expdict)

	# Go exploring in the world!
	def explore(self):
		envchoice = input("Great!  Where would you like to go?")
		

	# General error message
	def fourohfour(self):
		print("Ooops!  That's not working yet (but if this is \'play game\' it's not supposed to work, yet)!")


	# Main method for gaining experience in the game; varies (or will vary) between flexible and fixed modes
	def getactivities(self):
		fullbreak = False
		while True:
			print(self.expdict)
			greeting = print("What did you do, today? (or you can 'quit'!)")
			activity = input("")
			if "quit" in activity:
				self.quitsave()
			count = 0
			
			# Determines whether or not the activity has been done before
			while True:
				for category in self.activitydict.keys():
					if activity in self.activitydict[category]:
						count += 1
						print("You've done that one before!")
						current = self.activitydict[category][activity]
						print("{0} experience points have been added to {1}!".format(current, category))
						self.expdict[category] += current
						break
				
				# Indicates that the activity hasn't been done before
				if count == 0:
					# Assigns a quantity of experience points to your activity
					goodexp = False
					print("That's a new one--how many experience points is it worth?  (Give a number between 1 and 50!)")
					while goodexp == False:
						while True:
							activityexp = input("")
							try:
								activityexpint = int(activityexp)
								break
							except ValueError:
								print("Could not convert data to an integer--give a number between 1 and 50.")
						if (activityexpint > 50) | (activityexpint < 1):
							print("Ooops--that number won't work!  Choose an amount of exp between 1 and 50.")
						else:
							goodexp = True
					while True:
						for category in self.expdict.keys():
							print(category.title())
						print("To which category should I assign that?  You can assign it to any of the above categories:\n")
						catchoice = input("")
						catchoice = catchoice.lower()
						if catchoice in self.expdict.keys():
							self.expdict[catchoice] += activityexpint
							print("{0} exp added to {1}!".format(activityexpint, catchoice))
							self.activitydict[catchoice][activity] = activityexpint
							break
						else:
							print("Ooops--that one didn't register.  Try entering it again!")
					
					while goodexp == False:
						activityexp = input("")

					self.activitydict[catchoice.lower()][activity] = activityexpint
					

					# Assigns a category to the activity for future use
					#while True:
					#	print("To which category should I assign that exp?  You can assign it to any of the above categories:\n")
					#	catchoice = input("")
					#	catchoice = catchoice.lower()
					#	if catchoice in self.expdict.keys():
					#		self.expdict[catchoice] += activityexpint
					#		print("{0} exp added to {1}!".format(activityexpint, catchoice))
					#		self.activitydict[catchoice][activity] = activityexpint
					#		break
					#	else:
					#		print("Ooops--that one didn't register.  Try entering it again!")
				
				# Checks to see if the user wants to add more activities before moving on to the next choice
				print("One more activity?")
				endinput = input("")
				if "quit" in endinput:
					self.quitsave()
			
				if ("n" in endinput and (len(endinput) < 2)) or ("no" in endinput):
					fullbreak = True

					# Prompts user to save the game
					self.save()

					break
				
				# Returns to original question about activities (what did you do, today?)
				else:
					break

			if fullbreak == True:
				break


# Used to print out all animals and their shuffled names for debugging use
	def printanimals(self):
		for animal in self.popmaster:
			print("Current Name:" + animal.name + "\n", "True Name: " + animal.truename + "\n", "Mega-Shuffled Name: " + animal.meganame + "\n","Inter-Shuffled Name: " + animal.intername + "\n", "Type: " + animal.type + "\n")


# Used to strictly save the game (without quitting)
	def save(self, namedfile="newgame1"):
		save = input("Save game? (y/n)\n")
		if "y" in save:
			print("Choose a filename! (Default is '{0}') ".format(namedfile))
			userinput = input("")
			if not userinput:
				outdir = os.path.join(os.path.curdir, "Saves")
				print(outdir)
				if not os.path.exists(outdir):
					os.mkdir(outdir)
				# os.makedirs("my_folder1")
				path = os.path.join(outdir, namedfile+".pickle")
				print(path)
				print("wolverine")
				
				with open(path, 'wb') as handle:
					pickle.dump(self, handle)
					print("Game Saved to default!")
			elif userinput:	
				outdir = os.path.join(os.path.curdir, "Saves")
				print(outdir)
				if not os.path.exists(outdir):
					os.mkdir(outdir)
				# os.makedirs("my_folder1")
				path = os.path.join(outdir, userinput+".pickle")
				print(path)
				print("wolverine")
				with open(path, 'wb') as handle:
					pickle.dump(self, handle)
					print("Game Saved!")
		else:
			print("Game not saved!")

# Verifies that the user wants to quit and offers to save the game
	def quitsave(self, namedfile="newgame1"):
			choice = input("Are you sure you want to quit? ")
			if "y" in choice:
				self.save(namedfile)
				print("Shutting it down!")
				quit()
			else:
				pass

	

popmain = Population()





startarea = startArea()

bog = Bog()

#startorgs = genorgs(startarea, poppop)

#bogorgs = genorgs(bog, poppop)

#newlist = assignstats(startarea, startorgs)

#biggerlist = assignstats(bog, bogorgs)


