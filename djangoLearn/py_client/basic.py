from http.client import ImproperConnectionState


import requests

endpoint = "http://127.0.0.1:8000/api/products/"

# get_reponse = requests.get(endpoint,params={'product_id': 123},json={'message':'client message'}) 
get_reponse = requests.get(endpoint) 

# print(get_reponse.json()) 
# print(get_reponse.text)
print(get_reponse.content)
print(get_reponse.status_code)