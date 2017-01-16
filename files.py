

def save(name, content):
	"""
	Receives two strings: a name for the file and the content
	to be saved. A file with the appropriate name will be
	created and written to.
	"""
	with open(name, 'w+') as f:
		f.write(content)
		f.write("\n")
