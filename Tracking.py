import requests
req = requests.get("http://api.open-notify.org/iss-now.json")
data = req.json()
loc = data["iss_position"]
lat = loc["latitude"]
long = loc["longitude"]