import urllib2
import json
from collections import OrderedDict


def __get_request(url):
	"""
	Makes a GET request to the specified URL and
	returns the string obtained from the response.
	"""
	try:
		response = urllib2.urlopen(url)
		return response.read()
	except:
		raise Exception("Could not load '%s'." % str(url))


def __prettify_json(input):
	"""
	Receives a JSON-formatted string and returs the same
	string with adjusted indentation.
	"""
	try:
		parsed = json.loads(input, object_pairs_hook=OrderedDict)
		return json.dumps(parsed, indent=4)
	except:
		return input


def get_app_list():
	"""
	Returns an array of dicts represeting the JSON of strings
	of all app IDs from the Steam Store API.
	"""
	url = "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
	string = __get_request(url)
	dict = json.loads(string)
	array = dict['applist']['apps']['app']
	return array


def get_app_details(appid=None):
	"""
	Returns a JSON-formatted string with Steam Store
	information regarding the provided app ID number.
	"""
	if appid is None:
		raise Exception('appid was not provided')
	url = "http://store.steampowered.com/api/appdetails/?cc=us&l=english&filters=basic,developers,publishers,price_overview,platforms,metacritic,categories,genres,recommendations,achievements,release_date&appids=" + str(appid)
	string = __get_request(url)
	content = __prettify_json(string)
	return content
