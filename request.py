import requests
response = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/sy223")
type1 = response.json()["Recipient"]
type2 = response.json()["Donor"]
response = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M1")
print(response.text)
response = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F5")
print(response.text)
data = {"Name":"sy223", "Match": "Yes"}
response = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=data)
print(response.text)
