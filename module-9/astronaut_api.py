import requests
import json

#api request
response = requests.get("http://api.open-notify.org/astros.json")

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# print the formatted string
jprint(response.json())