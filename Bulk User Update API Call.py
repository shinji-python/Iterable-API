import csv
from itertools import islice
import requests

#Create a variable to retrieve data field information for each user
def datafield_search(emails):


    with open ('se_assignment_users.csv', newline = '') as f:
        f.seek(0)
        records = csv.reader(f)
        for row in islice(records,0,50):
            if emails == row[2]:
                output=row
    return output

#Read and iterate through the first 50 users in the CSV to establish the body of the API request
with open ('se_assignment_users.csv', newline = '') as f:
    f.seek(0)
    reader = csv.reader(f)
    payload_data = []
    for row in islice(reader,1,50):
        emails = row[2]
        p_data = "{\n        {\n            \"email\":", emails,"\n            \"dataFields\": {", datafield_search(emails), "}," \
                    "\n            \"preferUserId\": true,\n            \"mergeNestedObjects\": true\n        }\n    ]\n}"
        payload_data.append(p_data)

#The API endpoint
url = "https://api.terable.com/api/users/bulkUpdate"

#This is where the correct API Key will be placed
querystring = {"api_key":"123"}

#This is the body of the API request
payload = "{\n    \"users\": ",payload_data,"}"

headers = {
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

#This will print the response code. We are looking for a successful code of '200'
print(response.text)
