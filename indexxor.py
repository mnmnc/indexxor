
import os
import datetime
import hashlib

def mlist(directory):
	files = [f for f in os.listdir(directory) if os.path.isfile(f)]
	for f in files:
		print(f)
		print(details(f).st_ctime)
		print(datetime.datetime.fromtimestamp(details(f).st_ctime))
		print(details(f).st_atime)
		print(datetime.datetime.fromtimestamp(details(f).st_atime))
		print(details(f).st_mtime)
		print(datetime.datetime.fromtimestamp(details(f).st_mtime))

		print(details(f).st_size)
		print(size_fix(details(f).st_size))

		print(get_hash(f))
		print()


def details(file):
		det = os.stat(file)
		return det

def size_fix(size):
	unit = "B"
	if size > 1024:
		size /= 1024
		unit = "KB"
	if size > 1024:
		size /= 1024
		unit = "MB"
	if size > 1024:
		size /= 1024
		unit = "GB"
	if size > 1024:
		size /= 1024
		unit = "TB"
	return str(size) + ' ' + unit

def get_hash(file):
	f = open(file, "rb")
	sha = hashlib.sha256()
	while True:
		data = f.read(2 ** 20)
		if not data:
			break
		sha.update(data)
	f.close()

	return sha.hexdigest()


def main():
	mlist('.')





if __name__ == "__main__":
		main()
