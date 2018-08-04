<style scoped>



</style>

<template>

<div id="app">
    <v-app id="inspire">
        <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
                <v-card>

                    <v-list v-for="data in myJson" subheader two-line>


                        <v-list-tile@click="">
                            <v-list-tile-action>
                                <v-checkbox v-model="notifications"></v-checkbox>
                            </v-list-tile-action>

                            <v-list-tile-content @click="notifications = !notifications">
                                <v-list-tile-title>{{ data.Task_Description }}</v-list-tile-title>



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

<script>

import json from '../../server/checklistData.json'
export default {
    name: 'procedures',
    data() {
        return {
            myJson: json,
            notifications: false

        }
    }
}

</script>
