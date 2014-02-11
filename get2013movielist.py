#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2

urlroot = 'http://www.imdb.com'
nextpage = '/search/title?at=0&sort=alpha&title_type=feature&year=2013,2013'
item = 1
nextsubpre = '/search/title?at=0&sort=alpha,asc&start='
nextsubpost = '&title_type=feature&year=2013,2013'




# Open file for writing
fo = open("movies.txt", "w")

condition = True
while condition:
	# Request HTML
	response = urllib2.urlopen(urlroot + nextsubpre + str(item) + nextsubpost)
	html = response.read()

	# Load HTML into BeautifulSoup
	soup = BeautifulSoup(html)

	# Get all the movie names and links
	movies = soup.find('tr', 'detailed')
	while movies != None:
		mname = movies.find('td', 'title').a.get_text()
		murl = urlroot + movies.find('td', 'title').a['href']
		fo.write((mname + ';;' + murl + '\n').encode('UTF-8'))
		print((mname + ', ' + murl).encode('UTF-8'))
		movies = movies.find_next('tr', 'detailed')

	# Build next link
	item += 50
	if item > 8654:
		condition = False

'''
	# Find the next link
	link = soup.find('span', 'pagination')
	nextpage = None
	if link != None:
		link = link.a
		while not 'Next' in link.get_text():
			link = link.find_next_siblings("a")
			link = link[0]

		nextpage = link['href']
	else:
		condition = False
'''

# Close file
fo.close()




# Get the next page

'''

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)
print(soup)

'''