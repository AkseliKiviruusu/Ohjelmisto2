import requests
import json

request = 'https://api.chucknorris.io/jokes/random'
response = requests.get(request).json()
print(f'\n{response['value']}')