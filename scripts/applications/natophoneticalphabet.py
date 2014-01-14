#!/usr/bin/python

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

class NatoPhoneticAlphabet:

	def __init__(self):
		self.temp = ""

	def decode(self, character):
		return nato[character.upper()]

if __name__ == '__main__':

	mynatopa = NatoPhoneticAlphabet()
	print mynatopa.decode("abc")
