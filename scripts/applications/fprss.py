import sys
import feedparser
import threading
from voicesynthetizer import Synthetizer

#List of uples (label, property-tag, truncation)
COMMON_CHANNEL_PROPERTIES = [
    ('Channel title:', 'title', None),
    ('Channel description:', 'description', 150),
    ('Channel URL:', 'link', None),
]

COMMON_ITEM_PROPERTIES = [
    ('Item title:', 'title', None),
    ('Item description:', 'description', 150),
    ('Item URL:', 'link', None),
]

INDENT = u' '*4

class FeedParserRss(threading.Thread):
	def __init__(self):
		self.url = None
		self.parsedurl = None
		self.channelname = None
		self.itemsnumber =  None
		threading.Thread.__init__(self)
		self.speak = Synthetizer("festival", "spanish")
		self.initialize()

	def initialize(self):
		self.seturl("http://www.eluniversal.com.mx/rss/universalmxm.xml")
		#mynews.seturl("http://www.eluniversal.com.mx/rss/computo.xml")
		self.parseurl()

	def seturl(self, url):
		self.url = url
		print "url? " + self.url

	def geturl(self):
		return self.url

	def parseurl(self):
		self.parsedurl = feedparser.parse(self.url)

	def setchannel(self, channelname):
		self.channelname = channelname
		print "channel name? " + self.channelname

	def getchannel(self):
		return self.channelname

	def setitemsnumber(self, itemsnumber):
		self.itemsnumber = itemsnumber
		print "items number? " + self.itemsnumber

	def channels(self):
		print "channels"

	def getitemsnumber(self):
		return self.itemsnumber

	def gettitle(self):
		newsdata = self.parsedurl
		channel = newsdata.feed

		#print channel['title'], channel['description']
		#self.speak.speechit(channel['description'])

		#for label, prop, trunc in COMMON_CHANNEL_PROPERTIES:
		#	print label
		#	print prop
		#	print trunc
		#	value = channel[prop]
		#	if trunc:
		#		value = value[:trunc] + u'...'
		#	print label, value

	def getitems(self):
                newsdata = self.parsedurl
                items = newsdata.entries
		items.sort()

		for item in items[1:4]:
			#print item['title']
			#print item['description']
			self.speak.speechit(item['title'])
			self.speak.speechit(item['description'])

		#	for label, prop, trunc in COMMON_ITEM_PROPERTIES:
		#		value = item[prop]
		#		if trunc:
		#			value = value[:trunc] + u'...'
		#		print INDENT, label, value
		#	print INDENT, u'---'

if __name__ == "__main__":

	mynews = FeedParserRss()

	mynews.seturl("http://www.eluniversal.com.mx/rss/universalmxm.xml")
	mynews.seturl("http://www.eluniversal.com.mx/rss/computo.xml")
	mynews.setchannel("national")
	mynews.setitemsnumber("1")
	mynews.parseurl()

	title = mynews.gettitle()
	mynews.getitems()


