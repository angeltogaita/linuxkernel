#!/usr/bin/python

import ConfigParser
from morsegenerator import MorseGenerator
from voicesynthetizer import Synthetizer

nato = {'A': 'alfa',    'B': 'bravo',   'C': 'charli',
        'D': 'delta',	'E': 'eco',	'F': 'foxtrot',
	'G': 'golf',	'H': 'hotel',	'I': 'india',
	'J': 'yuliet',	'K': 'kilo',	'L': 'lima',
	'M': 'maik',	'N': 'november','O': 'oscar',
	'P': 'papa',	'Q': 'quebec',	'R': 'romeo',
	'S': 'sierra',	'T': 'tango',	'U': 'union',
	'V': 'victor',	'W': 'wiski',	'X': 'exrey',
	'Y': 'yanqui',	'Z': 'zulu',
	}

class MorseTeacher:

	def __init__(self):
		self.hi = ""
		self.configuration()
		self.character = ""

		self.speaker = Synthetizer("festival", "spanish")
		self.morse = MorseGenerator()

	def configuration(self):
		self.conf = ConfigParser.ConfigParser()
		self.path = "configuration/configuration.morseteacher"
		self.conf.read(self.path)

	def natodecode(self, character):
		return nato[character.upper()]

	def welcome(self, section):
		welcome = section + 'welcome'
		print self.conf.get(section, welcome)
		self.speaker.speechit(self.conf.get(section, welcome))

	def basic(self):
		topic = self.conf.get("basic", "basict2")
		#self.speaker.speechit(topic)
		for s in self.conf.get("basic", "basicq2"):
			print s
			de=self.natodecode(s)
			print de
			self.speaker.speechit(de)
			#self.speaker.speechit(s)
			#self.speaker.speechit(topic + " " + s + " en codigo morse es")
			#self.speaker.speechit(self.morse.natodecode(s))
			#self.morse.generate(s)

if __name__ == '__main__':

	mymorse = MorseTeacher()
	
	#mymorse.welcome("general")
	#mymorse.welcome("basic")
	mymorse.basic()

	#testg = MorseGenerator()
	#testg.generate("hola amor")
