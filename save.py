
class Save(object):
	
	def save(self, name, content):
		with open('files/%s.txt' % name, 'w+') as f:
			f.write(content)
	

