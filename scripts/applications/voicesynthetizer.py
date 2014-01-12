import commands
import logging
import sys
import threading
import unicodedata
import time

from ports import Ports

class Synthetizer(threading.Thread):

	def __init__(self, synthetizer, language):
		self.synthetizer = synthetizer
		self.language = language
		self.arguments = ""

		threading.Thread.__init__(self)
		self.lock = threading.Lock()

		self.setsynthetizer(self.synthetizer)

		self.port = Ports()

	def setsynthetizer(self, synthetizer):
		self.synthetizer = synthetizer
		self.setallarguments()

        def getsynthetizer(self, synthetizer):
                return self.synthetizer

	def setlanguage(self, language):
                self.language = language
		if self.synthetizer == "festival":
			self.languageargument = "--language " + self.language

	def getlanguage(self, language):
		return self.language

	def setallarguments(self):
		if self.synthetizer == "festival":
			self.text2speechargument = "--tts"
			if self.language == "spanish":
				self.languageargument = "--language " + self.language
			else:
				self.languageargument = ""
			self.arguments = " " + self.synthetizer + " " + self.text2speechargument + " " + self.languageargument		

	def speechit(self, text):
		#text = unicodedata.normalize('NFKD', text)
		self.lock.acquire()
		self.port.openport()
		text = text.encode('ASCII', 'ignore')
		print text
		time.sleep(4)
		command = "echo " + "" + " | " + self.arguments
		command = "echo " + text + " | " + self.arguments
		status, output = commands.getstatusoutput(command)
		self.port.closeport()
		self.lock.release()

if __name__ == "__main__":

	myspeak = Synthetizer("festival", "spanish")
	
	myspeak.speechit("Hola x e uno golf yanki quebec, estacion experimental sayulita")
	#myspeak.speechit("no sin antes ofrecer una disculpa por el atraso en la entrega de este documento, les hago llegar los comentarios que esta Federacion hace al proyecto del nuevo reglamento para el servicio de radioaficionados, en el que se hacen comentarios y propuestas puntuales al documento")
	myspeak = Synthetizer("festival", "english")
	myspeak.speechit("hello crazy guy")

