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

email = jsonpath.jsonpath(json_response,"data[0].email")


print(email)


