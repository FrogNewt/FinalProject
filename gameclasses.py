#!/usr/bin/env python3

import sys
import os
import re
import pickle
import organisms
import random
from shufflecipher import *
from environments import *
import pygame
import time





def begingame():
	def start():
		#pygame.mixer.init()
		#pygame.mixer.music.load('woodfrog.wav')
		#pygame.mixer.music.play()

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
		soundready = False
		while soundready == False:
			print("One last thing--would you like to begin with sound 'on' or 'off'?")
			soundinput = input("")
			if "n" in soundinput:
				print("Sound on!")
				import pygame
				newplayer.soundon = True
				soundready = True
			elif "f" in soundinput:
				print("Sound off!")
				newplayer.soundon = False
				soundready = True
			else:
				print("I didn't get that--try again!")
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
		ready = False
		usrinput = input("")
		for option in self.optionlist.keys():
			if (usrinput) and (usrinput.lower() in option):
				print("######################################################################")
				self.optionlist[option]()
				ready = True
		if ready == False:
			print("Ooops--didn't get that!")


def shufflebegin(poplist):
	opened = organisms.openitup()
	popmaster = organisms.shuffleboth(organisms.givetype(organisms.scrapetypes(organisms.populatemaster(opened))))
	

	for organism in popmaster:
		organism.name = organism.meganame
	return popmaster
### TURN BACK ON AFTER DEBUGGING ###
#shufflebegin(popmaster)


# Creates an object in-game with just a name (mostly exists just to allow for the cultivation of new fixed elements later)
class gameObject(object):
	def __init__(self):
		self.name = name


