import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import urllib2
import json
import time
import random


gapi1 = 'http://maps.googleapis.com/maps/api/geocode/json?address='
gapi2 = '&sensor=false'
gogo = False


fi = open('movielocations.txt', 'r')
fo = open('movielocationsgps.txt', 'a')

# Read each movie
for line in fi:
	# Parse out and build URL
	parts = line.split(';;')
	url = parts[2]
	url = url.replace('\n', '')
	url = gapi1 + urllib2.quote(url) + gapi2

	test = parts[1] + ';;' + parts[2]
	test = test.replace('\n', '')
	if test == 'http://www.imdb.com/title/tt2219552/;;Ladysmith, British Columbia, Canada':
		gogo = True

	if gogo:
		# Request HTML
		try:
			print url
			response = urllib2.urlopen(url)
			html = response.read()

			data = json.loads(html)
			status = data['status']

			if status == 'OVER_QUERY_LIMIT':
				print 'ERROR: ' + status
				break
			elif status == 'OK':
				lat = data['results'][0]['geometry']['location']['lat']
				lon = data['results'][0]['geometry']['location']['lng']
				out = parts[0] + ';;' + parts[1] + ';;' + parts[2].replace('\n', '') + ';;' + str(lat) + ';;' + str(lon) + '\n'
				fo.write(out)
				time.sleep(random.uniform(0.1, 1.5))
				print out
			else:
				print 'ERROR: ' + status

		except urllib2.HTTPError, e:
			print 'ERROR: ' + str(e.code)

# Close file
fi.close()
fo.close()