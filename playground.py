import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()
json = response.json() # {'message': 'success', 'iss_position': {'latitude': '20.1735', 'longitude': '-52.8828'}, 'timestamp': 1781509285}


print(json.get('iss_position').get('latitude'))