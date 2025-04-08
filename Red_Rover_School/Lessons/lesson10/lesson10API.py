from os import access

import requests
import json
#библиотека уникальных данных, имен emails etc
import uuid

BASE_URL = "https://simple-books-api.glitch.me"
#======================GET=================
# endpoint = f"{BASE_URL}/status"
#
# response = requests.get(f"{BASE_URL}/status", verify=False)
# print("Status Code:", response.status_code)
# print("Response:", response.json())
#
# params = {
#     "type": "fiction",
#     "limit": 3
# }
#
# response = requests.get(f"{BASE_URL}/books", params=params, verify=False)
# print("Books", response.json())
#
# book_id = 3
# response = requests.get(f"{BASE_URL}/books/{book_id}", verify=False)
# print("Book details", response.json())
#======================POST=================

unique_id = uuid.uuid4().hex[:6]
client_name = f"Student_{unique_id}"
client_email = f"student_{unique_id}@gmail.com"

headers = {"Content-Type":"application/json"}
payload = {
    'clientName': client_name,
    'clientEmail': client_email
}
response = requests.post(f"{BASE_URL}/api-clients",
                         headers=headers,
                         data=json.dumps(payload),
                         verify=False)
if response.status_code== 201:
    access_token = response.json().get("accessToken")
    print("Access Token:", access_token)
    print("Client Name", client_name)
    print("ClientEmail", client_email)
else:
    raise "Failed to get access token"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type":"application/json"
}
order_payload = {
    "bookId" : 1,
    "customerName": f"{client_name}"
}

response = requests.post(f"{BASE_URL}/orders",
                         headers=headers,
                         data=json.dumps(order_payload),
                         verify=False)

order = response.json()
print(order)

#all orders
response = requests.get(f"{BASE_URL}/orders",
                        headers=headers,
                        verify=False)
print("Orders", response.json())

#order by id
order_id = order['orderId']
response = requests.get(f"{BASE_URL}/orders/{order_id}",
                        headers=headers,
                        verify=False)
print("Order detail:", response.json())
print("Customer Name", response.json().get('customerName'))

#===========PaTCH============

unique_new_user = uuid.uuid4().hex[:6]
new_customer_name = f"UpdatedCustomer_{unique_new_user}"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

updated_payload = {
    "customerName": f"{new_customer_name}"
}
response = requests.patch(f"{BASE_URL}/orders/{order_id}",
                        headers=headers,
                        data=json.dumps(updated_payload),
                        verify=False)
print("Patch status code:", response.status_code)
print("Name new customer", new_customer_name)

response = requests.get(f"{BASE_URL}/orders/{order_id}",
                        headers=headers,
                        verify=False)
print("Order detail", response.json())
print("Get new customer :", response.json().get("customerName"))
