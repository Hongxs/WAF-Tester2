#! /usr/bin/env python
# coding:utf-8
from lib.request_util import *
import time

class logging:
	def __init__(self,logfile):
		self.logfile = logfile
		self.f = open(self.logfile,"w")
		self.f.write("+++++++++++[The result]+++++++++++\n\n")

	def writelog(self,message):
		try:
			self.f.write(message)
		except IOError:
			pass

	def close(self):
		self.f.close()
