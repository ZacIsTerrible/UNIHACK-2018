from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# Signing Access-Control-Allow-Origin. This is CRITICAL.
CORS(app)

# Data Stores
patientList = []



# API
@app.route('/get_patient_list', methods=['GET'])
def get_patient_list():
    return jsonify(patientList)

@app.route('/get_patient_list', methods=['GET'])

@app.route('/add_patient', methods=['POST'])
def add_patient():

	# Retrieve the new patient.
	patient_id = request.args.get('patient_id')
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    height = request.args.get('height')
    weight = request.args.get('weight')
    emergency_contact = request.args.get('emergency_contact')
	health_insurance = request.args.get('health_insurance')
    condition = request.args.get('condition')
    accepted = request.args.get('accepted')
    address = request.address.get('address')
    medical_history = request.address.get('medical_history')
    dietary_requirements = request.address.get('dietary_requirements')

    new_patient = {
    	'patient_id' : patient_id,
	    'name' : name,
	    'age' : age,
	    'gender' : gender,
	    'height' : height,
	    'weight' : weight,
	    'emergency_contact' : emergency_contact,
	    'health_insurance' : health_insurance,
	   	'condition' : condition,
	   	'accepted' : accepted,
	   	'address' : address,
	   	'medical_history' : medical_history,
	   	'dietary_requirements' : dietary_requirements
	}

	# Adding the patient to patient list.
	patientList.append(new_patient)

	# Return status. This is arbitary.
	return jsonify({ "status" : "success" })


