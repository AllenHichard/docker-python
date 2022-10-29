import requests
import json

print(json.dumps({"name":"Naruto"}))

print(requests.get("http://localhost:3000/").text)

headers = {
    "Content-Type": "application/json"
}

print(requests.post("http://localhost:3000/insert", headers = headers, data=json.dumps({"name":"Naruto"})).text)