import files
import api

DUMPS_DIR = "dumps"

def main():
	print("Hello, world!")
	files.save("dumps/teste.txt", "olar")
	return

def get_app_id():
	return 0

def save_app(app_id):
	str_app_id = str(app_id)

	try:
		content = api.get_app_details(str_app_id)
	except Exception as error:
		print('API error for app %s: %s' % (str_app_id, repr(error)))

	try:
		files.save("%s/%s.txt" % (DUMPS_DIR, str_app_id), content)
	except Exception as error:
		print('IO error for app %s: %s' % (str_app_id, repr(error)))

if __name__ == '__main__':
	main()
