import requests
import json

url = "http://localhost:5000/hello"

r = requests.get(url)
print(r.text)


url = "http://localhost:5000/name"

payload = {'data': "CSUSM CS Department"}
headers = {
        'Content-Type': 'application/json'
    }
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.text , response.status_code)

