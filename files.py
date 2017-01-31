import re
import os


def get_app_id(directory):
	"""
	Gets the next app ID to collect data from.
	If it returns 0, it means there are no more apps to
	get data from.
	"""
	app_id = 0
	regex = "^(\d+)\.txt$"
	list = os.listdir(directory)
	for l in list:
		m = re.search(regex, l)
		if m:
			n = int(m.group(1))
			app_id = max(app_id, n)
	return app_id


def save(name, content):
	"""
	Receives two strings: a name for the file and the content
	to be saved. A file with the appropriate name will be
	created and written to.
	"""
	with open(name, 'w+') as f:
		f.write(content)
		f.write("\n")
