import commands
import logging
import sys
import threading
import serial

class PushToTalk(threading.Thread):

	def __init__(self):
		#threading.Thread.__init__(self)
		#self.lock = threading.Lock()
		self.port = ""

	def openport(self):
		self.port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)
		self.port.write("\r\nSay something:")
		rcv = self.port.read(10)
		self.port.write("\r\nYou sent:" + repr(rcv))

        def closeport(self):
		self.port.close()

if __name__ == "__main__":

	myptt = PushToTalk()

