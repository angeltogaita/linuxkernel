#!/usr/bin/python

import ConfigParser
from morsegenerator import MorseGenerator

class MorseTeacher:

	def __init__(self):
		self.hi = ""
		self.configuration()

	def configuration(self):
		self.conf = ConfigParser.ConfigParser()
		self.path = "configuration/configuration.morseteacher"
		self.conf.read(self.path)

	def welcome(self, section):
		welcome = section + 'welcome'
		print self.conf.get(section, welcome)	

if __name__ == '__main__':
	mymorse = MorseTeacher()
	mymorse.welcome("basic")

	#testg = MorseGenerator()
	#testg.generate("hola amor")
