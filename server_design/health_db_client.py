import requests

server = "http://127.0.0.1:5000/"

new_patient = {"name": "Bob", "blood_type": "O+"}
r = requests.get(server + "/get_results/202")
print(r.status_code)
print(r.text)