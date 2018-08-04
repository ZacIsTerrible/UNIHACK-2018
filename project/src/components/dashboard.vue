<style scoped>

#text-color {
    color:black;
}


</style>

<template>

<div id="dashboard">

    <v-app id="inspire">

        <v-container grid-list-md>
            <h1 class="display-2 font-weight-medium">{{patient_name}}'s Medical Information</h1>
            <br>
            <v-layout row wrap>
                <v-flex xs12>
                    <h2>Profile</h2>
                    <v-card dark color="white" id="text-color">
                        <v-card-text>Age: {{patient_age}}</v-card-text>
                        <v-card-text>Sex: {{patient_gender}}</v-card-text>
                        <v-card-text>Height: {{patient_height}}</v-card-text>
                        <v-card-text>Weight: {{patient_weight}}</v-card-text>
                        <v-card-text>Blood Type: {{patient_blood_type}}</v-card-text>
                    </v-card>
                </v-flex>

                <v-flex xs12>
                    <h2>Administrative Information</h2>
                    <v-card dark color="white" id="text-color">
                        <v-card-text>Address: {{patient_address}}</v-card-text>
                        <v-card-text>Emergency Contact: {{patient_emergency_contact}}></v-card-text>
                        <v-card-text>Health Insurance: {{patient_health_insurance}}</v-card-text>
                    </v-card>
                </v-flex>
                <v-flex xs12>
                    <h2>Current Condition</h2>
                    <v-card dark color="white" id="text-color">
                        <v-card-text>{{patient_current_condition}}</v-card-text>
                    </v-card>
                </v-flex>

            </v-layout>
            </v-layout>
            <h2>Actions</h2>
            <v-layout row wrap>
                <v-btn v-on:click="summary" color="secondary" flat>Summary</v-btn>
                <v-btn v-on:click="doctor_log" color="secondary" flat>Doctor Log</v-btn>
                <v-btn v-on:click="view_procedures" color="secondary" flat>View Procedures</v-btn>
                <v-btn color="secondary" v-on:click="pass_on" flat>Pass On</v-btn>
                <v-btn color="success" v-on:click="complete" flat>Complete</v-btn>
            </v-layout>
        </v-container>

    </v-app>


</div>

</template>

<script>

export default {
    name: 'dashboard',
    data() {
        return {
            patient: null,
            patient_name: null,
            patient_age: null,
            patient_gender: null,
            patient_height: null,
            patient_weight: null,
            patient_address: null,
            patient_emergency_contact: null,
            patient_health_insurance: null,
            patient_blood_type: null,
            patient_current_condition: null,
        }
    },

    methods: {

    },

    mounted: function() {
        this.$nextTick(function() {
            console.log(this.$route.params.id)
            this.axios
                .get("http://localhost:5000/get_patient?patient_id=" + this.$route.params.id)
                .then((response) => {
                    this.patient = response.data
                    this.patient_name= this.patient.name,
                    this.patient_age= this.patient.age,
                    this.patient_gender= this.patient.gender,
                    this.patient_height= this.patient.height,
                    this.patient_weight= this.patient.age,
                    this.patient_address= this.patient.address,
                    this.patient_emergency_contact= this.patient.emergency_contact,
                    this.patient_health_insurance= this.patient.health_insurance,
                    this.patient_blood_type= this.patient.bloodType,
                    this.patient_current_condition= this.patient.condition,

                    console.log(this.patient)
                })

        })
    }


}

</script>
