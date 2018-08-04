import time
import json
from pprint import pprint

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# Signing Access-Control-Allow-Origin. This is CRITICAL.
CORS(app)

# Data Stores
idToPatient = {}
idToDoctor = {}
specialisationToPatients = {}
patientToProcedures = {}
patientToProgress = {}




# API
@app.route('/get_progress', methods=['GET'])
def get_progress():
    return jsonify(patientToProgress[patient_id])

@app.route('/get_specialisations', methods=['GET'])
def get_specialisations():
    specialisations = []
    for specialisation in specialisationToPatients.keys():
        specialisations.append(specialisation)
    return jsonify(specialisations)

@app.route('/view_procedures', methods=['GET'])
def view_procedures():
    #may need to reverse order???
    patient_id = request.args.get('patient_id')
    return jsonify(patientToProcedures[patient_id])

@app.route('/get_patient_list', methods=['GET'])
def get_patient_list():
    doctor_id = request.args.get('doctor_id')
    specialisation = idToDoctor[doctor_id]['specialisation']
    patientQueue = specialisationToPatients[specialisation]
    patientList = []
    print("HERE")
    print(patientQueue)

    counter = 1
    while counter < 4:
        for patient in patientQueue:
            print("in for loop")
            print(patient)
            if patient['priority'] == counter:
                patientList.append(patient)
        counter = counter + 1
    return jsonify(patientList)

@app.route('/get_all_patients', methods=['GET'])
def get_all_patients():
    patientList = []
    for patient in idToPatient.values():
        patientList.append(patient)
    return jsonify(patientList)

@app.route('/get_patient', methods=['GET'])
def get_patient():
    patient_id = request.args.get('patient_id')
    print(patient_id)
    print(idToPatient)
    return jsonify(idToPatient[patient_id])

@app.route('/accept_patient', methods=['POST'])
def accept_patient():
    patient_id = request.args.get('patient_id')
    doctor_id = request.args.get('doctor_id')
    idToPatient[patient_id][accepted] = True
    patientToProcedures[patient_id] = []


	# Return status. This is arbitary.
    return jsonify({ "status" : "success" })

app.route('/add_procedure', methods=['POST'])
def add_procedure():
    doctor_id = request.args.get('doctor_id')
    procedure_name = request.args.get('procedure_name')
    comments = request.args.get('comments')
    timestamp = time.asctime( time.localtime(time.time()) )
    #get the list of sessions for this patient
    #get the most recent session
    #add to it to given procedure
    patientToProcedures[patient_id].append({
        'doctor_id':doctor_id,
        'timetstamp':timestamp,
        'procedure_name':procedure_name,
        'comments': comments
    })

    # Return status. This is arbitary.
    return jsonify({ "status" : "success" })

@app.route('/pass_on', methods=['POST'])
def pass_on():
    patient_id = request.args.get('patient_id')
    specialty = request.args.get('specialty')
    idToPatient[patient_id]['accepted'] = False
    specialisationToPatients[specialty].append(idToPatient[patient_id])

    # Return status. This is arbitary.
    return jsonify({ "status" : "success" })

@app.route('/assign', methods=['POST'])
def assign():
    patient_id = request.args.get('patient_id')
    specialty = request.args.get('specialty')
    idToPatient[patient_id]['accepted'] = False
    specialisationToPatients[specialty].append(idToPatient[patient_id])
    # Return status. This is arbitary.
    return jsonify({ "status" : "success" })

@app.route('/add_patient', methods=['POST'])
def add_patient():

	# Retrieve the new patient.
    patient_id = str(len(idToPatient))
    firstName = request.args.get('firstName')
    lastName = request.args.get('lastName')
    age = request.args.get('age')
    gender = request.args.get('gender')
    height = request.args.get('height')
    weight = request.args.get('weight')
    emergency_contact = request.args.get('emergency_contact')
    health_insurance = request.args.get('health_insurance')
    condition = request.args.get('condition')
    accepted = False
    address = request.args.get('address')
    priority = request.args.get('priority')
    bloodType = request.args.get('bloodType')

    if priority == "Low":
        priority = 3
    elif priority == "Mid":
        priority = 2
    elif priority == "High":
        priority = 1

    name = firstName + " " +lastName

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
	   	'priority' : priority,
        'bloodType' : bloodType
	}


	# Adding the patient to patient list.
    idToPatient[patient_id] = new_patient
    patientToProcedures[patient_id] = []

	# Return status. This is arbitary.
    return jsonify({ "status" : "success" })

def add_doctor(doctor_id, name, age, gender, specialisation):

    print(doctor_id + " " + name + " " + age + " " + gender + " " + specialisation)
    new_doctor = {
		'doctor_id' : doctor_id,
		'name' : name,
		'age' : age,
		'gender' : gender,
		'specialisation' : specialisation
	}
    idToDoctor[doctor_id] = new_doctor

	#if we haven't seen the specialisation before create a new PQ of patients
    if specialisation not in specialisationToPatients.keys():
        specialisationToPatients[specialisation] = []

@app.route('/save_progress', methods=['POST'])
def save_progress():
    step_number = request.args.get('step_number')
    task_description = request.args.get('task_description')
    timer = request.args.get('timer')
    patientToProgress[patient_id] = {
        "step_number": step_number,
        "task_decription": task_decription,
        "timer": timer
    }

@app.route('/dummy')
def dummy():
    return jsonify({ "status" : "success" })

with open('doctors.json') as f:
    data = json.load(f)

for doctor in data:
    add_doctor(doctor["doctor_id"], doctor["name"], str(doctor["age"]), doctor["gender"], doctor["specialisation"])

app.run()
