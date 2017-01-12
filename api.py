import urllib2
import json
from collections import OrderedDict

class Api(object):
	
	def __get_request(url):
		try:
			response = urllib2.urlopen(url)
			return response.read()
		except:
			print("Could not load '%s'." % str(url))
			return ""
	
	def __prettify_json(input):
		try:
			parsed = json.loads(input, object_pairs_hook=OrderedDict)
			return json.dumps(parsed, indent=4)
		except:
			return input
	
	def get_app_list():
		url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
		string = __get_request(url)
		dict = json.dumps(string)
		array = [str(e['appid']) for e in dict['applist']['apps']['app']]
		return array
	
	def get_app_details(appid=None):
		if appid is None:
			return ""
		url = "http://store.steampowered.com/api/appdetails/?cc=us&l=english&filters=basic,developers,publishers,price_overview,platforms,metacritic,categories,genres,recommendations,achievements,release_date&appids=" + str(appid)
		string = __get_request(url)
		content = __prettify_json(string)
		return content