# Used in generating the initial population list
class Population(gameObject):
	def __init__(self):
		self.name = "Population Master"
		self.popmaster = []
	def shufflebegin(self, poplist = ""):
		opened = organisms.openitup()
		self.popmaster = organisms.shuffleboth(organisms.givetype(organisms.scrapetypes(organisms.populatemaster(opened))))




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
		
	# Player Stats (Unaccessed during gameplay after initialization)
		self.maxHP = 10
		self.HP = 10
		self.strength = 1
		self.intellect = 1
		self.naturalism = 1
		#self.happiness = 1
		self.luck = 50
		self.fixed = True
		self.soundon = True

	# USABLE Player stats--reference these in combat/interactions (rather than the originals)
		self.stats = {
		"HP" : self.HP,
		"Max HP" : self.maxHP,
		"Strength" : self.strength,
		"Intellect" : self.intellect,
		"Naturalism" : self.naturalism,
		"Luck" : self.luck
		}
	# Links categories and related activities ("FLEX" version)
		
		if self.fixed == False:
		# Sets categories to be used (empty) for flex mode for leveling-up
			self.activitydict = {
			"fitness" : {}, 
			"intellect" : {}, 
			"naturalism" : {}, 
			"happiness" : {}
			}
		elif self.fixed == True:
		# Sets activities to be included in "fixed" mode for leveling-up
			self.activitydict = {
			"fitness" : {
				"walked" : 10, 
				"jogged" : 20,
				"swam" : 25,
				"ate healthy" : 10,
				"worked-out": 30,
				"ran a marathon" : 50,
				"slept well" : 10
				},
			"intellect" : {
				"read a paper" : 20, 
				"worked on manuscript" : 30,
				"learned a skill" : 20,
				"taught someone" : 15,
				"learned something interesting" : 5,
				"met with a professor" : 15
			},
			"naturalism" : {
				"hiked" : 25,
				"identified a wild organism" : 10,
				"collected litter" : 5,
				"watered plants" : 10,
				"planted something" : 40,
				"spent time outdoors" : 10
				},
			"happiness" : {
				"gave a compliment" : 20,
				"ate something delicious" : 15,
				"helped someone" : 25,
				"kept my cool" : 30,
				"gave a gift" : 35,
				"offered help" : 5,
				"meditated" : 20,
				"played with a pet" : 25
			},
			}

	# Links experience categories to stat categories
		self.statexpdict = {
		"fitness" : "Strength",
		"fitness2" : "Max HP",
		"intellect" : "Intellect",
		"happiness" : "Luck",
		"naturalism" : "Naturalism"

		}

	# Aggregates experience by category

		self.expdict = {"fitness" : 0, "intellect" : 0, "naturalism": 0, "happiness" : 0, "game" : 0}

	# Creates list of all options for a player to choose
		self.optionlist = {
			"add new activities" : self.getactivities,
			#"[demo] print all animals" : self.printanimals,
			"set companion" : self.setcompanion,
			"examine companion" : self.examinecompanion,
			"breed organisms" : self.breed,
			"check nursery" : self.checknursery,
			#"play the game" : self.fourohfour,
			#"capture" : self.capture,
			"check stats" : self.checkstats,
			"check inventory" : self.checkinventory,
			"examine bestiary" : self.examinebestiary,
			"feed companion" : self.feedcompanion,
			"check nature log" : self.checklog,
			"explore a new environment" : self.explorenew,
			"explore my current environment" : self.explorecurrent,
			"check my exp" : self.checkexp,
			"toggle sound" : self.togglesound,
			"quit game" : self.quitsave
		}



	# Lists the possible environments available
		self.envlist = {
			"meadow" : Meadow,
			"bog" : Bog,
			"swamp" : Swamp,
			"forest" : Forest,
			"plains" : Plain,
			"dark forest" : darkForest
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
		self.nursery = []
		self.companion = ""
		self.formercompanion = ""
	
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
		self.previoustarget = ""
		self.tempenemy = self
		self.excludestats = ["Max HP", "Gold", "Exp"]

	# For breeding organisms
		self.dam = ""
		self.sire = ""
	
	def addtolog(self):
		if self.target not in self.naturelog:
			print("######################################################################")
			print("{0} (a {1}) added to your nature log!".format(self.target.name, self.target.type))
			self.naturelog.append(self.target)

	def attack(self):
		def setdamage(self):
			self.damage = random.randint(self.stats["Strength"], self.stats["Strength"] + self.stats["Luck"])
		setdamage(self)
		self.target.stats["HP"] -= self.damage
		print("{0} attacks the {1} for {2}!".format(self.name, self.target.name, self.damage))

	def befriend(self):
		targetindex = (self.target.stats["Skittishness"] + self.target.stats["Luck"]) // 2
		playerindex = (self.stats["Naturalism"] + self.stats["Luck"]) // 2
		print("You attempt to befriend the {0}!".format(self.target.name))
		input("")
		if targetindex >= playerindex:
			print("You failed--the {0} isn't having it!".format(self.target.name))
		elif targetindex < playerindex:
			print("You did it--you've befriended the {0}!  It follows you into the bestiary!".format(self.target.name))
			if self.bounded == True:
				randnum = random.randint(1,3)
				if randnum == 1:
					print("Looks like bounding after this thing weakened it...that happens sometimes.")
					for stat in self.target.stats.keys():
						self.target.stats[stat] = self.target.stats[stat] - 2
						if self.target.stats[stat] < 1:
							self.target.stats[stat] = 1
					self.bounded = False
			elif self.sat == True:
				randnum = random.randint(1,10)
				if randnum == 1:
					print("Looks like your caution paid off--because this one didn't panic, it has elevated stats!")
					for stat in self.target.stats.keys():
						self.target.stats[stat] = self.target.stats[stat] + 3
				self.sat = False
			self.bestiary.append(self.target)
			self.currentenv.occupants.pop(self.currentenv.occupants.index(self.target))
			self.safe = True
			if not self.companion:
				self.companion = self.target
				self.bestiary.pop(self.bestiary.index(self.companion))
				print("{0} has been set as your companion!".format(self.companion.name))

	def bound(self):
		self.bounded = True
		print("######################################################################")
		print("You go bounding after something!")
		if not self.currentenv.occupants:
			print("There's nothing here...try another environment!")
			return

		def makerandom(self):
			self.randomnum = random.randint(0, len(self.currentenv.occupants)-1)
		
		def makeboundnum(self):
			self.boundnum = random.randint(1,self.stats["Luck"])
		
		#Checks whether or not the target gets super-strength as a result of your intrusion
		def checkberserk(self):
			if self.target.stats["Luck"] > self.boundnum:
				self.target.berserk = True

			if self.target.berserk == True:
				self.target.stats["Strength"] = self.target.stats["Strength"] * 2
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
		self.encounter()

	# Attempts to capture the current target
	#def capture(self):
		#self.bestiary.append(organism)
		#print("You've captured a wild {0}--it looks like it might be a {1}!".format(organism.name, organism.type))
		#print(self.bestiary)
		pass

	def breed(self):
		if not self.nursery:
			self.excludestats = ["Max HP", "Gold", "Exp"]

			class Typeholder(object):
				def __init__(self):
					self.type = ""
					self.females = 0
					self.males = 0
					self.ready = False

			breedready = False
			typeset = set()

			typeholderlist = []
			if self.bestiary:
				for org in self.bestiary:
					typeset.add(org.type)
			else:
				print("You don't have anything in your bestiary...yet!")
				return
			for orgtype in typeset:
				reptype = Typeholder()
				reptype.type = orgtype
				for org in self.bestiary:
					if org.type == reptype.type:
						if org.sex == "female":
							reptype.females += 1
						elif org.sex == "male":
							reptype.males += 1
				print(reptype.type + ":" + str(reptype.males) + " males, " + str(reptype.females) + " females")
				if (reptype.males > 0) and (reptype.females > 0):
					typeholderlist.append(reptype)
					reptype.ready = True
					breedready = True
			if breedready == False:
				print("You don't have enough males and females of a given type who aren't related, yet!")
				return
			


			readyfemales = []
			readymales = []
			femindex = 0
			mindex = 0
			matingdone = False
			if matingdone == False:
				femalechosen = False
				while femalechosen == False and breedready == True:
					if breedready == True:
						print("######################################################################")
						print("Remember, you can only breed two organisms at a time!")
						print("Which female would you like to breed?")
						for typeholder in typeholderlist:
							if typeholder.ready == True:
								for org in self.bestiary:
									if org.type == typeholder.type:
										if org.sex == "female":
											org.index = femindex
											readyfemales.append(org)
											femindex += 1
											print("Name: " + org.name)
											print("Type: " + org.type)
											print("Index: " + str(org.index))
											if org.damID:
												print("Dam ID: " + str(org.damID))
											if org.babyID:
												print("Baby ID: " + str(org.babyID))
											for stat in org.stats.keys():
												if stat not in self.excludestats:
													print(stat, org.stats[stat])
											print("\n")
								print("\n")
						print("Which female would you like to breed? (Available females are listed above--you can also type 'leave')")
						userfemale = input("")
						if "leave" in userfemale:
							print("Ok--leaving the breeding area.")
							return
						for org in readyfemales:
							if (userfemale == org.name) or (userfemale == str(org.index)):
								self.dam = org
								femalechosen = True
						if not self.dam:
							print("Ooops--didn't get that!  Try again.")

				malechosen = False
				while malechosen == False:
					print("######################################################################")
					for org in self.bestiary:
						if org.type == self.dam.type:
							if org.sex == "male":
								readymales.append(org)
								org.index = mindex
								mindex += 1
								print("Name: " + org.name)
								print("Type: " + org.type)
								print("Index: " + str(org.index))
								for stat in org.stats.keys():
									if stat not in self.excludestats:
										print(stat, org.stats[stat])
								print("\n")
					while malechosen == False:
						print("Which male would you like to breed? (Available males are listed above--you can also type leave)")
						usermale = input("")
						if "leave" in usermale:
							print("Ok--leaving the breeding area.")
							return
						if usermale:
							for org in readymales:
								if (usermale == org.name) or (usermale == str(org.index)):
									self.sire = org
									malechosen = True
									break
						if malechosen == False:
							print("I didn't get that--can you enter the male's ID again?")


					print("Got it--you want to breed {0} ({1}) with {2} ({3})!".format(self.dam.name, self.dam.sex, self.sire.name, self.sire.sex))
					print("This baby won't be ready until tomorrow--are you sure you want to lose access to these two parents until then?")
					userwait = input("")
					if "y" in userwait:
						print("Ok--check back tomorrow!")
						self.dam.matedtime = str(time.ctime())
						self.dam.matedtime = self.dam.matedtime.split()[3]
						self.dam.matedtime = self.dam.matedtime.split(":")[1]
						self.bestiary.pop(self.bestiary.index(self.dam))
						self.bestiary.pop(self.bestiary.index(self.sire))
						self.nursery.append(self.dam)
						self.nursery.append(self.sire)
						matingdone = True
						
					else:
						print("Leaving the breeding area!")
						return


				if matingdone == False:
					print("I didn't get that--type the index or the name of the individual you're wanting to breed.")

				

			else:
				print("You don't have a male and female pair of any one type, yet!")
				return

		else:
			print("You've already got a pair of parents in the nursery--they'll have to finish-up before you can breed anyone else!")


		





	# Checks to see how much experience the user has in each area
	def checkexp(self):
		for thing in self.expdict.keys():
			print(thing + ": " + str(self.expdict[thing]))

	def checkinventory(self):
		if self.inventory:
			print("Here's what you have in your inventory right now:")
			for element in self.inventory:
				print("\t" + element.name.capitalize())
		else:
			print("You don't have anything in your inventory right now.")

	def checknursery(self):
		if not self.nursery:
			print("Your nursery is currently empty--come back after you've bred two adults of the same type!")
			return
		
	# Splits ctime output to produce an element of the current time (e.g. day, month, hour, etc)
		checktime = str(time.ctime())
		checktime = checktime.split()[3]
		checktime = checktime.split(":")[1]
		
	# Checks to see if the baby is ready, yet
		if self.dam.matedtime != checktime:
			newbaby = organisms.Organism()
			print("Congratulations--you've got a new baby!")

		# Sets the new baby's stats
			# New baby gets an "ID" that it then shares with mom and dad to prevent breeding with offspring
			newbaby.babyID = random.randint(1,1000000)
			self.sire.sireID = newbaby.babyID
			self.dam.damID = newbaby.babyID
			
			# Sets the new baby as a standard orgnaism
			newbaby = organisms.Organism()

			# Gives the new baby the same type as its mother
			newbaby.type = self.dam.type

			# Makes newbaby into a list so that it can be processed by "givetype"
			offspring = [newbaby]

			# Gives newbaby a name that's half its mom and half its dad
			species = self.sire.name.split()[1]
			genus = self.dam.name.split()[0]
			organisms.givetype(offspring)
			newbaby = offspring[0]
			newbaby.name = genus.capitalize() + " " + species.lower()


			hybridvigor = False
			for stat in self.dam.stats.keys():
				if stat in self.sire.stats.keys():
					if (self.dam.stats[stat] // 2 == 0) and (self.sire.stats[stat] // 2 == 0):
						newbaby.stats[stat] = self.sire.stats[stat] + self.dam.stats[stat]
						hybridvigor = True
					elif (self.dam.stats[stat] // 2 != 0) and (self.sire.stats[stat] // 2 != 0):
						newbaby.stats[stat] = self.sire.stats[stat] + self.dam.stats[stat]
						hybridvigor = True
				else:	
					newbaby.stats[stat] = ((self.sire.stats[stat] + self.dam.stats[stat]) // 2)

			print("\n\tMom:")
			print("\tName: " + self.dam.name) 
			print("\tType: " + self.dam.type)
			print("\tSex: " + self.dam.sex.capitalize())
			for stat in self.dam.stats.keys():
				print("\t\t" + stat + " " + str(self.dam.stats[stat]))

			print("\n\tDad:")
			print("\tName: " + self.sire.name) 
			print("\tType: " + self.sire.type)
			print("\tSex: " + self.sire.sex.capitalize())
			for stat in self.sire.stats.keys():
				if stat not in self.excludestats:
					print("\t\t" + stat + " " + str(self.sire.stats[stat]))


			print("\n\tThe new baby is a hybrid of mom and dad:")
			if hybridvigor == True:
				print("\t\t...and hey--this one's got hybrid vigor (at least one enhanced trait)!")
			print("\tName: " + newbaby.name)
			print("\tType: " + newbaby.type) 
			print("\tSex: " + newbaby.sex.capitalize())
			
			# Assigns specific stats to baby
			for stat in newbaby.stats.keys():
				if stat not in self.excludestats:
					print("\t\t" + stat + " " + str(newbaby.stats[stat]))
			
			# Puts mom and dad back in bestiary
			self.bestiary.append(self.sire)
			self.bestiary.append(self.dam)

			# Clears these variables for use again
			self.sire = ""
			self.dam = ""

			# Empties the nursery
			self.nursery = []

			# Puts baby into bestiary
			self.bestiary.append(newbaby)
		else:
			print("Looks like the baby's not ready yet--the parents are still nesting!  Come back tomorrow.")

	def actexpdump(self):
		for exptype in self.expdict.keys():
			while self.expdict[exptype] >= 100:				
				for key in self.statexpdict.keys():
					if exptype.lower() in key.lower():
						self.stats[self.statexpdict[exptype]] += 1
						self.expdict[exptype] -= 100
				

	def gameexpdump(self):
		# Checks to see whether or not you've earned more than ten exp points in game, and if you have, distributes them across types of exp
		if self.expdict["game"] >= 10:
			for exptype in self.expdict.keys():
				if exptype != "game":
					self.expdict[exptype] += 1
			self.expdict["game"] -= 10

	def checklog(self):
		if self.naturelog:
			print("\n ### NATURE LOG ### ")
			for element in self.naturelog:
				print("Shuffled-name: " + "\t" + element.name)
				print("Type: " + element.type + "\n")
			print("\n")
		else:
			print("Your nature log is empty--go find something!")
			input("")
	
	def checkHP(self):
		print("\nYour HP: " + str(self.stats["HP"]))
		if self.companion:
			print("{0}'s HP: ".format(self.companion.name) + str(self.companion.stats["HP"]))
		if self.target:
			print("Opponent HP: " + str(self.target.stats["HP"]))

	def checkstats(self):
		print("These are your current stats: ")
		for stat in self.stats.keys():
			print(stat+": " + str(self.stats[stat]))

	def companionattack(self):
		if self.companion and self.companion.stats["HP"] > 0:
			self.companion.orgattack(self.target)
			if self.companion.stats["HP"] > 0 :
				self.tempenemy = self.companion

	def encounter(self):
		self.safe = False
		self.target.safe = False
		self.target.stats["HP"] = self.target.stats["Max HP"]
		self.tempenemy = self
		# Actions the player can take
		encoptions = {
		"attack" : self.attack,
		"flee" : self.flee,
		"befriend" : self.befriend
		#"capture it" : self.capture
		}
		if self.companion:
			encoptions["companion attack"] = self.companionattack

		# Actions the enemy can take

		self.playsound()
		while (self.safe == False) and (self.stats["HP"] > 0) and (self.target.safe == False) and (self.target.stats["HP"] > 0):
			self.checkHP()
			print("######################################################################")
			
			print("You're facing-off against a {1} {0}!  What do you want to do?".format(self.target.name, self.target.sex))
			print("You can: ")
			for option in encoptions.keys():
				print(option.title())
			userinput = input("")
			choice = ""
			proceed = False
			for key in encoptions.keys():
				if userinput in key and userinput != "":
					choice = key
					encoptions[choice]()
					proceed = True
					print("######################################################################")
					break
			if proceed == False:
				print("Your command wasn't clear--try typing it again!")
			elif choice == "check health":
				pass
			elif self.safe == False:
				if self.companion and self.companion.stats["HP"] < 1:
					print("{0} has collapsed!  {1} turns its attention back to {2}!".format(self.companion.name, self.target.name, self.name))
					self.tempenemy = self	
				self.target.orgchoose(self.tempenemy)
		if self.stats["HP"] < 1:
			print("You were driven off!")
			self.restoreHP()
		elif self.target.stats["HP"] < 1:
			print("You drove the {0} off!".format(self.target.name))
			self.tempenemy = self
			self.target.orgdrop(self)
			self.restoreHP()
			self.expdict["game"] += self.target.stats["Exp"]
			print("You've gained {0} exp!".format(self.target.stats["Exp"]))
			self.previoustarget = self.target
			self.target = ""
		self.gameexpdump()



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
					if userinput in choice and userinput != "":
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

	# Examine bestiary
	def examinebestiary(self):
		self.excludestats = ["Max HP", "Gold", "Exp"]
		if self.bestiary:
			for org in self.bestiary:
				print("\t" + "Name: " + org.name)
				print("\t" + "Type: " + org.type)
				print("\t" + "Sex: " + str(org.sex).title())
				for stat in org.stats.keys():
					if stat not in self.excludestats:
						print("\t\t" + stat + " " + str(org.stats[stat]))
				print("\n")
		else:
			print("You don't have anything in your bestiary, yet--go out and explore!")
	def examinecompanion(self):
		if not self.companion:
			print("You don't have a companion to examine right now!")
			return
		print("\t" + "Name: " + self.companion.name)
		print("\t" + "Type: " + self.companion.type)
		print("\t" + "Sex: " + str(self.companion.sex).title())
		for stat in self.companion.stats.keys():
			if stat not in self.excludestats:
				print("\t\t" + stat + " " + str(self.companion.stats[stat]))
		print("\n")

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
					if userinput.lower() in env.lower() and userinput != "":
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

	def feedcompanion(self):
			print("What would you like to feed your companion?")
			for element in self.inventory:
				print(element.name.capitalize())
			userinput = input("")
			for element in self.inventory:
				if userinput == element.name:
					print("You fed {0} {1}!".format(self.companion.name, element.name))
					print("{0}'s {1} went up by {2}!".format(self.companion.name, element.affects, element.quality))
					self.companion.stats[element.affects] += element.quality
					self.inventory.pop(self.inventory.index(element))
					return


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
					if activitycomplete == False and "list" not in activity:
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
								if category.lower() != "game":
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
			self.actexpdump()
		elif self.fixed == False:
			flexactivities(self)
			self.actexpdump()


	def goback(self):
		self.brokenloop = True

	def look(self):
		print("You go looking for things in a reasonable way.")
		if not self.currentenv.occupants:
			print("There's nothing here...try another environment!")
			return

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
	
		print("You found something!")
		self.addtolog()
		self.encounter()

	def playsound(self):
		newsound = ""
		if self.soundon:
			if self.target.sound:
				pygame.mixer.init()
				newsound = pygame.mixer.Sound(self.target.sound)
				pygame.mixer.Channel(1).play(newsound)
				time.sleep(2)
				pygame.mixer.Channel(1).stop()


# Used to print out all animals and their shuffled names for debugging use
	def printanimals(self):
		for animal in self.popmaster:
			print("Current Name:" + animal.name + "\n", "True Name: " + animal.truename + "\n", "Mega-Shuffled Name: " + animal.meganame + "\n","Inter-Shuffled Name: " + animal.intername + "\n", "Type: " + animal.type + "\n")
			for stat in animal.stats.keys():
				print("\t"+stat+":"+ " " + str(animal.stats[stat]))

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

	def setcompanion(self):
		i = 0
		self.excludestats = ["Gold", "Exp", "Max HP"]
		if self.bestiary:
			for org in self.bestiary:
				org.index = i
				print("\tName: " + org.name)
				print("\tType: " + org.type)
				print("\tBestiary Index:" + str(org.index))
				for stat in org.stats.keys():
					if stat not in self.excludestats:
						print("\t\t" + stat + ": " + str(org.stats[stat]))
				print("\n")
				i += 1
			print("######################################################################")
			print("You can currently have one companion traveling alongside you--who would you like it to be?")
			print("(You can either type the entire name or just the index number!")
			userinput = input("")
			for org in self.bestiary:
				if userinput == (str(org.index) or org.name):
					self.formercompanion = self.companion
					self.companion = org
					self.bestiary.pop(self.bestiary.index(self.companion))
					break
			if self.companion != self.formercompanion and self.formercompanion:
				print("Your new companion is {0}, and {1} has gone back into the bestiary!".format(self.companion.name, self.formercompanion.name))
				input("")
				self.bestiary.append(self.formercompanion)
			else:
				print("You've decided to keep traveling with {0} for a while.".format(self.companion.name))


		else:
			print("You don't have anyone in the bestiary to choose from...yet.")

	def sit(self):
		if not self.currentenv.occupants:
			print("There's nothing here...try another environment!")
			return
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
		if (self.stats["Luck"]*2) > self.currentenv.difficulty:
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
				print("\tA wild {0} (a {1}) cautiously appears--it looks like a {2}!".format(self.target.name, self.target.type, self.target.sex))
				self.addtolog()
				self.sat = True
				self.encounter()
			elif chosen == False:
				print("\t...nothing.  Looks like you'll have to try again.")
		else:
			print("######################################################################")
			print("\tIt looks like you might need to level-up your \"luck\" stat before anything will approach you in this area!")

	def togglesound(self):
		while True:
			print("Would you like sounds on or off?")
			userinput = input("")
			if "f" in userinput:
				self.soundon = False
				print("Sound off!")
				return
			elif "n" in userinput:
				self.soundon = True
				print("Sound on!")
				return
			else:
				print("I didn't get that--try again!")

	def restoreHP(self):
		self.stats["HP"] = self.stats["Max HP"]
		if self.companion:
			self.companion.stats["HP"] = self.companion.stats["Max HP"]

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


