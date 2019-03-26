import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

print(response.content)
print('-----')
print(response.headers)
print('---')
print(response)

# API Testing in python

# Fetch Response Header  = GET
# Fetch Specific response header content
# fetch Cookies
# Fetch Encoding
# Fetch Elapsed Time

print(response.headers.get("Date"))

# Fetch Response Content
# By using Json response

#import json
#parse response to Json format

json_response = json.loads(response.text)

print(json_response)
# Fetch value using jsonpath
# Advance Json path
firstname= jsonpath.jsonpath(json_response,'data[0].first_name')
print (firstname[0])

lastname= jsonpath.jsonpath(json_response,'data[0].last_name')
print (lastname[0])

for i in range(0,3):
   #data[0].firstname
   firstname= jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
   print (firstname[0])

   lastname= jsonpath.jsonpath(json_response,'data['+str(i)+'].last_name')
   print (lastname[0])


#API Testing in Python
# Delete Resource
# Use delete method 
# Request =  Response = 204
url_delete = "https://reqres.in/api/users/2"
response = requests.delete(url)

#Fetch Response code

print (response.status_code)
assert response.status_code == 204


#API Testing in Python
# POST Resource   means create new user
# Use post method
# Request =  Response = 204
# base_url/post_method from server

#----------------------------------#
# 1. Create new Resource on Server
# 2. Use Post Method
#  ---  Request    and Response
# Steps:
# 1. Read Input json from file
# 2. Parse into json format
# 3. Hit Post method
# 4. Parse response to json format
# 5. Validate response

url_post = "https://reqres.in/api/users"
#read INput Json File

file = open("/Users/brandonchamba/code/CreateUser.json","r")
json_input = file.read()  #all string
request_json = json.loads(json_input)

print request_json

#Make POST request with Json Input body

response = requests.post(url, request_json)

print(response.content)
assert request.status.code == 201

#Fetch Header from response
print(response.headers.get('Content_Lenth'))

#Parse response to Json format
response_json = json.loads(response.text)

#Pick Id using Json Path
id = jsonpath.jsonpath(response_json,'id')  #will return the list all in one
print(id[0])


#-------------------------
# PUT resource.





url_post = "https://reqres.in/api/users"
#read INput Json File

file = open("/Users/brandonchamba/code/CreateUser.json","r")
json_input = file.read()  #all string
request_json = json.loads(json_input)

print request_json
#Make PUT (Update) request with Json input Body

response = requests.put(url, request_json)

print(response.content)
assert request.status.code == 201

#Fetch Header from response
print(response.headers.get('Content_Lenth'))

#Parse response to Json format
response_json = json.loads(response.text)

#Pick Id using Json Path
id = jsonpath.jsonpath(response_json,'id')  #will return the list all in one
print(id[0])

