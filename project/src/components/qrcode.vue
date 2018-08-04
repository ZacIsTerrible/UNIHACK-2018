<style scoped>



</style>

<template>

<div id="qrcode">
    <v-app id="inspire">
        <v-layout row>
            <v-flex xs12 sm6 offset-sm3>

                <v-card>
                    <v-card-title class="headline grey lighten-2" primary-title>
                        Qr Reader
                    </v-card-title>

                    <v-card-text>
                        <QrcodeReader @decode="onDecode">
                        </QrcodeReader>
                        Scan patient's QR code.
                    </v-card-text>

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

import {
    QrcodeReader
}
from 'vue-qrcode-reader'
export default {
    components: {
        QrcodeReader
    },
    name: 'qrcode',
    data() {
        return {


        }
    },
    methods: {
        onDecode(decodedString) {
            this.$router.push('/')
            console.log(decodedString)
        }
    }
}

</script>
