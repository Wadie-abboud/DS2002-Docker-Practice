import requests
import json
import datetime

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)
r = response.json()
timestamp = r['timestamp']
datetime = datetime.datetime.fromtimestamp(timestamp)
dtime = datetime.strftime('%Y-%m-%d-%H:%M:%S')

long = r['iss_position']['longitude']
lat = r['iss_position']['latitude']
print(dtime)
print(long)
print(lat)