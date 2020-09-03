##############################################################
# Project : AugmentedCISO Public API
# Author : EXCUBE (contact@excube.fr)
##############################################################
import json

import requests

# Change these to match your needs
API_KEY = 'YOU_API_KEY'

# This sample walk you though the update of one metric value

# Required headers with authorization
headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': API_KEY}

BASE_URL = "https://api.augmentedciso.com/api/public"

print("# Get key information")

# send key in header (safer)
response = requests.get(BASE_URL + '/me', headers=headers)
print(response.json())

print('# List all available metrics')
response = requests.get(BASE_URL + '/metrics', headers=headers)
print(response.json())
print()

selected_perimeter = input('Please type a perimeter identifier and press Enter\n')
selected_metric = input('Please type a metric identifier you which to update and press Enter\n')
value = input('Please type a value\n')
try:
    value = int(value)
except:
    print("Value must be an integer")
    exit(0)

print('# Update selected value')
to_send = {
    "metrics": [
        {
            "metric_id": selected_metric,
            "perimeter_id": selected_perimeter,
            "value": value
        }
    ]
}
print(to_send)
response = requests.put(BASE_URL + '/metrics', data=json.dumps(to_send), headers=headers)
print(response.json())

print('# Check value')
response = requests.get(BASE_URL + '/metrics/%s/%s' % (selected_perimeter, selected_metric), headers=headers)
print(response.json())
print()
