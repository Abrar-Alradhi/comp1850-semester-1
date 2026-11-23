
import httpx

base_url = "https://dummyjson.com/"


content = "recipes/meal-type/snack"

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response


data = response.json()
for recipe in data["recipes"]:
    print(recipe["name"], "->", recipe["difficulty"])


