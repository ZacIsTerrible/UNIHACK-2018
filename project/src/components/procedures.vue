<template>

    <div id="app">
    <v-app id="inspire">
      <v-layout row>
        <v-flex xs12 sm6 offset-sm3>
          <v-card>

            <v-list
              subheader
              two-line
            >
              <h1>Insert conditon here</h1>

              <v-list-tile @click="">
                <v-list-tile-action>
                  <v-checkbox v-model="check1"></v-checkbox>
                </v-list-tile-action>

                <v-list-tile-content @click="check1 = !check1">
                  <v-list-tile-title>check 1</v-list-tile-title>
                  <v-list-tile-sub-title>instruction</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>

              <v-list-tile @click="">
                <v-list-tile-action>
                  <v-checkbox v-model="check2"></v-checkbox>
                </v-list-tile-action>

                <v-list-tile-content @click="check2 = !check2">
                  <v-list-tile-title>check 2</v-list-tile-title>
                  <v-list-tile-sub-title>instruction</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>

              <v-list-tile @click="">
                <v-list-tile-action>
                  <v-checkbox v-model="check3"></v-checkbox>
                </v-list-tile-action>

                <v-list-tile-content @click="check3 = !check3">
                  <v-list-tile-title>check 3</v-list-tile-title>
                  <v-list-tile-sub-title>instruction</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>

              <v-list-tile @click="">
                <v-list-tile-action>
                  <v-checkbox v-model="check4"></v-checkbox>
                </v-list-tile-action>

                <v-list-tile-content @click="check4 = !check4">
                  <v-list-tile-title>check 4</v-list-tile-title>
                  <v-list-tile-sub-title>instruction</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>

              <v-list-tile @click="">
                <v-list-tile-action>
                  <v-checkbox v-model="check5"></v-checkbox>
                </v-list-tile-action>

                <v-list-tile-content @click="check5 = !check5">
                  <v-list-tile-title>check 5</v-list-tile-title>
                  <v-list-tile-sub-title>instruction</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>

              <v-list-tile @click="">
                <v-list-tile-action>
                  <v-checkbox v-model="check6"></v-checkbox>
                </v-list-tile-action>

                <v-list-tile-content @click="check6 = !check6">
                  <v-list-tile-title>check 6</v-list-tile-title>
                  <v-list-tile-sub-title>instruction</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>



            </v-list>

          </v-card>
        </v-flex>
      </v-layout>
    </v-app>
    <v-layout align-end justify-end row reverse fill-height/>
      <div>
        <v-btn color="orange darken-2" dark>
            <v-icon dark left>arrow_back</v-icon>Back
          </v-btn>
      </div>
  </div>


</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

<script>
import CheckListjson from '../../server/checklistData.json'
export default{
  name: 'procedures',
  data () {
    return {
      myList: CheckListjson
    }
  }
}
</script>
