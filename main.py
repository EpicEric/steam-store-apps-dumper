import files
import api


DUMPS_DIR = "dumps"


def main():
	"""
	Main function. TODO
	"""
	print("Hello, world!")
	files.save("dumps/teste.txt", "olar")
	return


def get_app_id():
	"""
	Gets the next app ID to collect data from.
	If it returns 0, it means there are no more apps to
	get data from.
	"""
	return 0


def save_app(app_id):
	"""
	Given an app ID, obtains the data from the API and
	saves it to the file named after it.
	"""
	str_app_id = str(app_id)
	try:
		content = api.get_app_details(str_app_id)
	except Exception as error:
		print('API error for app %s: %s' % (str_app_id, repr(error)))
	try:
		files.save("%s/%s.txt" % (DUMPS_DIR, str_app_id), content)
	except Exception as error:
		print('IO error for app %s: %s' % (str_app_id, repr(error)))


# Calls the main function
if __name__ == '__main__':
	main()
