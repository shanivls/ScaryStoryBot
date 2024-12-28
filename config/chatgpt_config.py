

import requests

url = "https://chatgpt-api.shn.hk/v1/"
headers = {
    "Content-Type": "application/json"
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello, how are you?"}]
}

response = requests.post(url, headers=headers, json=data)

# Print the response from the API
print(response.json())