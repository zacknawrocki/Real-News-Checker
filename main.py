"""
Real News Checker
File: main.py

Created by Zachary Nawrocki
LinkedIn: www.linkedin.com/in/zachary-nawrocki-b88b54152
"""


import wsite
import sitelist
from flask import Flask, render_template, request

# web
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		request.form["url"]
		article = request.form["url"] 
		return checker(article)
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/updates")
def updates():
	return render_template("updates.html")

@app.route("/results")
def results():
	return render_template("results.html")

def checker(article):

	# Find similar sites
	ws = wsite.Site(article)
	good = ws.isgood()
	if not good:
		return render_template("index.html")
	name = ws.name(tablesites)
	title = ws.title()
	similar_sites = ws.find_sites(title)
	site_objs = []
	# List of varibles to be outputted to results.html
	results = []
	# create list of all the site result objects, in order to create separate objects for a loop ouptut
	for i in range(len(similar_sites)):
		site_objs.append(wsite.Site(similar_sites[i]))

    #Results to Console
       # User inputted data
	print(article)
	print("\n\nSearching link...")
	print("Name of News Company: "+ name)
	print(title)
	if title == "Article ":
		# Site not available yet
		results = []
		results.append(["This site cannot be checked yet.", "/"])
		return render_template("results.html", length = 0, results = results)
	   # printing resulting sites
	for obj in site_objs:
		results.append([obj.title() + " by " + obj.name(tablesites), obj.url])
		print(obj.title() + " by " + obj.name(tablesites))
		print("url: " + obj.url + "\n")

	return render_template("results.html", length = len(similar_sites), results = results)

if __name__ == "__main__":
	
	# load titles
	tablesites = sitelist.HashSites()
	app.run()












