"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object

if response.is_success:
    print(response.json())      # response object, json() method
#if response.status_code == True:

print(response.status_code)
print(response.encoding)
print(response.is_success)
#response.encoding
#response.text
# response.status_code
# responseis.is_succes