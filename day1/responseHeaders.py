import requests
import jsonpath

baseURl = "https://reqres.in"
endpoint = "/api/users?page=2"

response = requests.get(baseURl+endpoint)


assert response.status_code == 200

print(response.headers)

# Specifc response header
print(response.headers.get("Content-Type"))
#
print(response.cookies)

print(response.encoding)

print(response.elapsed)