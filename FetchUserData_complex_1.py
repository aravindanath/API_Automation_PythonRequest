import requests
import jsonpath
import json

baseURl = "https://reqres.in"
endpoint = "/api/users?page=2"

response = requests.get(baseURl+endpoint)


json_response = json.loads(response.text)


for i in range(0,5):
    email = jsonpath.jsonpath(json_response,"data["+str(i)+"].first_name")
    print(email)




