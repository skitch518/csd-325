import requests
import json

# API key
response = requests.get('https://pokeapi.co/api/v2/generation/?limit=2')

# Fomatting the response
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Printing the response
jprint(response.json())