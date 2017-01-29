import requests

r = requests.get('http://alainwebdesign.ca')
if r.status_code == 200:
	print ("success")

else:
	print ("something went wrong")
