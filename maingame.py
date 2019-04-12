#!/usr/bin/env python3

import sys
import re
import os
import pickle
#import activityengine
from gameclasses import *
#import organisms
from shufflecipher import *

#Shuffles organisms into unrecognizable names
megaorglist = [megacipher(organism) for organism in popmaster]
print(megaorglist)

#newplayer = Player()





newplayer = Player()


def main(player):

	# Prompts the user to choose whether to load an existing game or play a new game.
	def begingame():
		welcome = input("Welcome back!  Would you like to start a new game or load an existing game? ")
		if "n" in welcome.lower():
			newplayer = Player()
			return newplayer
		elif "l" in welcome.lower():
			filelist = []
			for item in os.listdir():
					if item.endswith(".pickle"):
						filelist.append(item[:-7])
			if filelist:
				while True:
					print("These are the available files: ")
					for item in filelist:
						print(item)
					choosefile = input("What's your filename? (Give the exact filename!) ")
					if choosefile in filelist:
						with open(choosefile+".pickle", 'rb') as handle:
							newplayer = pickle.load(handle)
							return newplayer
					else:
						print("I can't find that file!")
			else:
				print("There are no saved files--starting a new game!")
				newplayer = Player()
				return newplayer

	def choosenext(player):
		while True:
			print("What would you like to do next?  You can choose from any of these:")
			for key in player.optionlist.keys():
				print(key.title())
			usrinput = input("")
			for option in player.optionlist.keys():
				if (usrinput.lower() in option):
					player.optionlist[option]()



	
	choosenext(begingame())
	#player.opener()



if __name__ == "__main__":
	main(newplayer)

