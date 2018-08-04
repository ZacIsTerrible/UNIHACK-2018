<style scoped>



</style>

<template>

<div id="app">
    <v-app id="inspire">
        <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
                <v-card>

                    <v-list v-for="data in myJson" three-line>

                        <v-list-tile @click="">
                            <v-list-tile-action>
                                <v-checkbox></v-checkbox>
                            </v-list-tile-action>

                            <v-list-tile-content @click="check = !check">
                                <v-list-tile-title>{{ data.Task_Description }}</v-list-tile-title>
                                <v-list-tile-sub-title>{{data.Timer}}</v-list-tile-sub-title>

                            </v-list-tile-content>
                        </v-list-tile>

                    </v-list>

                </v-card>

            </v-flex>
            <div>
                <v-btn color="orange darken-2" dark>
                    <v-icon dark left>arrow_back</v-icon>Back
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
            check: false
        }
    }
}

</script>
