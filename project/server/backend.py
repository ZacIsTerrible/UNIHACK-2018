import time

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# Signing Access-Control-Allow-Origin. This is CRITICAL.
CORS(app)

# Data Stores
idToPatient = {}
idToDoctor = {}
doctorToPatient = {}
specialisationToPatients = {}
patientToProcedures = {}

# API
@app.route('/view_procedures', methods=['GET'])
def view_procedures():
    patient_id = request.args.get('patient_id')
    procedureList = []
    for procedure in patientToProcedures[patient_id]:
        procedureList.append(procedure[0]+":"+procedure[1]+":"+procedure[2]+":"+procedure[3])
    return jsonify(procedureList)

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
                patientList.append(patient['name']+":"+patient['patient_id']+":"+patient['priority']+":"+patient['accepted'])
        counter = counter + 1
    return jsonify(patientList)

@app.route('/get_patient', methods=['GET'])
def get_patient():
    patient_id = request.args.get('patient_id')
    return jsonify(idToPatient["patient_id"])

@app.route('/add_condition', methods=['POST'])
def add_condition():
	patient_id = request.args.get('patient_id')
	new_condition = request.args.get('condition')
	for patient in idToPatient:        
		if patient["patient_id"] == patient_id:
			patient["conditions"].append(new_condition)
			break

	# Return status. This is arbitary.
	return jsonify({ "status" : "success" })

@app.route('/accept_patient', methods=['POST'])
def accept_patient():
    patient_id = request.args.get('patient_id')
    doctor_id = request.args.get('doctor_id')
    doctorToPatient[doctor_id] = patient_id
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
    patientToProcedures[patient_id].append(doctor_id, timestamp, procedure_name, comments)

    # Return status. This is arbitary.
    return jsonify({ "status" : "success" })

@app.route('/pass_on', methods=['POST'])
def pass_on():
    patient_id = request.args.get('patient_id')
    old_doctor_id = request.args.get('old_doctor_id')
    new_doctor_id = request.args.get('new_doctor_id')
    specialty = idToDoctor[new_doctor_id][specialty]
    idToPatient[patient_id][accepted] = False
    specialisationToPatients[specialty] = idToPatient[patient_id]
    del doctorToPatient[old_doctor_id]

    # Return status. This is arbitary.
    return jsonify({ "status" : "success" })

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
    conditions = request.args.get('conditions')
    accepted = request.args.get('accepted')
    address = request.address.get('address')
    medical_history = request.address.get('medical_history')
    dietary_requirements = request.address.get('dietary_requirements')
    priority = request.address.get('priority')

    new_patient = {
    	'patient_id' : patient_id,
	   'name' : name,
	   'age' : age,
	   'gender' : gender,
	   'height' : height,
	   'weight' : weight,
	   'emergency_contact' : emergency_contact,
	   'health_insurance' : health_insurance,
	   	'conditions' : conditions.split(','),
	   	'accepted' : accepted,
	   	'address' : address,
	   	'medical_history' : medical_history,
	   	'dietary_requirements' : dietary_requirements,
	   	'priority' : priority
	}

	# Adding the patient to patient list.
    idToPatient[patient_id] = new_patient
    patientToProcedures[patient_id] = []

	# Return status. This is arbitary.
    return jsonify({ "status" : "success" })

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    doctor_id = request.args.get('doctor_id')
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    specialisation = request.args.get('specialisation')

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

	# Return status. This is arbitary.
    return jsonify({ "status" : "success" })

@app.route('/dummy')
def dummy():
    return jsonify({ "status" : "success" })

