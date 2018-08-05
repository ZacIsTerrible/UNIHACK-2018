<style scoped>



</style>

<template>

<div id="app">
    <v-app id="inspire">
        <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
                <v-card>

                    <v-list v-for="data in myJson" three-line>

                        <v-list-tile>
                            <v-list-tile-action @click="add_procedure(data.Step_Number)">
                                <v-checkbox v-bind:id="data.Step_Number"></v-checkbox>
                            </v-list-tile-action>

                            <v-list-tile-content @click="check = !check">
                                <v-list-tile-title>{{ data.Step_Number }}) {{ data.Task_Description }}</v-list-tile-title>
                                <v-list-tile-sub-title>Time Required: {{data.Timer}}</v-list-tile-sub-title>

                            </v-list-tile-content>
                        </v-list-tile>

                    </v-list>

                </v-card>

            </v-flex>
            <div>
                <v-btn color="orange darken-2" dark v-on:click="back">
                    <v-icon  dark left>arrow_back</v-icon>Back
                </v-btn>
            </div>
        </v-layout>

    </v-app>

</div>

</template>

<script>

import json from '../../server/checklistData.json'
export default {
    name: 'procedures',
    data() {
        return {
            myJson: json,
            check: false,
            isLoaded: false,
        }
    },

    methods: {
        back: function() {
            console.log("back")
            this.$router.push('/patient/' + this.$route.params.id)
        },
        add_procedure: function(count) {
            //var str = this.myJson[count-1].Task_Description;
            //console.log(str)
            if (this.isLoaded == true) {
              var ajax_request = "http://localhost:5000/add_procedure?doctor_id=" + this.$cookies.get("userName") + "&count=" + count
              console.log(ajax_request)
              this.axios.post(ajax_request)
                  .then(function(response) {
                      console.log(response);
                  }).catch(error => {
                      console.log(error.response)
                  });
            }
        }


    },

    mounted: function() {
        if (annyang) {
            var NumberEnum = {
                "first": "1",
                "second": "2",
                "third": "3",
                "forth": "4",
                "fifth": "5",
                "sixth": "6",
                "seventh": "7",
                "eighth": "8",
                "ninth": "9",
                "tenth": "10",
                "eleven": "11",
                "twelve": "12",
                "thirteen": "13",
                "fourteen": "14",
                "fifteen": "15",
                "sixteen": "16",
            }

            Object.freeze(NumberEnum)
            // Let's define our first command. First the text we expect, and then the function it should call


            var commands = {
                'complete one': function() {
                    console.log(document.getElementById("1").click())
                }, 'complete two': function() {
                    console.log(document.getElementById("2").click())
                }, 'complete three': function() {
                    console.log(document.getElementById("3").click())
                }, 'complete four': function() {
                    console.log(document.getElementById("4").click())
                }, 'complete five': function() {
                    console.log(document.getElementById("5").click())
                }, 'complete six': function() {
                    console.log(document.getElementById("6").click())
                }, 'complete seven': function() {
                    console.log(document.getElementById("7").click())
                }, 'complete eighth': function() {
                    console.log(document.getElementById("8").click())
                }, 'complete nine': function() {
                    console.log(document.getElementById("9").click())
                }, 'complete ten': function() {
                    console.log(document.getElementById("10").click())
                }, 'complete eleven': function() {
                    console.log(document.getElementById("11").click())
                }
            };

            // Add our commands to annyang
            annyang.addCommands(commands);

            // Start listening. You can call this here, or attach this call to an event, button, etc.
            annyang.start();
        }


        this.axios
            .get("http://localhost:5000/view_procedures")
            .then((response) => {
                console.log(response.data.counter)

                for (var i = 1; i < response.data.counter+1; i++){

                  document.getElementById(i.toString()).click()
                }

            })
        this.isLoaded = true

    },

    beforeUpdate: function() {
        this.isLoaded = false
    }

}

</script>
