import time

import files
import api


DUMPS_DIR = "dumps"
index = 0


def main():
	"""
	Main function. First, it collects the most recent
	app list; then, it finds the last obtained app;
	and finally, it iterates over the app list for new
	apps until done or canceled by user.
	"""
	print("Getting updated app list..."),
	array = api.get_app_list()
	print("Done.")

	print("Finding last added app..."),
	last_app_id = files.get_app_id(DUMPS_DIR)
	app_id = next_app_id(last_app_id, array)
	if app_id is None:
		print("No new apps. Ending program...")
		return
	print("Done.")

	print("\nStarting from app {}.".format(app_id))
	print("Hit CTRL-C to stop this program at any time.\n")
	
	while (app_id is not None):
		print("{}: Saving...".format(app_id)),
		save_app(app_id)
		time.sleep(1.2) # API max request time
		print("Done")
		app_id = next_app_id(app_id, array)


def next_app_id(app_id, array):
	"""
	Receives the current app_id and returns the next
	one from the array. Returns None if it already is
	the last one.
	"""
	if app_id is None:
		return None
	if app_id == 0:
		return array[0]['appid']
	global index
	for i, v in enumerate(array[index::]):
		if v['appid'] > app_id:
			index = index + i + 1
			return v['appid']
	return None


def save_app(app_id):
	"""
	Given an app ID, obtains the data from the API and
	saves it to the file named after it.
	"""
	str_app_id = str(app_id)
	content = api.get_app_details(str_app_id)
	files.save("{}/{}.txt" .format(DUMPS_DIR, str_app_id), content)


# Calls the main function
if __name__ == '__main__':
	main()
