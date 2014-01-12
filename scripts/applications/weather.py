#!/usr/bin/python

import time
import feedparser
import os

from voicesynthetizer import Synthetizer

class Weather:

	def __init__(self, method):
		self.method = method
		self.url = "http://weather.yahooapis.com/forecastrss?w=124162&u=c"
		self.city = ""
		self.high = ""
		self.low = ""

		self.speaker = Synthetizer("festival", "spanish")

		self.parser(self.url)

	def setup(self, method):
		self.method = method
		return

	def parser(self, url):
		self.url = url
		print self.url
		d = feedparser.parse(self.url)
		location = d.feed.yweather_location
		atmosphere = d.feed.yweather_atmosphere
		astronomy = d.feed.yweather_astronomy
		self.city=location['city']
		humidity=atmosphere['humidity']
		sunrise=astronomy['sunrise']
		sunset=astronomy['sunset']

		summary=d.entries[0].summary
		#print summary
		temp=summary.split("High: ")
		temp=temp[1].split(" Low: ")
		self.high=temp[0]
		self.low=temp[1].split("<br />")[0]
		return

	def test(self):
		self.speaker.speechit("Reporte del Clima en " + self.city)
		self.speaker.speechit("Temperatura Maxima de " + self.high + " grados centigrados")
		self.speaker.speechit("Temperature Minima de " + self.low + " grados centigrados")
		return

if __name__ == '__main__':

	test = Weather("temp")
	test.test()
