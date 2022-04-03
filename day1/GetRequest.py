import requests
import jsonpath

baseURl = "https://reqres.in"
endpoint = "/api/users?page=2"

response = requests.get(baseURl+endpoint)
print(response)
print(response.content)
print(response.headers)