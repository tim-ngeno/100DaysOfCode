#!/usr/bin/env python3
"""Getting data from an API endpoint"""

import requests

# The endpoint url of the ISS API
endpoint = "http://api.open-notify.org/iss-now.json"


response = requests.get(endpoint)
if response.status_code != 200:
    response.raise_for_status()


print(response.json())
# Output: {'iss_position': {'longitude': '143.0338', 'latitude': '18.1086'},
# 'message': 'success', 'timestamp': 1721369022}


data = response.json()

# Filter the data to get the latitude and longitude
latitude = data.get("iss_position").get("latitude")
longitude = data.get("iss_position").get("longitude")

coordinates = (latitude, longitude)
print(coordinates)
