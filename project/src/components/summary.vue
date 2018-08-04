<template>
<div id="summary">
  <h1>{{patient_name}}</h1>
  <p>{{patient_summary}}</p>
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
