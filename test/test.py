import requests
import json

print(json.dumps({"name":"Naruto"}))

print(requests.get("http://localhost:3000/").text)

print(requests.post("http://localhost:3000/insert", data=json.dumps({"name":"Naruto"})).text)