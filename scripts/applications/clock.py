import time
from voicesynthetizer import Synthetizer

class Clock():

	def __init__(self):
		self.speaker = Synthetizer("festival", "english")

	def clockget(self):
		self.speaker.speechit(time.strftime("%A %B %d %Y %H:%M:%S"))
		


if __name__ == "__main__":

	myclock = Clock()
	myclock.clockget()

