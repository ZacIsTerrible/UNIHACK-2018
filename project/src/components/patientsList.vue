<style scoped>

#patient-flex {
    padding: 20px;
}

#add-positioner {
    position: fixed;
    right: 20px;
    bottom: 0px;
}

#time-info {
    color: grey;
}

#grey {
    background-color: #F5F5F5;
}

</style>

<template>

<div id="app">
    <div id="container">
        <v-container grid-list-xl text-xs-left>
            <v-layout row wrap>
                <v-flex v-for="patient in patients" xs4 id="patient-flex">
                    <v-card id="patient-card">
                        <v-card-title>
                            <div id="chat-container">
                                <span class="title">{{patient.name}}</span>
                                <br>
                                <span class="body-1" id="time-info">{{patient.priority}}</span>
                            </div>
                        </v-card-title>
                        <div id="grey">
                            <v-card-actions>

                                <v-dialog v-model="assignDialog" persistent max-width="500px">

                                    <v-btn slot="activator" flat color="secondary">Assign Specialist</v-btn>
                                    <v-card>
                                        <v-card-title>
                                            <span class="headline">Select Specialist</span>
                                        </v-card-title>
                                        <v-card-text>
                                            <v-container grid-list-md>
                                                <v-layout wrap>
                                                    <v-flex xs12 sm6>
                                                        <v-autocomplete :items="specialists" v-model="selectedSpecialist" label="Specialists" required></v-autocomplete>
                                                    </v-flex>
                                                </v-layout>
                                            </v-container>
                                        </v-card-text>
                                        <v-card-actions>
                                            <v-spacer></v-spacer>
                                            <v-btn color="blue darken-1" flat @click.native="assignDialog = false" id="close1">Close</v-btn>
                                            <v-btn color="blue darken-1" flat @click.native="assignDoctor(patient)">Save</v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>
                            </v-card-actions>
                        </div>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>












    <div id="add-positioner">
        <v-container>
            <v-layout align-end justify-end row fill-height>
                <v-dialog v-model="dialog" persistent max-width="500px">
                    <v-btn slot="activator" fab dark color="secondary">
                        <v-icon dark>add</v-icon>
                    </v-btn>
                    <v-card>
                        <v-card-title>
                            <span class="headline">Patient Profile</span>
                            <v-container grid-list-xl>
                                <v-layout wrap>
                                    <v-flex xs12 sm6 md4>
                                        <v-text-field label="Legal first name" v-model="firstName" required></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm6 md4>
                                        <v-text-field label="Legal last name" v-model="lastName" persistent-hint required></v-text-field>
                                    </v-flex>
                                    <v-flex xs12>
                                        <v-text-field label="Emergency Contact" v-model="emergencyContact" required></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm6 md4>
                                        <v-text-field label="Condition" v-model="condition"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12 sm6>
                                        <v-text-field label="Age" v-model="age" required></v-text-field>
                                    </v-flex>

                                    <v-flex xs12 sm6>
                                        <v-select :items="['Male', 'Female', 'Other']" label="Gender" required v-model="gender"></v-select>
                                    </v-flex>

                                    <v-flex xs12 sm6>
                                        <v-text-field label="Height" required v-model="height"></v-text-field>
                                    </v-flex>

                                    <v-flex xs12 sm6>
                                        <v-text-field label="Weight" required v-model="weight"></v-text-field>
                                    </v-flex>
                                    <v-flex xs12>
                                        <v-select :items="['Low', 'Mid', 'High']" label="Priority" required v-model="priority"></v-select>
                                    </v-flex>

                                    <v-flex xs12>
                                        <v-select :items="['O-Positive', 'O-Negative', 'A-Positive', 'A-Negative', 'B-Positive',
                             'B-Negative', 'AB-Positive', 'AB-Negative']" label="Blood Types" required v-model="bloodType"></v-select>
                                    </v-flex>

                                    <v-flex xs12>
                                        <v-text-field label="Address" required v-model="address"></v-text-field>
                                    </v-flex>

                                    <v-flex xs12>
                                        <v-text-field label="Health insurance" required v-model="insurance"></v-text-field>
                                    </v-flex>


                                </v-layout>
                            </v-container>
                        </v-card-title>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="blue darken-1" flat @click.native="dialog = false" id="close2">Close</v-btn>
                            <v-btn color="blue darken-1" flat @click.native="addPatient">Save</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-layout>
        </v-container>
        <v-snackbar v-model="snackbar" color="success" multi-line="multi-line" timeout="4000">
            Successully {{ text }}!
            <v-btn dark flat @click="snackbar = false">
                Close
            </v-btn>
        </v-snackbar>
    </div>
</div>

</template>

<style scoped>
</style>

<script>

export default {
    name: 'patientsList',
    data() {
        return {
            dialog: false,
            assignDialog: false,
            snackbar: false,
            firstName: null,
            condition: null,
            lastName: null,
            emergencyContact: null,
            age: null,
            gender: null,
            height: null,
            weight: null,
            priority: null,
            address: null,
            insurance: null,
            bloodType: null,
            patients: [],
            specialists: [],
            selectedSpecialist: null,
            text: null,
        }
    },

    methods: {
        addPatient: function() {
            var ajax_request_first_half = "http://localhost:5000/add_patient?firstName=" + this.firstName + "&lastName=" + this.lastName + "&emergency_contact=" + this.emergencyContact + "&age=" + this.age + "&gender=" + this.gender + "&height=" + this.height + "&weight=" + this.weight
            var ajax_request = ajax_request_first_half + "&address=" + this.address + "&health_insurance=" + this.insurance + "&priority=" + this.priority + "&bloodType=" + this.bloodType + "&condition=" + this.condition;

            console.log(ajax_request)

            this.axios.post(ajax_request)
                .then(function(response) {
                    console.log(response);
                }).catch(error => {
                    console.log(error.response)
                });
            this.text = "Added New Patient"
            this.snackbar = true
            document.getElementById("close2").click()
        },
        assignDoctor: function(patient) {
            var ajax_request = "http://localhost:5000/assign?patient_id=" + patient.patient_id + "&specialty=" + this.selectedSpecialist

            this.axios.post(ajax_request)
                .then(function(response) {
                    console.log(response);
                }).catch(error => {
                    console.log(error.response)
                });

            this.text = "Assigned Patient to Specialist"
            this.snackbar = true
            document.getElementById("close1").click()

        },
    },

    mounted: function() {

        this.$nextTick(function() {
            this.axios
                .get("http://localhost:5000/get_all_patients")
                .then((response) => {
                    this.patients = response.data
                })
            this.axios
                .get("http://localhost:5000/get_specialisations")
                .then((response) => {
                    this.specialists = response.data
                })
        })
    }
}

</script>
