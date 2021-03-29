import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "api/user", {"name": "sean", "age": 28, "email": "testemail@email.com", "parentOrGuardian": "myself"})
print(response.json())
response = requests.post(BASE + "api/user", {"name": "sean", "age": 28, "email": "testemail@email.com"})
print(response.json())
response = requests.get(BASE + "api/user/1")
print(response.json())
response = requests.get(BASE + "api/user/2")
print(response.json())
response = requests.get(BASE + "api/users")
print(response.json())
response = requests.get(BASE + "api/user/10")
print(response.json())
