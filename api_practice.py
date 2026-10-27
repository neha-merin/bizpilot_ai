import requests
url= "https://jsonplaceholder.typicode.com/todos/2"
response= requests.get(url)
print("Status Code:", response.status_code)
data= response.json()
print("API response:")
print(data)
print(data["completed"])