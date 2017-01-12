def save(name, content):
	with open(name, 'w+') as f:
		f.write(content)
		f.write("\n")
