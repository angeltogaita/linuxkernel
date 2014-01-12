#!/usr/bin/python

import pygame
import sys
import time

code = {'A': '.-',	'B': '-...',	'C': '-.-.',
	'D': '-..',	'E': '.',	'F': '..-.',
	'G': '--.',	'H': '....',	'I': '..',
	'J': '.---',	'K': '-.-',	'L': '.-..',
	'M': '--',	'N': '-.',	'O': '---',
	'P': '.--.',	'Q': '--.-',	'R': '.-.',
	'S': '...',	'T': '-',	'U': '..-',
	'V': '...-',	'W': '.--',	'X': '-..-',
	'Y': '-.--',	'Z': '--..',

	'0': '-----',	'1': '.----',	'2': '..---',
	'3': '...--',	'4': '....-',	'5': '.....',
	'6': '-....',	'7': '--...',	'8': '---..',
	'9': '----.'
	}

class MorseGenerator:

	def __init__(self):
		self.message = ""
		self.oneunit = 0.5
		self.threeunits = 3 * self.oneunit
		self.sevenunits = 7 * self.oneunit
		self.morsesoundfiles = 'morse_sound_files/'

		pygame.init()

	def verify(self, string):
		keys = code.keys()
		for char in string:
			if char.upper() not in keys and char != ' ':
				sys.exit('Error the charcter ' + char + ' cannot be translated to Morse Code')

	def generate(self, message):
		self.message = message
		self.verify(message)

		for char in self.message:
			if char == ' ':
				print ' '*7,
				time.sleep(self.sevenunits)
			else:
				print code[char.upper()],
				pygame.mixer.music.load(self.morsesoundfiles + char.upper() + '_morse_code.ogg')
				pygame.mixer.music.play()
				time.sleep(self.threeunits)

if __name__ == '__main__':

	test = MorseGenerator()
	test.generate("0")
