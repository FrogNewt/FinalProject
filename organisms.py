#!/usr/bin/env python3

import sys
import re
import pickle
from gameclasses import *



class Animal(livingThing):
	def __init__(self):
		super().__init__()

class Reptile(Animal):
	def __init__(self):
		super().__init__()
		self.therm="ecto"

newanimal = Reptile()

print(newanimal.therm)


