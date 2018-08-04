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
      <v-dialog v-model="dialog" persistent max-width="500px">
        <v-btn slot="activator" fab dark color="indigo">
            <v-icon dark>add</v-icon>
        </v-btn>
        <v-card>
          <v-card-title>
            <span class="headline">Patient Profile</span>
          </v-card-title>
          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12 sm6 md4>
                  <v-text-field label="Legal first name" required></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field label="Legal middle name" hint="example of helper text only on focus"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field
                    label="Legal last name"
                    hint="example of persistent helper text"
                    persistent-hint
                    required
                  ></v-text-field>
                </v-flex>
                <v-flex xs12>
                  <v-text-field label="Emergency Contact" required></v-text-field>
                </v-flex>

                <v-flex xs12 sm6>
                  <v-text-field label="Age" required></v-text-field>
                </v-flex>

                <v-flex xs12 sm6>
                  <v-select
                    :items="['Male', 'Female', 'Other']"
                    label="Gender"
                    required
                  ></v-select>
                </v-flex>

                <v-flex xs12 sm6>
                  <v-text-field label="Height" required></v-text-field>
                </v-flex>

                <v-flex xs12 sm6>
                  <v-text-field label="Weight" required></v-text-field>
                </v-flex>

                <v-flex xs12>
                  <v-select
                    :items="['O-Positive', 'O-Negative', 'A-Positive', 'A-Negative', 'B-Positive',
                     'B-Negative', 'AB-Positive', 'AB-Negative']"
                    label="Blood Types"
                    required
                  ></v-select>
                </v-flex>

                <v-flex xs12>
                  <v-text-field label="Address" required></v-text-field>
                </v-flex>

                <v-flex xs12>
                  <v-text-field label="Health insurance" required></v-text-field>
                </v-flex>


              </v-layout>
            </v-container>
            <small>*indicates required field</small>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" flat @click.native="dialog = false">Close</v-btn>
            <v-btn color="blue darken-1" flat @click.native="dialog = false">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

    </v-layout>

  </div>

</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

<script>
export default{
  name: 'patientsList',
  data: () => ({
    dialog: false
  })
}
</script>
