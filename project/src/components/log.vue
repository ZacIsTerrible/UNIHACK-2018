<style scoped>



</style>

<template>

<div id="app">
    <v-app id="inspire">
        <v-flex xs20 sm6 offset-sm3>
          <h1> Doctor's comment</h1>
          <br/>
            <v-card>

                <v-form>

                    <v-divider></v-divider>
                    <v-text-field label="Subject" value="" single-line full-width hide-details></v-text-field>
                    <v-divider></v-divider>
                    <v-textarea label="Message" counter maxlength="1000" full-width single-line></v-textarea>
                </v-form>
            </v-card>
            <div>
                <v-btn color="orange darken-2" dark>
                    <v-icon dark left>arrow_back</v-icon>Back
                </v-btn>
                <v-btn color="green" @click="submit">submit</v-btn>
            </div>
        </v-flex>

    </v-app>
</div>
</div>

</template>

<script>

export default {
    name: 'log'
}

</script>
