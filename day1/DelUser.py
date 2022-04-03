import requests
import jsonpath
import json

baseURl = "https://reqres.in"
endpoint = "/api/users/2"

response  = requests.delete(baseURl+endpoint)

print(response.status_code)

assert response.status_code == 204



