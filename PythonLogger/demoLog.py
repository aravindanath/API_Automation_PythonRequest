
import logging

logging.basicConfig(filename="automation.log", filemode='a', format='%(asctime)s  -%(message)s')

logging.warning("This will get loggeed to file")
logging.info("This will get loggeed to file")
logging.fatal("This will get loggeed to file")
logging.error("This will get loggeed to file")
logging.exception("This will get loggeed to file")

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

# print(request_json)
logging.warning(str(request_json))
# Make post request with json input body

response = requests.post(url,request_json)

logging.warning(response.content)



json_response = json.loads(response.text)

logging.warning(json_response)

id = jsonpath.jsonpath(json_response,"id")
job = jsonpath.jsonpath(json_response,"job")

# assert job == "Automation Lead"
logging.warning(id)
logging.warning(job)



