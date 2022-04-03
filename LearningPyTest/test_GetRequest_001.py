import requests
import jsonpath

baseURl = "https://reqres.in"
endpoint = "/api/users?page=2"

def test_getReq_001():
    response = requests.get(baseURl+endpoint)
    print(response)
    print(response.content)
    print(response.headers)
    assert 200 == 100