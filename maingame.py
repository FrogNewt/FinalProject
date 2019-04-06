#!/usr/bin/env python3

import sys
import re

# Saves a greeting for use later
greeting = print("WELCOME TO--*ahem*--welcome to the game. What did you do, today?")

# Gets whatever the user did that day as input.


#Generates an empty list to be populated by the user's activities
activitydict = {"walk" : 5}

expdict = {"exercise" : 0, "academics" : 0, "social": 0, "professional" : 0}

def getactivities():
	activity = input("")
	if activity.lower() in activitydict.keys():
		print("You've done that one before!")
		print("It's worth {0} exp!".format(activitydict[activity]))
	else:
		print("That's a new one--how many experience points is it worth?  (Give a number between 1 and 50!)")
		activityexp = int(input(""))
		activitydict[activity.lower()] = activityexp
		for category in expdict.keys():
			print(category.title())
		while True:
			print("To which category should I assign that exp?  You can assign it to any of the above categories:\n")
			catchoice = input("")
			if catchoice.lower() in expdict.keys():
				expdict[catchoice] += activityexp
				print("{0} exp added to {1}!".format(activityexp, catchoice))
				break
			else:
				print("Ooops--that one didn't register.  Try entering it again!")

getactivities()

print(expdict)
print(activitydict)
