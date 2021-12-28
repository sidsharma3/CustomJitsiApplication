import requests
# local host
BASE = "http://127.0.0.1:5000/"
# first train model with a post request
requests.post(BASE + "predict")
# now get request to use model
response = requests.get(BASE + "predict")
print(response.json())
