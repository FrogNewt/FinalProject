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
	def start():
		print("Please hold--we're shuffling all your organisms into the game!\n")
		popmain.shufflebegin()
		newplayer = Player()
		print("Hey--what's your name?")
		userinput = input("")
		newplayer.name = userinput
		print("######################################################################")
		print("Hi {0}!".format(newplayer.name))
		newplayer.popmaster = popmain.popmaster
		print("Oh--before we get started, we should pick a game mode!")
		input("")
		print("You can choose between 'Fixed' and 'Flex' modes:")
		input("")
		print("\t'Fixed' (default) comes pre-loaded with common daily goals.")
		input("")
		print("\t'Flex' mode allows you to choose and customize your own goals (recommended for people who trust themselves not to cheat!)")
		input("")
		gameready = False
		while gameready == False:
			print("What would you prefer? (type 'flex' or 'fixed')")
			flexchoice = input("")
			if "l" in flexchoice.lower():
				newplayer.fixed = False
				gameready = True
			elif "d" in flexchoice.lower():
				newplayer.fixed = True
				gameready = True
			else:
				print("I didn't get your choice--can you try again? (type either 'fixed' or 'flex'")
		print("Got it--we're ready to go! (Press any key to continue)")
		input("")
		return newplayer

	while True:	
		print("######################################################################")
		welcome = input("Welcome back!  Would you like to start a new game or load an existing game? ")
		if "n" in welcome.lower():
			return start()

		elif "l" in welcome.lower():
			path = "Saves/"
			filelist = []
			if os.path.exists(path):
				for item in os.listdir(path):
						if item.endswith(".pickle"):
							filelist.append(item[:-7])
			if filelist:
				while True:
					print("######################################################################")
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
				print("######################################################################")
				print("There are no saved files--starting a new game!")
				return start()
		else:
			print("Whoops--try again!")

