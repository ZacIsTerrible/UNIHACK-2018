<style scoped>



</style>

<template>

<div id="app">
    <v-app id="inspire">
        <v-layout row>
            <v-flex xs12 sm6 offset-sm3>
                <v-card>

                    <v-list subheader two-line>
                        <v-subheader>Hangout notifications</v-subheader>

                        <v-list-tile @click="">
                            <v-list-tile-action>
                                <v-checkbox v-model="notifications"></v-checkbox>
                            </v-list-tile-action>

                            <v-list-tile-content @click="notifications = !notifications">
                                <v-list-tile-title>Notifications</v-list-tile-title>
                                <v-list-tile-sub-title>Allow notifications</v-list-tile-sub-title>
                                <v-btn v-on:click="read">send</v-btn>
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

export default {
    name: 'procedures',
    data() {
        return {
            notifications: false
        }
    },
    methods: {
        read: function() {
            this.axios
                .get("http://127.0.0.1:5000/dummy")
                .then((response) => {
                    console.log(response.data)
                })
        }
    }
}

</script>
