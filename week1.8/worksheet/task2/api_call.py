
import httpx

base_url = "https://dummyjson.com/"

#content1 = "posts/5"
content = "products/search?q=apple"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

#content1 = response.json()   # JSON data

#print(content1)

data = response.json()
print(content)
print("Total matching products:", data["total"])
print("Products returned in this call:", len(data["products"]))
#print(data["reactions"]["likes"])