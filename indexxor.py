
import os
import datetime
import hashlib

def mlist(directory):
	collection = []
	files = [f for f in os.listdir(directory) if os.path.isfile(f)]
	for f in files:
		file = {}
		file_details = details(f)
		file.update({'name': f})
		file.update({'size': file_details.st_size})
		file.update({'text_size': size_fix(file_details.st_size)})
		file.update({'ctime': file_details.st_ctime})
		file.update({'atime': file_details.st_atime})
		file.update({'mtime': file_details.st_mtime})
		file.update({'text_ctime': str(datetime.datetime.fromtimestamp(file_details.st_ctime))[:19]})
		file.update({'text_atime': str(datetime.datetime.fromtimestamp(file_details.st_atime))[:19]})
		file.update({'text_mtime': str(datetime.datetime.fromtimestamp(file_details.st_mtime))[:19]})

		file.update({'sha256': get_hash(f)})
		collection.append(file)

	return collection

def details(file):
		det = os.stat(file)
		return det

def size_fix(size):
	unit = "&nbsp;B"
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
	return str(round(size,2)) + ' ' + unit

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

def generate_table(files, exclude):
	table = "<table>"
	th = "<tr>"
	th += "<th>" + 'No.' + "</th>"
	th += "<th>" + 'Name' + "</th>"
	th += "<th>" + 'Size' + "</th>"
	th += "<th>" + 'Created' + "</th>"
	th += "<th>" + 'Modified' + "</th>"
	th += "<th>" + 'SHA256' + "</th>"
	th += "</tr>"
	table += th

	for i in range(len(files)):
		if files[i]['name'] not in exclude:
			link = "<a href='" + files[i]['name'] + "'>" + files[i]['name'] + "</a>"

			tr = "<tr>"
			tr += "<td>" + str(i) + "</td>"
			tr += "<td class='left'>" + link + "</td>"
			tr += "<td class='right'>" + files[i]['text_size'] + "</td>"
			tr += "<td class='gcolor'>" + files[i]['text_ctime'] + "</td>"
			tr += "<td class='gcolor'>" + files[i]['text_mtime'] + "</td>"
			tr += "<td>" + files[i]['sha256'] + "</td>"
			tr += "</tr>"
			table += tr

	return table + "</table>"

def create_css():
	css = "<style>"
	css += "\
		table, th, td {\
		  font-family:Consolas,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New, monospace;\
		  padding-left: 0.4em;\
		  padding-right: 0.4em;\
		  padding-top: 0.2em;\
		  margin-left: 0.7em;\
		}\
	"
	css += "\
		.left {\
		  text-align: left;\
		}\
	"
	css += "\
		.right {\
		  text-align: right;\
		}\
	"
	css += "\
		.gcolor {\
		  color: gray;\
		}\
	"

	return css + "</style>"

def main():
	files = mlist('.')

	outfile = 'index.html'
	exclude = ['indexxor.py', outfile]

	with open(outfile, 'w+') as file:
		file.write( create_css() + generate_table(files, exclude))



if __name__ == "__main__":
		main()
