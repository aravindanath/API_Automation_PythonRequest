import requests
import jsonpath
import json

baseURl = "https://reqres.in"
endpoint = "/api/users?page=2"

response = requests.get(baseURl+endpoint)
# response is in Object type

print(response.content)

#Parsing response to json format

json_response = json.loads(response.text)

print(json_response)

pages = jsonpath.jsonpath(json_response,"total_pages")

assert pages[0] == 2
print(pages)


