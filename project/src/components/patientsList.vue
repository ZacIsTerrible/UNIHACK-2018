<!-- made by Nick-->
<template>
  <div id="app">
    <div
      id="e3"
      style="max-width: 1000px; margin: auto;"
      class="grey lighten-3"
    >
      <v-card>
        <v-container
          fluid
          grid-list-lg
        >
          <v-layout align-center justify-start row fill-height>


            <v-flex xs12>
              <v-card color="blue-grey darken-2" class="white--text">
                <v-card-title primary-title>
                  <div class="headline">Patient 1 name</div>
                </v-card-title>
                <v-card-actions>
                  <v-btn flat dark>Accept</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>

            <v-flex xs12>
              <v-card color="blue-grey darken-2" class="white--text">
                <v-card-title primary-title>
                  <div class="headline">Patient 2 name</div>
                </v-card-title>
                <v-card-actions>
                  <v-btn flat dark>Accept</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>

            <v-flex xs12>
              <v-card color="blue-grey darken-2" class="white--text">
                <v-card-title primary-title>
                  <div class="headline">Patient 3 name</div>
                </v-card-title>
                <v-card-actions>
                  <v-btn flat dark>Accept</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>

            <v-flex xs12>
              <v-card color="blue-grey darken-2" class="white--text">
                <v-card-title primary-title>
                  <div class="headline">Patient 4 name</div>
                </v-card-title>
                <v-card-actions>
                  <v-btn flat dark>Accept</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>

            <v-flex xs12>
              <v-card color="blue-grey darken-2" class="white--text">
                <v-card-title primary-title>
                  <div class="headline">Patient 5 name</div>
                </v-card-title>
                <v-card-actions>
                  <v-btn flat dark>Accept</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>


          </v-layout>
        </v-container>
      </v-card>
    </div>
    <v-layout align-end justify-end row fill-height>
      <v-btn fab dark color="indigo">
          <v-icon dark>add</v-icon>
      </v-btn>
    </v-layout>
  </div>

</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

<script>
export default{
  name: 'patientsList'
}
</script>
