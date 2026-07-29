#The requests library is the most popular Python library for making HTTP requests. It provides a simple and elegant interface for interacting with REST APIs and websites.

import requests
#get-request
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)
print("\n")
print(response.text)
print("\n")
print(response.reason)
print("\n")
print(response.headers)
print("\n")
print(response.content)
print("\n")
print(response.json())
print("\n")

# #get request with query parameters
# params = {
#     "q": "python",
#     "page": 2
# }
# response = requests.get("https://httpbin.org/get",params=params)
# print(response.url)
# print(response.json())

#post request
# data = {
#     "name": "Alice",
#     "age": 25
# }

# response = requests.post("https://httpbin.org/post",data=data)  #requests.post(url, json=data)

# print(response.json())

#params and headers
# params = {
#     "search": "python"
# }
# headers = {
#     "Accept": "application/json"
# }
# response = requests.get("https://httpbin.org/get",params=params,headers=headers)
# print(response.json())

#handling errors
# try:
#     response = requests.get("https://httpbin.org/status/404")
#     response.raise_for_status()

# except requests.exceptions.HTTPError as e:
#     print(e)

#full example
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Accept": "application/json"
}

params = {
    "userId": 1
}

try:
    response = requests.get(
        BASE_URL,
        headers=headers,
        params=params,
        timeout=5
    )

    response.raise_for_status()    #instead of checking every status code manually

    posts = response.json()

    for post in posts:
        print(post["title"])

except requests.exceptions.RequestException as e:
    print("Request failed:", e)