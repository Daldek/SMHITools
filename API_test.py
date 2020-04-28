import requests

# https://opendata-download-hydroobs.smhi.se/api/version/{version}/parameter/{parameter}/station/{station}/period/{period}/data.{ext}
# 2284 - Byske
url = 'https://opendata-download-hydroobs.smhi.se/api/version/latest/parameter/1/station/2284/period/latest-day/data.json'
r = requests.get(url)
response_dict = r.json()

print("Kod stanu: ", r.status_code)
print(response_dict)
