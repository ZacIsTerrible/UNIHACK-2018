<template>

<div id="dashboard">
  <h1>Patient Info</h1>

  <h2>Administration Information</h2>
  <h3>Name: {{patient_name}}</h3>
  <h3>Age: {{patient_age}}</h3>
  <h3>Gender: {{patient_gender}}</h3>
  <h3>Height: {{patient_height}}</h3>
  <h3>Weight: {{patient_weight}}</h3>
  <h3>Address: {{patient_address}}</h3>
  <h3>Emergency Contact: {{patient_emergency_contact}}</h3>
  <h3>Health Insurance: {{patient_health_insurance}}</h3>
  <h3>Blood Type: {{patient_blood_type}}</h3>
  <h3>Current Condition: {{patient_current_condition}}</h3>
  <h3>Medical History: {{patient_medical_history}}</h3>
  <h3>Dietary Requirements: {{patient_dietary_requirments}}</h3>
</div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

<script>
export default{
  name: 'dashboard',
  data () {
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
  }

}
</script>
