"""
Real News Checker
File: wsite.py

Created by Zachary Nawrocki
LinkedIn: www.linkedin.com/in/zachary-nawrocki-b88b54152

This file, containing the class Site, contains all the necesasry data
needed for a given url on Real News Checker.
"""

import urllib.request
import requests
from googlesearch import search
from bs4 import BeautifulSoup

class Site:
	def __init__(self, url):
		self.url = url
		self.headers = {'User-Agent':'Mozilla/5.0'}
		try:
			self.wsite = requests.get(self.url)
		except:
			self.good = False
			return
		self.html = BeautifulSoup(self.wsite.text, "html.parser")
		self.titlestr = None
		self.search = ""
		self.similar_sites = []
		self.name_or = ""
		self.nm = ""
		self.good = True

	def name(self, tablesites):
		splt = self.url.split(".")
		self.name_or = splt[1]
		#Fixes some of the parsing bugs for urls without "www"
		if "www" not in splt[0]:
			parse_index = splt[0].find('//')
			self.name_or = splt[0][parse_index + 2:]
		# List of news sites to abbreviate
		self.nm = tablesites.get(self.name_or)
		return self.nm

	def find_sites(self, title):
		for page in search(title, num=7, start = 0, stop=7):
			# Makes sure the new news articles does not come from the same website
			if page.split(".")[1] != self.name_or:
				self.similar_sites.append(page)
		print("\n\n" + str(len(self.similar_sites)) + " similar sites found...\n")
		return self.similar_sites

	def title(self):
		if self.html.title.string is not None:
			self.titlestr = self.html.title.string
			if self.titlestr == "Access Denied":
				self.titlestr = "Article "
		else:
			self.titlestr = "Article "
		return self.titlestr

	# checks to see if url is valid
	def isgood(self):
		if self.good:
			return True
		else:
			return False

  
