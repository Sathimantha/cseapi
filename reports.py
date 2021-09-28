import requests
import json

url = "https://www.cse.lk/api/financials"

payload = "symbol=ACL"
headers = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

response = requests.request("POST", url, headers=headers, data=payload)

data = json.loads(response.text)

infoAnnualData = data['infoAnnualData']

count = 0
for i in infoAnnualData:
    print(i.values())


# with open('data.txt', 'w') as f:
#    f.write(json.dumps(data['infoAnnualData'][1]['path'], indent=4, sort_keys=True))

# print(data['infoAnnualData'])
