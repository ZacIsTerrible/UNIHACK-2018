from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# Signing Access-Control-Allow-Origin. This is CRITICAL.
CORS(app)

# Data Stores
idToPatient = {}
idToDoctor = {}
specialisationToPatients = {}


# API
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
				patientList.append(patient['name']+":"+patient['patient_id']+":"+patient['priority'])
		counter = counter + 1
	return jsonify(patientList)

@app.route('/get_patient', methods=['GET'])
def get_patient():
    patient_id = request.args.get('patient_id')
    return jsonify(idToPatient["patient_id"])

<<<<<<< HEAD
@app.route('/accept_patient', methods=['POST'])
def accept_patient():
    patient_id = request.args.get('patient_id')
    doctor_id = request.args.get('doctor_id')
    doctorToPatient[doctor_id] = patient_id
    idToPatient[patient_id][accepted] = True
    patientToProcedures[patient_id] = []

=======
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

@app.route('/assign_patient', methods=['POST'])
def assign_patient():
	patient_id = request.args.get('patient_id')
	doctor_id = request.args.get('doctor_id')
	specialty = idToDoctor[doctor_id][specialty]
	idToPatient[patient_id][accepted] = True
	heappq.heappush(specialisationToPatients[specialty], idToPatient[patient_id])
>>>>>>> 7d3be0975eecbda2f6ebdf443224366c6f8616a1

	# Return status. This is arbitary.
	return jsonify({ "status" : "success" })

@app.route('/add_patient', methods=['POST'])
def add_patient():

	# Retrieve the new patient.
    patient_id = len(idToPatient)
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
<<<<<<< HEAD
	   'name' : name,
	   'age' : age,
	   'gender' : gender,
	   'height' : height,
	   'weight' : weight,
	   'emergency_contact' : emergency_contact,
	   'health_insurance' : health_insurance,
	   	'condition' : condition,
=======
	    'name' : name,
	    'age' : age,
	    'gender' : gender,
	    'height' : height,
	    'weight' : weight,
	    'emergency_contact' : emergency_contact,
	    'health_insurance' : health_insurance,
	   	'conditions' : conditions.split(','),
>>>>>>> 7d3be0975eecbda2f6ebdf443224366c6f8616a1
	   	'accepted' : accepted,
	   	'address' : address,
	   	'priority' : priority,
        'bloodType' : bloodType
	}

    print(new_patient)

	# Adding the patient to patient list.
    idToPatient[patient_id] = new_patient

	# Return status. This is arbitary.
    return jsonify({ "status" : "success" })

@app.route('/add_doctor', methods=['POST'])
def add_doctor():

	doctor_id = request.args.get('doctor_id')
	name = request.args.get('name')
	age = request.args.get('age')
	gender = request.args.get('gender')
	specialisation = request.args.get('specialisation')

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
