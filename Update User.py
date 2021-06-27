import requests

url = "https://reqres.in/api/users/2"
file = open("C:\\Users\\Prateek.THINKPAD\\Downloads\\Testing_JSONFile.JSON", 'r')
response = file.read()
put_response = requests.put(url, response)
a = put_response.json()
print(a)
