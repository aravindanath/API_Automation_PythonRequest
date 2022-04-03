import json

import requests
import jsonpath

baseURl = "https://reqres.in"
endpoint = "/api/users/2"

url = baseURl+endpoint


# Read input form json file

file = open("emp.json",'r')

json_input = file.read()

request_json =  json.loads(json_input)

print(request_json)

# Make post request with json input body

response = requests.put(url,request_json)

print(response.content)



json_response = json.loads(response.text)

print(json_response)

id = jsonpath.jsonpath(json_response,"id")
job = jsonpath.jsonpath(json_response,"job")

assert  response.status_code == 200
# assert job == "Automation Lead"
print(id)
print(job)
print(response.elapsed)


