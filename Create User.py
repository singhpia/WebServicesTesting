import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

a = requests.get(url)
print(a.content)
print(a.headers)
format = a.headers.get("Content-Type")
print(format)
if format == 'application/json; charset=utf-8':
    print("JSON response")
else:
    print("Response is not JSON")
    print("It is - ", format)

'''#post data / create data directly by passing body through parameter
body = {
    "name": "morpheus",
    "job": "leader"
}
c = requests.post(url, body)
print(c.status_code)
e = json.loads(c)
print(e.content)
if c.status_code==201:
    assert c.status_code==201
else:
    False
'''

#post data / create user through uploading json file
json_file = open("C:\\Users\\Prateek.THINKPAD\\Downloads\\Testing_JSONFile.JSON", 'r')
b = json_file.read()
c = json.loads(b)

#post user / create user / resource

d = requests.post(url, c)
print(d.content)
e = d.json()
print(e)
id = jsonpath.jsonpath(e, 'id')
print(id[0])