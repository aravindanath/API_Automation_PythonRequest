import json

import requests
import jsonpath

baseURl = "https://reqres.in"
createuser = "/api/users"
getuser = "/api/users/"

url = baseURl+createuser


# Read input form json file

file = open("emp.json",'r')

json_input = file.read()

request_json =  json.loads(json_input)

print(request_json)

# Make post request with json input body

response = requests.post(url,request_json)

print(response.content)



json_response = json.loads(response.text)

print(json_response)

id = jsonpath.jsonpath(json_response,"id")
job = jsonpath.jsonpath(json_response,"job")

# assert job == "Automation Lead"
print(id)
print(job)


