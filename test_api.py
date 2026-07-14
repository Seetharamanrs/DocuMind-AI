import requests

url = "http://127.0.0.1:5000/ask"

payload = {
    "question": "What are the working hours?"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)