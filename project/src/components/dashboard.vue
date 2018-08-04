<style scoped>



</style>

<template>

<div id="dashboard">

    <v-app id="inspire">

        <v-container grid-list-xl>
            <h1>Patient Info</h1>
            <h2>Administration Information</h2>
            <v-layout v-bind="binding">
                <v-flex>
                    <v-card dark color="primary">
                        <v-card-text>Name: {{patient_name}}</v-card-text>
                    </v-card>
                </v-flex>
                <v-flex>
                    <v-card dark color="secondary">
                        <v-card-text>Age: {{patient_age}}</v-card-text>
                    </v-card>
                </v-flex>
                <v-flex>
                    <v-card dark color="accent">
                        <v-card-text>Gender: {{patient_gender}}</v-card-text>
                    </v-card>
                </v-flex>
                <v-flex>
                    <v-card dark color="accent">
                        <v-card-text>Height: {{patient_height}}</v-card-text>
                    </v-card>
                </v-flex>
                <v-flex>
                    <v-card dark color="accent">
                        <v-card-text>Weight: {{patient_weight}}</v-card-text>
                    </v-card>
                </v-flex>
                <v-flex>
                    <v-card dark color="accent">
                        <v-card-text>Address: {{patient_address}}</v-card-text>
                    </v-card>
                </v-flex>

                <v-flex>
                    <v-card dark color="accent">
                        <v-card-text>Emergency Contact: {{patient_emergency_contact}}</v-card-text>
                    </v-card>
                </v-flex>

                <v-flex>
                    <v-card dark color="accent">
                        <v-card-text>Health Insurance: {{patient_health_insurance}}</v-card-text>
                    </v-card>
                </v-flex>

                <v-flex>
                    <v-card dark color="accent">
                        <v-card-text>Blood Type: {{patient_blood_type}}</v-card-text>
                    </v-card>
                </v-flex>

                <v-flex>
                    <v-card dark color="accent">
                        <v-card-text>Current Condition: {{patient_current_condition}}</v-card-text>
                    </v-card>
                </v-flex>

                <v-flex>
                    <v-card dark color="accent">
                        <v-card-text>Medical History: {{patient_medical_history}}</v-card-text>
                    </v-card>
                </v-flex>

                <v-flex>
                    <v-card dark color="accent">
                        <v-card-text>Dietary Requirements: {{patient_dietary_requirments}}</v-card-text>
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
            patient_name: 'alex',
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
