import urllib
import httplib
import os
import os.path
import sys
from getopt import getopt
import random
import json
import requests

API_KEY='API_KEY'
Username='fayanp'

def test():
	print 'Pruebas de conexion'
	#url='http://ws.audioscrobbler.com//2.0/?method=user.gettopalbums&user='+Username+'&api_key='+API_KEY+'&format=json'
	try:
		params = urllib.urlencode({'method' : 'user.getTopAlbums',
               'user' : Username,
               'api_key' : API_KEY,
               'format':'json'})

		header = {"user-agent" : "myapp/1.0",
		          "Content-type": "application/x-www-form-urlencoded"}

		lastfm = httplib.HTTPConnection("ws.audioscrobbler.com")

		lastfm.request("POST","/2.0/?",params,header)

		response = lastfm.getresponse()
		with open('charts_'+Username+'.json', 'w') as outfile:
    			json.dump(response.read(), outfile)
		#print response.read()
	except Exception,err:
		print "#"*20
		print "I couldn't download the profile or make a local copy of it."
		print "#"*20

	try:
		with open('charts_'+Username+'.json','rb') as json_data:
    			jsondoc = json.load(json_data)
    			print(jsondoc)
		#xmldoc=minidom.parse(data)
		data.close()
	except Exception,err:
		print '#'*20
		print "Error while parsing your profile. Your username might be misspelt or your charts empty."
		print '#'*20		
		print 'fin de prueba'
		sys.exit()
	

test()
