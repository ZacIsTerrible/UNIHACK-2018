import time
import json
from pprint import pprint

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# Signing Access-Control-Allow-Origin. This is CRITICAL.
CORS(app)

# Data Stores
nursePQ = {}
idToPatient = {}
idToDoctor = {}
specialisationToPatients = {}
#doctorToPatient = {}
patientToProcedures = {}
patientToProgress = {}
count = 0



# API
@app.route('/get_doctor_name',methods=['GET'])
def get_doctor_name():
    doctor_id = request.args.get('doctor_id')
    doctor_name = idToDoctor[doctor_id]['name']
    return jsonify({"doctor_name":doctor_name})

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

    return jsonify({"counter":count})

@app.route('/get_patient_list', methods=['GET'])
def get_patient_list():
    doctor_id = request.args.get('doctor_id')
    specialisation = idToDoctor[doctor_id]['specialisation']
    patientQueue = specialisationToPatients[specialisation]
    patientList = []

    counter = 1
    while counter < 4:
        for patient in patientQueue:
            if patient['priority'] == counter:
                patientList.append(patient)
        counter = counter + 1
    return jsonify(patientList)

@app.route('/get_all_patients', methods=['GET'])
def get_all_patients():
    patient_list = []
    for patient in nursePQ.values():
        patient_list.append(patient)
    return jsonify(patient_list)

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
    #doctorToPatient[doctor_id] = patient_id

	# Return status. This is arbitary.
    return jsonify({ "status" : "success" })

@app.route('/add_procedure', methods=['POST'])
def add_procedure():
    global count
    doctor_id = request.args.get('doctor_id')
    #patient_id = doctorToPatient[doctor_id]

    doctor_name = idToDoctor[doctor_id]['name']
    count = count+1

    #get the list of sessions for this patient
    #get the most recent session
    #add to it to given procedure
    #patientToProcedures[patient_id].append({
    #    'doctor_id':doctor_id,
    #    'doctor_name':doctor_name,
    #    'count':count,
    #})

    # Return status. This is arbitary.
    return jsonify({ "status" : "success" })

@app.route('/pass_on', methods=['POST'])
def pass_on():
    old_doctor_id = request.args.get('doctor_id')
    patient_id = request.args.get('patient_id')
    specialty = request.args.get('specialisation')
    old_specialty = idToDoctor[old_doctor_id]['specialisation']
    specialisationToPatients[old_specialty].remove(idToPatient[patient_id])
    idToPatient[patient_id]['accepted'] = False
    specialisationToPatients[specialty].append(idToPatient[patient_id])
    # Return status. This is arbitary.
    return jsonify({ "status" : "success" })

@app.route('/assign', methods=['POST'])
def assign():
    patient_id = request.args.get('patient_id')
    specialty = request.args.get('specialisation')
    idToPatient[patient_id]['accepted'] = False
    specialisationToPatients[specialty].append(idToPatient[patient_id])
    del nursePQ[patient_id]
    # Return status. This is arbitary.
    return jsonify({ "status" : "success" })
def add(patient_id, name, age, gender, height, weight, emergency_contact, health_insurance, condition, address, priority, bloodType):
    if priority == "Low":
        priority = 3
    elif priority == "Mid":
        priority = 2
    elif priority == "High":
        priority = 1

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
	   	'accepted' : False,
	   	'address' : address,
	   	'priority' : priority,
        'bloodType' : bloodType
	}


	# Adding the patient to patient list.
    idToPatient[patient_id] = new_patient
    nursePQ[patient_id] = new_patient
    patientToProcedures[patient_id] = []

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
    nursePQ[patient_id] = new_patient
    patientToProcedures[patient_id] = []

	# Return status. This is arbitary.
    return jsonify({ "status" : "success" })

def add_doctor(doctor_id, name, age, gender, specialisation):

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

@app.route('/remove_patient', methods=['POST'])
def remove_patient():
    doctor_id = request.args.get('doctor_id')
    patient_id = request.args.get('patient_id')
    specialisation = idToDoctor[doctor_id]['specialisation']
    specialisationToPatients[specialisation].remove(idToPatient[patient_id])


@app.route('/dummy')
def dummy():
    return jsonify({ "status" : "success" })

with open('doctors.json') as f:
    data = json.load(f)

for doctor in data:
    add_doctor(doctor["doctor_id"], doctor["name"], str(doctor["age"]), doctor["gender"], doctor["specialisation"])

with open('patients.json') as f:
    data = json.load(f)

for patient in data:
    add(patient["patient_id"], patient["name"], patient["age"], patient["gender"], patient["height"], patient["weight"], patient["emergency_contact"], patient["health_insurance"], patient["condition"], patient["address"], patient["priority"], patient["blood_type"])

app.run()
