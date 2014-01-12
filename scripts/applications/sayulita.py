import logging
import threading
import time

from apscheduler.scheduler import Scheduler
from voicesynthetizer import Synthetizer
from clock import Clock
from fprss import FeedParserRss

class SayulitaMain(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)

		self.speaker = Synthetizer("festival", "spanish")
		self.scheduler = Scheduler()
		self.scheduler.start()
	
	def initialization(self):
		self.speaker.speechit("Aqui proyecto Sayulita operado por x e uno gol yanqui quebec")
		self.speaker.speechit("Estacion experimental de texto a voz")

	def features(self):
		self.clock = Clock()
		self.news = FeedParserRss()

	def logging(self, command):
		if command == 'start':
			logging.basicConfig(filename='sayulita.log', filemode='w', level=logging.INFO)
			logging.basicConfig(format='%(asctime)s %(message)s')
			logging.info('Started')

	def scheduling(self):
		#self.scheduler.interval_schedule(seconds=1)
		#self.clock.clockget()
		self.news.getitems
		self.scheduler.add_cron_job(self.clock.clockget,month='*',day='*',hour='*',minute ='*',second='0')
		self.scheduler.add_cron_job(self.initialization,month='*',day='*',hour='*',minute ='*',second='15')
                self.scheduler.add_cron_job(self.news.getitems,month='*',day='*',hour='*',minute ='15,30,45',second='15')

		self.scheduler.print_jobs()


if __name__ == "__main__":

	myfc = SayulitaMain()
	myfc.logging('start')
	myfc.initialization()
	myfc.features()
	myfc.scheduling()

	while True:
		print 'Sayulita Project Alive'
		time.sleep(5)

