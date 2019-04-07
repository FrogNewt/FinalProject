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

		self.optionlist = {
			"new game" : self.getactivities,
			"quit" : self.quitsave,
		}

	def opener(self):
		print("Hi, and welcome!")
		while True:
			print("What would you like to do first? (You can choose from these things: ")
			for key in self.optionlist.keys():
				print(key.title())
			
			newinput = input("")
			newinput = newinput.lower()

			for i in self.optionlist.keys():
				if newinput in i:
					self.optionlist[i]()
					break

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

	def getactivities(self):
		greeting = print("What did you do, today?")
		activity = input("")
		count = 0
		
		# Determines whether or not the activity has been done before
		for category in self.activitydict.keys():
			if activity in self.activitydict[category]:
				count += 1
				print("You've done that one before!")
				current = self.activitydict[category][activity]
				print("{0} experience points have been added to {1}!".format(current, category))
				self.expdict[category] += current
		
		# Indicates that the activity hasn't been done before
		if count == 0:
			while True:
				
				# Assigns a quantity of experience points to your activity
				print("That's a new one--how many experience points is it worth?  (Give a number between 1 and 50!)")
				activityexp = input("")
				try:
				    activityexpint = int(activityexp)
				    break
				except ValueError:
				    print("Could not convert data to an integer.")
				self.activitydict[activity.lower()] = activityexp
			for category in self.expdict.keys():
				print(category.title())
			while True:

				# Assigns a category to the activity for future use
				print("To which category should I assign that exp?  You can assign it to any of the above categories:\n")
				catchoice = input("")
				catchoice = catchoice.lower()
				if catchoice in self.expdict.keys():
					self.expdict[catchoice] += activityexpint
					print("{0} exp added to {1}!".format(activityexp, catchoice))
					break
				else:
					print("Ooops--that one didn't register.  Try entering it again!")
				print("All done with your activities for the day?")
				endinput = input("")
				if ("y" in endinput):
					break
				else:
					pass


	

		