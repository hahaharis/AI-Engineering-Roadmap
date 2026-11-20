
import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
print("GitHub API working:", response.status_code == 200)
