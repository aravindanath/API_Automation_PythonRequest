import requests
import jsonpath

baseURl = "https://reqres.in"
endpoint = "/api/users?page=2"

response = requests.get(baseURl+endpoint)
print(response.status_code)

assert response.status_code == 200

