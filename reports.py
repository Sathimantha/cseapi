import requests
import json
import csv

url = "https://www.cse.lk/api/financials"

payload = "symbol=ACL"
headers = {
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)


data = json.loads(response.text)
infoAnnualData = data['infoAnnualData']
infoQuarterlyData= data['infoQuarterlyData']

data_file = open('data_file.csv', 'w')
csv_writer = csv.writer(data_file)

count = 0
 
for i in infoAnnualData:
    if count == 0:
 
        # Writing headers of CSV file
        header = i.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(i.values())


 
data_file.close()
