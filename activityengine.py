#!/usr/bin/env python3

import sys
import re
import pickle


# Saves a greeting for use later
#greeting = print("WELCOME TO--*ahem*--welcome to the game. What did you do, today?")

# Gets whatever the user did that day as input.


# Generates an empty list to be populated by the user's activities
#activitydict = {"walk" : 5}


def main():

	# Links categories and related activities
	activitydict = {"wellness" : {"walk" : 5, "run" : 10}, "professional" : {}, "social" : {}, "academics" : {}}

	# Aggregates experience by category
	expdict = {"wellness" : 0, "academics" : 0, "social": 0, "professional" : 0}

	def getactivities():
		greeting = print("WELCOME TO--*ahem*--welcome to the game. What did you do, today?")
		activity = input("")
		count = 0
		for category in activitydict.keys():
			if activity in activitydict[category]:
				count += 1
				print("You've done that one before!")
				current = activitydict[category][activity]
				print("{0} experience points have been added to {1}!".format(current, category))
				expdict[category] += current
		if count == 0:
			while True:
				print("That's a new one--how many experience points is it worth?  (Give a number between 1 and 50!)")
				activityexp = input("")
				try:
				    activityexpint = int(activityexp)
				    break
				except ValueError:
				    print("Could not convert data to an integer.")
				activitydict[activity.lower()] = activityexp
			for category in expdict.keys():
				print(category.title())
			while True:
				print("To which category should I assign that exp?  You can assign it to any of the above categories:\n")
				catchoice = input("")
				if catchoice.lower() in expdict.keys():
					expdict[catchoice] += activityexpint
					print("{0} exp added to {1}!".format(activityexp, catchoice))
					break
				else:
					print("Ooops--that one didn't register.  Try entering it again!")

	pickle.dump(getactivities(), open("savefile.py", "wb"))


	print(expdict)
	print(activitydict)

if __name__ == "__main__":
	main()