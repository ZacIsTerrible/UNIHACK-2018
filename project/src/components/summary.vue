<template>
<div id="summary">
    <v-container grid-list-md>
        <h1 class="display-2 font-weight-medium">{{patient_name}}'s Medical Information</h1>
    </v-container>

</div>

</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

<script>
export default{
  name: 'summary',
  data () {
    return {
      patient_name: 'dkj',
      patient_summary: 'sdsdf'

    }
  }
}
</script>
