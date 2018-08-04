<style scoped>



</style>

<template>

<div id="dashboard">

    <v-app id="inspire">

        <v-container grid-list-md>
            <h1>{{patient_name}}'s Info</h1>
            <v-layout row wrap>
                <v-flex xs4>
                    <h2>Features</h2>
                    <v-card dark color="primary">
                        <v-card-text>Age: {{patient_age}}</v-card-text>
                        <v-card-text>Gender: {{patient_gender}}</v-card-text>
                        <v-card-text>Height: {{patient_height}}</v-card-text>
                        <v-card-text>Weight: {{patient_weight}}</v-card-text>
                        <v-card-text>Blood Type: {{patient_blood_type}}</v-card-text>
                        <v-card-text>Dietary Requirments: {{patient_dietary_requirments}}</v-card-text>
                    </v-card>
                </v-flex>

                <v-flex xs4>
                    <h2>Administrative Information</h2>
                    <v-card dark color = darkgray>
                        <v-card-text>Address: {{patient_address}}</v-card-text>
                        <v-card-text>Emergency Contact: {{patient_emergency_contact}}></v-card-text>
                        <v-card-text>Health Insurance: {{patient_health_insurance}}</v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>

            <v-layout row wrap>
              <v-flex xs8>
                  <h2>Medical History</h2>
                  <v-card dark color = darkgray>
                      <v-card-text>{{patient_medical_history}}</v-card-text>
                  </v-card>
              </v-flex>
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
            patient_name: 'Alex',
            patient_age: '16',
            patient_gender: 'Male',
            patient_height: '160cm',
            patient_weight: '61kg',
            patient_address: '67 Tree St, NSW',
            patient_emergency_contact: '0455739990',
            patient_health_insurance: 'Bupa',
            patient_blood_type: 'O-',
            patient_current_condition: 'Broken Arm',
            patient_medical_history: 'None',
            patient_dietary_requirments: 'None'

        }

    },
    computed: {
        binding() {
            const binding = {}

            if (this.$vuetify.breakpoint.mdAndUp) binding.column = true

            return binding
        }
    }

}

</script>
