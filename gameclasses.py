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
	def __init__(self, name = "Unknown"):
		self.name = name
		
	# Links categories and related activities
		self.activitydict = {"fitness" : {"walk" : 5, "run" : 10}, "intellect" : {}, "intellect" : {}, "happiness" : {}}

	# Aggregates experience by category
		self.expdict = {"fitness" : 0, "intellect" : 0, "naturalism": 0, "happiness" : 0}

	# Creates list of all options for a player to choose
		self.optionlist = {
			"add new activities" : self.getactivities,
			"play the game" : self.fourohfour,
			"check my exp" : self.checkexp,
			"quit game" : self.quitsave
		}

	# Stuff the player has
		self.inventory = []
		self.gold = 0
		self.equipment = []


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


	#Prompts the player to save the game and either writes to a new file or overwrites an existing file
	
	def checkexp(self):
		print(self.expdict)


	def fourohfour(self):
		print("Ooops!  That's not working yet (but if this is \'play game\' it's not supposed to work, yet)!")

# Used to strictly save the game (without quitting)
	def save(self, namedfile="newgame1"):
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

# Verifies that the user wants to quit and offers to save the game
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
				print("All done with your activities for the day?")
				endinput = input("")
				if "quit" in endinput:
					self.quitsave()
			
				if ("y" in endinput):
					fullbreak = True

					# Prompts user to save the game
					self.save()

					break
				
				# Returns to original question about activities (what did you do, today?)
				else:
					break

			if fullbreak == True:
				break







	

		