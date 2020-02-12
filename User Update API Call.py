import requests
import csv
from itertools import islice

#Read the csv and pull back information on one user
with open ('se_assignment_users.csv', newline = '') as f:
    reader = csv.reader(f)
    for row in islice(reader, 1, 2):
        emails_var = row[2]
    #reset the csv read iteration
    f.seek(0)

    #Read the csv and provide the output as a dictionary for the data field
    records = csv.DictReader(f)
    dataFields_var = []
    for row in islice(records, 0, 1):
        dataFields_var = list(row.items())

#The API endpoint
url = "https://api.terable.com/api/users/update"

#This is where the correct API Key will be placed
querystring = {"api_key":"123"}

#This is the body of the API request
payload  = "{\n        {\n            \"email\":", emails_var,"\n            \"dataFields\":, {",dataFields_var," }," \
                    "\n            \"preferUserId\": true,\n            \"mergeNestedObjects\": true\n        }\n    ]\n}"

headers = {
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

#This will print the response code. We are looking for a successful code of '200'
print(response.text)
