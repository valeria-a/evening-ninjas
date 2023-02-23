#
# Fundamentally, Base64 is used to encode binary data as printable text.
# This allows you to transport binary over protocols or mediums
# that cannot handle binary data formats and require simple text.
# Base64 uses 6-bit characters grouped into 24-bit sequences.


import base64
import json
import os
import pprint

print("https://classroom.google.com/u/0/c/NTYxNTc4MDk2ODc4".encode())

url_id = base64.urlsafe_b64encode(
    "https://classroom.google.com/u/0/c/NTYxNTc4MDk2ODc4".encode()).decode().strip("=")
print(url_id)


import requests
import os

url = "https://www.virustotal.com/api/v3/urls"

headers = {
    "x-apikey": "c22145b1a04f8e6b87aee05d902cd9faa46e73c2fa5c17ff30b068d638c59f23"
}

response = requests.get(url+"/"+url_id, headers=headers)
if response.status_code == 200:
    pprint.pprint(response.json())
else:
    print(response.status_code)


# with open(os.environ["VT_API"]) as fh:
#     all_keys = json.load(fh)

# print(all_keys)
#
# print(os.environ)


# print(os.environ["VT_API"])

# response = requests.post(url, headers=headers)

# print(response.text)

