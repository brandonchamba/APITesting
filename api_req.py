


import requests
url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

print(response.content)
print('-----')
print(response.headers)
print('---')
print(response)

# API Testing in python

# Fetch Response Header
# Fetch Specific response header content
# fetch Cookies
# Fetch Encoding
# Fetch Elapsed Time

print(response.headers.get("Date"))

# Fetch Response Content
# By using Json response

import json
#parse response to Json format
json_response = json.load(response.text)
print(json_response)
print(response.headers.Date.get("first_name"))
