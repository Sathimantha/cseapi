import requests

url = "https://www.cse.lk/api/allSecurityCode"

payload={}
headers = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
