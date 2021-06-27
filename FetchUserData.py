import requests

baseurl = "https://reqres.in"
path = "/api/users?page=2"

response = requests.get(baseurl+path)
#print(response.content)
#print(response.headers)
print(response.status_code)
if response.status_code == 200:
    print("Request ran successfully")
else:
    print("Request did not run")
