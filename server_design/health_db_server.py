from distutils.log import error
from flask import Flask, request, jsonify

app = Flask(__name__)

db  = []

def add_patient_to_db(name, id, blood_type):
    new_patient = {"name": name, "id": id, "blood_type": blood_type, "tests": {}}
    db.append(new_patient)
    return True

def init_server():
    add_patient_to_db("ann Ables", 101, "A+")
    add_patient_to_db("Bob Boyles", 202, "B-")


@app.route("/add_patient", methods=["POST"])
def add_patient():
    in_data = request.get_json()
    answer = add_patient_driver(in_data)
    return jsonify(answer)

def add_patient_driver(in_data):
    answer, status_code = validate_add_patient_input(in_data)
    if status_code != 200:
        return answer, status_code
    add_patient_to_db(in_data["name"], in_data["id"], in_data["blood_type"])
    return True

def validate_add_patient_input(in_data):
    expected_keys = ["name", "id", "blood_type"]
    for key in expected_keys:
        if key not in in_data:
            error_message = "Key {} is missing".format(key)
            return error_message, 400
    return True, 200

@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results(patient_id):
    print(patient_id)
    for patient in db:
        if patient["id"] == int(patient_id):
            return jsonify(patient), 200
    return "patient id {} is not in database".format(patient_id), 400

init_server()
app.run()
