#!/usr/bin/env python3

import sys
import os
import re
import pickle
import organisms
import random
from shufflecipher import *
from environments import *




def begingame():
	while True:	
		welcome = input("Welcome back!  Would you like to start a new game or load an existing game? ")
		if "n" in welcome.lower():
			print("Please hold--we're shuffling all your organisms into the game!\n")
			popmain.shufflebegin()
			newplayer = Player()
			newplayer.popmaster = popmain.popmaster
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
		else:
			print("Whoops--try again!")

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
	# Fundamentals of the player
		self.name = name
		self.popmaster = []
		
	#Player Stats
		self.HP = 10
		self.strength = 1
		self.intellect = 1
		self.naturalism = 1
		self.happiness = 1
		self.luck = 1

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
			"check nature log" : self.checklog,
			"explore a new environment" : self.explorenew,
			"explore my current environment" : self.explorecurrent,
			"check my exp" : self.checkexp,
			"quit game" : self.quitsave
		}
	# Lists the possible environments available
		self.envlist = {
			"starting area" : startArea,
			"bog" : Bog,
			"swamp" : Swamp,
		}

	# Lists the options available to a player within a given environment
		self.envoptions = {
			"sit patiently and wait to be approached" : self.sit,
			"go out and carefully look for organisms" : self.look,
			"go bounding through the environment" : self.bound,
			"go back" : self.goback
		}

	# Stuff the player has
		self.inventory = []
		self.gold = 0
		self.equipment = []
		self.bestiary = []
		self.naturelog = []
	
	# Things the player may need to "hold" in order to advance the game
		self.randomnum = 0
		self.currentenv = ""
		self.currentoccupants = []
		self.target = []
		self.brokenloop = True
		self.bounded = False
		self.sat = False
		self.looked = False
		self.sitnum = 0
		self.looknum = 0
		self.boundnum = 0
	
	def addtolog(self):
		if self.target not in self.naturelog:
			print("{0} added to your nature log!".format(self.target.name))
			self.naturelog.append(self.target)

	def bound(self):
		print("You go bounding after something!")
		for org in self.currentenv.occupants:
			print(org.name, org.type)
			for stat in org.stats.keys():
				print(stat, org.stats[stat])
		def makerandom(self):
			self.randomnum = random.randint(0, len(self.currentenv.occupants)-1)
		
		def makeboundnum(self):
			self.boundnum = random.randint(1,self.luck)
		
		#Checks whether or not the target gets super-strength as a result of your intrusion
		def checkberserk(self):
			print("Berserk test")
			if self.target.luck > self.boundnum:
				self.target.berserk = True
			
			self.target.berserk
			print("My boundnum:" + str(self.boundnum))
			print("Organism's luck: " + str(self.target.luck))

			if self.target.berserk == True:
				self.target.strength = self.target.strength * 2
				print("(And it looks PISSED!)")

		self.target = ""
		chosen = False
		possible = False
		print("You bound into {0}!".format(self.currentenv.name))
		input("(Press any key to find out what you've crashed into!)")
		makeboundnum(self)
		makerandom(self)
		occupant = self.currentenv.occupants[self.randomnum]
		self.target = occupant
		
		
		

		print("You've crashed into a wild {1}--and it looks like a {0}!".format(self.target.name, self.target.type))
		
		# Assign berserk status of target
		checkberserk(self)
		
		# Add organism to nature log if yet unseen
		self.addtolog()

	# Attempts to capture the current target
	def capture(self):
		self.bestiary.append(organism)
		print("You've captured a wild {0}--it looks like it might be a {1}!".format(organism.name, organism.type))
		print(self.bestiary)

	# Checks to see how much experience the user has in each area
	def checkexp(self):
		print(self.expdict)

	def checklog(self):
		if self.naturelog:
			print("\n ### NATURE LOG ### ")
			for element in self.naturelog:
				print("Shuffled-name: " + "\t" + element.name)
				print("Type: " + element.type)
			print("\n")
		else:
			print("Your nature log is empty--go find something!")
			input("")
		
	# Allows you to engage with your current environment in different ways!
	def explorecurrent(self):
		self.brokenloop = False
		if self.currentenv:
			while self.brokenloop == False:
				print("You're currently in {0}.  What would you like to do?  You can: ".format(self.currentenv.name))
				for choice in self.envoptions.keys():
					print("\t" + choice)
				userinput = input("")
				goahead = False
				for choice in self.envoptions.keys():
					if userinput in choice:
						goahead = True
				if goahead == True:
					for choice in self.envoptions.keys():
						if userinput in choice:
							self.envoptions[choice]()
							break
				else:
					print("I didn't get that--try writing the choice exactly as it appears!")

				

		else:
			print("Ooops--you haven't chosen an environment to start with, yet!  Better go back and pick a new one, first.")
			input("")


	# Go exploring in the world!
	def explorenew(self):
		while self.currentenv:
			print("Are you sure you want to leave {0}?".format(self.currentenv.name))
			userinput = input("")
			if "y" in userinput:
				break
			elif "n":
				return
			else:
				print("I didn't get that--try again!")
		for env in self.envlist:
			print(env.title())
		self.currentenv = ""
		print("Great!  Where would you like to go? It can be anywhere listed above!")
		while True:
			userinput = input("")
			if userinput.lower() in self.envlist.keys():
				for env in self.envlist.keys():
					if userinput.lower() in env:
						self.currentenv = self.envlist[env]()
				break
			else:
				print("I didn't get that--could you try again?")
		
		currentlist = self.currentenv.genorgs(self)
		self.currentenv.occupants = self.currentenv.assignstats(currentlist)




		print("It looks like you've made it to {0}!".format(self.currentenv.name))
		print("You can see the following, here:")
		print(self.currentenv.occupants)
		for occupant in self.currentenv.occupants:
			print("Name: " + occupant.name, "\n" + "Type: " + occupant.type)
			for stat in occupant.stats.keys():
				print("\t" + str(stat) + " " + str(occupant.stats[stat]))
		self.explorecurrent()




		

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

	def goback(self):
		self.brokenloop = True

	def look(self):
		print("You go looking for things in a reasonable way.")
		for org in self.currentenv.occupants:
			print(org.name, org.type)
			for stat in org.stats.keys():
				print(stat, org.stats[stat])
		def makerandom(self):
			self.randomnum = random.randint(0, len(self.currentenv.occupants)-1)
		def makelooknum(self):
			self.looknum = random.randint(1,self.luck)
		self.target = ""
		chosen = False
		possible = False
		print("You advance into {0}!".format(self.currentenv.name))
		input("(Press any key to find out what you've encountered!)")
		makelooknum(self)
		makerandom(self)
		occupant = self.currentenv.occupants[self.randomnum]
		self.target = occupant
		# Checks to see if the player is eligible to have organisms approach
	
		print("A wild {1} appears--it looks like a {0}!".format(self.target.name, self.target.type))
		self.addtolog()

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
				if not os.path.exists(outdir):
					os.mkdir(outdir)
				# os.makedirs("my_folder1")
				path = os.path.join(outdir, namedfile+".pickle")
				
				with open(path, 'wb') as handle:
					pickle.dump(self, handle)
					print("Game Saved to default!")
			elif userinput:	
				outdir = os.path.join(os.path.curdir, "Saves")
				if not os.path.exists(outdir):
					os.mkdir(outdir)
				# os.makedirs("my_folder1")
				path = os.path.join(outdir, userinput+".pickle")
				with open(path, 'wb') as handle:
					pickle.dump(self, handle)
					print("Game Saved!")
		else:
			print("Game not saved!")

	def sit(self):
		for org in self.currentenv.occupants:
			print(org.name, org.type)
			for stat in org.stats.keys():
				print(stat, org.stats[stat])
		def makerandom(self):
			self.randomnum = random.randint(0, len(self.currentenv.occupants)-1)
		def makesitnum(self):
			self.sitnum = random.randint(1,self.luck*2)
		self.target = ""
		chosen = False
		possible = False
		print("You sit and wait for something to approach you.")
		input("(Press any key to find out if something comes near!)")
		makesitnum(self)
		makerandom(self)
		occupant = self.currentenv.occupants[self.randomnum]

		# Checks to see if the player is eligible to have organisms approach
		if (self.luck*2) > self.currentenv.difficulty:
			possible = True

		if possible == True:
			if (occupant.skit > self.sitnum):
				chosen = False
			elif (occupant.skit < self.sitnum):
				chosen = True
			if chosen == True:
				self.target = occupant
				### ADD THIS IN TO THE ENCOUNTER WITH THE ORGANISM BECAUSE IT WAS ENCOUNTERED SITTING ###

				#for stat in occupant.stats:
				#	occupant.stats[stat] = occupant.stats[stat]//2
				print("A wild {1} cautiously appears--it looks like a {0}!".format(self.target.name, self.target.type))
				self.addtolog()
			elif chosen == False:
				print("...nothing.  Looks like you'll have to try again.")
		else:
			print("It looks like you might need to level-up your \"luck\" stat before anything will approach you in this area!")




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





#startorgs = genorgs(startarea, poppop)

#bogorgs = genorgs(bog, poppop)

#newlist = assignstats(startarea, startorgs)

#biggerlist = assignstats(bog, bogorgs)