def choosenext(self):
	while True:
		print("######################################################################")
		print("So, {0}, what would you like to do next?  You can choose from any of these:\n".format(self.name))
		for key in self.optionlist.keys():
			print(key.title())
		print("")
		usrinput = input("")
		for option in self.optionlist.keys():
			if (usrinput.lower() in option):
				print("######################################################################")
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
		self.maxHP = 10
		self.HP = 10
		self.strength = 1
		self.intellect = 1
		self.naturalism = 1
		self.happiness = 1
		self.luck = 2
		self.fixed = True
	# Links categories and related activities ("FLEX" version)
		
		if self.fixed == False:
			self.activitydict = {
			"fitness" : {}, 
			"intellect" : {}, 
			"naturalism" : {}, 
			"happiness" : {}
			}
		elif self.fixed == True:
			self.activitydict = {
			"fitness" : {"walk" : 10, "run" : 20},
			"intellect" : {"read" : 5, "wrote" : 10},
			"naturalism" : {"hiked" : 15},
			"happiness" : {"gave a compliment" : 20},
			}

	# Links categories and related activities ("FIXED" version)
		self.activitydict

	# Aggregates experience by category
		self.expdict = {"fitness" : 0, "intellect" : 0, "naturalism": 0, "happiness" : 0, "game" : 0}

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
		self.damage = 0
		self.safe = True
	
	def addtolog(self):
		if self.target not in self.naturelog:
			print("######################################################################")
			print("{0} added to your nature log!".format(self.target.name))
			self.naturelog.append(self.target)

	def attack(self):
		def setdamage(self):
			self.damage = random.randint(self.strength, self.strength + self.luck)
		setdamage(self)
		self.target.stats["HP"] -= self.damage
		print("{0} attacks the {1} for {2}!".format(self.name, self.target.name, self.damage))
		self.target.orgattack(self)

	def bound(self):
		print("######################################################################")
		print("You go bounding after something!")

		def makerandom(self):
			self.randomnum = random.randint(0, len(self.currentenv.occupants)-1)
		
		def makeboundnum(self):
			self.boundnum = random.randint(1,self.luck)
		
		#Checks whether or not the target gets super-strength as a result of your intrusion
		def checkberserk(self):
			print("Berserk test")
			if self.target.stats["Luck"] > self.boundnum:
				self.target.berserk = True
			
			self.target.berserk
			print("My boundnum:" + str(self.boundnum))
			print("Organism's luck: " + str(self.target.stats["Luck"]))

			if self.target.berserk == True:
				self.target.strength = self.target.stats["Strength"] * 2
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
	
	def checkHP(self):
		print("Your HP: " + str(self.HP))
		if self.target:
			print("Opponent HP: " + str(self.target.stats["HP"]))

	def encounter(self):
		self.safe = False
		self.target.safe = False
		self.target.stats["HP"] = self.target.stats["Max HP"]
		# Actions the player can take
		encoptions = {
		"attack it" : self.attack,
		"check HP" : self.checkHP,
		"flee" : self.flee,
		#"befriend it" : self.befriend,
		#"capture it" : self.capture
		}

		# Actions the enemy can take


		while (self.safe == False) and (self.HP > 0) and (self.target.safe == False) and (self.target.stats["HP"] > 0):
			print("######################################################################")
			print("You're facing-off against a {0}!  What do you want to do?".format(self.target.name))
			print("You can: ")
			for option in encoptions.keys():
				print(option.title())
			userinput = input("")
			for key in encoptions.keys():
				if userinput in key:
					encoptions[key]()
		if self.HP < 1:
			print("You were driven off!")
			self.HP = self.maxHP
		elif self.target.stats["HP"] < 1:
			print("You drove the {0} off!".format(self.target.name))
			self.target.stats["HP"] = self.target.maxHP
			self.target = ""



	# Allows you to engage with your current environment in different ways!
	def explorecurrent(self):
		self.brokenloop = False
		if self.currentenv:
			while self.brokenloop == False:
				print("You're currently in {0}.  What would you like to do?  You can: ".format(self.currentenv.name))
				for choice in self.envoptions.keys():
					print("\t" + choice.capitalize())
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



		print("######################################################################")
		print("It looks like you've made it to {0}!".format(self.currentenv.name))
		self.explorecurrent()



	def flee(self):
		print("You attempt to flee from the {0}!".format(self.target.name))
		luckrand = random.randint(1, self.luck)
		enemyrand = random.randint(1, self.target.stats["Luck"])
		if luckrand > enemyrand:
			print("You got away safely!")
			self.safe = True
		else:
			print("You weren't able to escape!")

		

	# General error message
	def fourohfour(self):
		print("Ooops!  That's not working yet (but if this is \'play game\' it's not supposed to work, yet)!")


	# Main method for gaining experience in the game; varies (or will vary) between flexible and fixed modes
	def getactivities(self):
		def fixedactivities(self):
			print("You're in fixed!")
			fullbreak = False
			activitygiven = False
			while True:
				activitycomplete = False
				print("######################################################################")
				greeting = print("What did you do, today? (You can also type 'list' to see the activities available or type 'quit' to quit!")
				activity = input("")
				if activity:
					activitygiven = True
				if "quit" in activity:
					self.quitsave()
				count = 0
				
				if "list" in activity.lower():
					for category in self.activitydict.keys():
						print(category.capitalize())
						for action in self.activitydict[category].keys():
							print("\t"+action.capitalize()+":"+" " +str(self.activitydict[category][action]))

				# Determines whether or not the activity has been done before
				if activitygiven:
					for category in self.activitydict.keys():
						if activity in self.activitydict[category]:
							count += 1
							print("######################################################################")
							print("Got it!")
							current = self.activitydict[category][activity]
							print("You've added {0} experience points to {1}!".format(current, category))
							self.expdict[category] += current
							activitycomplete = True
							break
					if activitycomplete == False:
						print("######################################################################")
						print("It doesn't look like that one's on the list--try typing it again (exactly as written).")
						print("If you'd prefer to customize your experience more, you can always start a game in 'flex' mode!)")
						input("")

				
				if activitycomplete == True:
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
						pass

				if fullbreak == True:
					break


		def flexactivities(self):
			print("You're in flex!")
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
							print("You've added {0} experience points to {1}!".format(current, category))
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
		if self.fixed == True:
			fixedactivities(self)
		elif self.fixed == False:
			flexactivities(self)


	def goback(self):
		self.brokenloop = True

	def look(self):
		print("You go looking for things in a reasonable way.")

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

		def makerandom(self):
			self.randomnum = random.randint(0, len(self.currentenv.occupants)-1)
		def makesitnum(self):
			self.sitnum = random.randint(1,self.luck*2)
		self.target = ""
		chosen = False
		possible = False
		print("\tYou sit and wait for something to approach you.")
		input("(Press any key to find out if something comes near!)")
		makesitnum(self)
		makerandom(self)
		occupant = self.currentenv.occupants[self.randomnum]

		# Checks to see if the player is eligible to have organisms approach
		if (self.luck*2) > self.currentenv.difficulty:
			possible = True

		if possible == True:
			if (occupant.stats["Skittishness"] > self.sitnum):
				chosen = False
			elif (occupant.stats["Skittishness"] < self.sitnum):
				chosen = True
			if chosen == True:
				self.target = occupant
				### ADD THIS IN TO THE ENCOUNTER WITH THE ORGANISM BECAUSE IT WAS ENCOUNTERED SITTING ###

				#for stat in occupant.stats:
				#	occupant.stats[stat] = occupant.stats[stat]//2
				print("\tA wild {1} cautiously appears--it looks like a {0}!".format(self.target.name, self.target.type))
				self.addtolog()
				self.encounter()
			elif chosen == False:
				print("\t...nothing.  Looks like you'll have to try again.")
		else:
			print("\tIt looks like you might need to level-up your \"luck\" stat before anything will approach you in this area!")




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


