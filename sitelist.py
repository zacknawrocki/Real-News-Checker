"""
Real News Checker
File: sitelist.py

Created by Zachary Nawrocki
LinkedIn: www.linkedin.com/in/zachary-nawrocki-b88b54152

This file, containing the class HashSites, provides the official titles of the most popular 
online news websites, properly punctuated, according to online rankings from the sources in 
sitetitles.txt. The intent of HashSites is to provide a cleaner set of information for website 
titles presented on the web UI. The list of website titles are easily editable and can be found
in sitetitles.txt.

If a given url does not come from one of these websites, it will continue to contain
the original web title in the Site class from wsite.py.
"""

class HashSites(object):
	# set up hash table with information from subtitles.txt
	def __init__(self):
		self.table = [None] * 100
		# parse text file
		parseready = False
		print("Loading sitetitles...")
		textfile = open("sitetitles.txt", "r")
		lines = textfile.readlines()
		textfile.close()
		for line in lines:
			line = line.strip()
			# Detect where in text file to start parsing
			if line == "SITETITLES:":
				parseready = True
				continue
			if parseready:
				insert = line.split("-")
				# add to table
				index = self.hash_fn(insert[0])
				if self.table[index] is None:
					self.table[index] = [(insert[0], insert[1])]
				else:
					self.table[index].append((insert[0], insert[1]))
				print(insert[1] + " loaded for " + insert[0])
	# calculate index with a hash function
	def hash_fn(self, title):
		index = (sum(map(ord, title)) + len(title)) % 100
		return index
	# retrieve site from hash table
	def get(self, title):
		index = self.hash_fn(title)
		if self.table[index] is not None and self.table[index][0][0] == title:
			return self.table[index][0][1]
		elif self.table[index] is not None:
			for tl in self.table[index]:
				if tl[0] == title:
					return tl[1]
			return title
		return title






