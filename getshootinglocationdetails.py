import sys
reload(sys)
sys.setdefaultencoding("utf-8")


from bs4 import BeautifulSoup
import urllib2

locationspath = 'locations?ref_=tt_dt_dt'
gogo = False

# Open movies list file
fi = open('movies.txt', 'r')
fo = open('movielocations.txt', 'a')

# Read each movie
for line in fi:
	# Parse out and build URL
	parts = line.split(';;')
	url = parts[1]
	url = url.replace('\n', '')
	url += locationspath

	if url == 'http://www.imdb.com/title/tt1941595/locations?ref_=tt_dt_dt':
		gogo = True
	
	if gogo:
		# Request HTML
		try:
			print url
			response = urllib2.urlopen(url)
			html = response.read()

			# Load HTML into BeautifulSoup
			soup = BeautifulSoup(html)

			# Parse Out Any Film Locations
			locations = soup.find('div', 'soda')
			while locations != None:
				local = locations.find('dt')
				if local != None:
					local = local.a.get_text()
					local = local.replace('\n', '')
					out = parts[0] + ';;' + parts[1].replace('\n', '') + ';;' + local + '\n'
					fo.write(out)
					print out
				locations = locations.find_next('div', 'soda')
		except urllib2.HTTPError, e:
			 print 'ERROR: ' + str(e.code)

# Close file
fi.close()
fo.close()


# Movie Name

# MPAA Rating

# Runtime

# Genres

# Release Date

# Country

# User Rating (n / 10)

# Metascore (n / 100)
