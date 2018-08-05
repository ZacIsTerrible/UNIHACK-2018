<style scoped>

#toolbar-style {
    color: white
}

#login-view {
    background: radial-gradient(#20287B, #141736);
    width: 100%;
    height: 100%;
}

#login-card {
    width: 30%;
    height: 30%;
    margin: 30%;
}

#login-box {
    text-align: center;
    color: white;
    font-size: 30px;
}

input[type=text],
select {
    width: 400px;
    padding: 5px 10px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    background-color: #f2f2f2;
    color: black;
}

input[type=password],
select {
    width: 400px;
    padding: 5px 10px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    background-color: #f2f2f2;
    color: black;
}

input[type=submit] {
    width: 400px;
    background-color: #2168BC;
    color: white;
    padding: 5px 10px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

input[type=submit]:hover {
    background-color: #236EC7;
}

#inputs {
    /* border-radius: 5px;
    background-color: #f2f2f2; */
    padding-left: 25%;
    padding-right: 25%;
}

#spacing {
    margin: 70px;
}

</style>

<template>

<v-app>

    <div v-if="isLoggedIn" id="pwa-view">
        <v-toolbar app:clipped-left="clipped" color="primary" id="toolbar-style" fixed>
            <img src="../../CheckWrist Logo.png" style="height: 50px; background-color: rgba(255,255,255,0.9); padding: 2px; border-radius: 4px;">
            <v-toolbar-title v-text="title" style="font-family: 'Rubik', sans-serif; font-size: 40px;"></v-toolbar-title>
            <v-spacer></v-spacer>
            <h1 style="font-family: 'Rubik', sans-serif; font-size: 40px;">{{doctor_name}}</h1>
            <v-spacer></v-spacer>
            <a href="/#">
                <v-btn flat color="accent" v-on:click="logout">Log Out</v-btn>
            </a>
        </v-toolbar>
        <div id="spacing">
        </div>
        <v-content>
            <router-view/>
        </v-content>
    </div>

    <div v-else id="login-view">
        <v-layout align-center justify-center row fill-height>
            <div id="login-box">

                <img src="../../CheckWrist Logo.png" style="height: 250px;">
                <h1 style="font-family: 'Rubik', sans-serif;">CheckWrist</h1>

                <div id="inputs">
                    <form>
                        <input type="text" id="uname" name="username" placeholder="Username">

                        <input type="password" id="pword" name="password" placeholder="Password">

                        <input type="submit" value="Login" v-on:click="login">
                    </form>
                </div>

            </div>
        </v-layout>
    </div>

</v-app>

</template>

<script>

export default {
    data() {
            return {
                clipped: false,
                drawer: true,
                fixed: false,
                title: 'CheckWrist',
                isLoggedIn: false,
                userName: null,
                doctor_name: null,
            }
        },

        methods: {
            login: function() {
                this.userName = document.getElementById('uname').value;
                this.$cookies.set('userName', this.userName);

                if (this.userName.charAt(0) == 'D' && this.userName.charAt(1) == '*') {
                    this.$cookies.set('userType', "Doctor");
                } else if (this.userName.charAt(0) == 'N' && this.userName.charAt(1) == '*') {
                    this.$cookies.set('userType', "Nurse");
                }
                this.isLoggedIn = true;
            },
            logout: function() {
                this.$cookies.remove("userName");
                this.$cookies.remove("userType");
                this.isLoggedIn = false;
            }

        },

        mounted: function() {
            this.$nextTick(function() {
                if (this.$cookies.isKey('userName')) {
                    this.userName = this.$cookies.get('userName')
                    this.isLoggedIn = true
                }

                this.axios
                    .get("http://localhost:5000/get_doctor_name?doctor_id=" + this.$cookies.get("userName"))
                    .then((response) => {
                        this.doctor_name = response.data.doctor_name
                        console.log(response.data.doctor_name)
                    })
            })
        },

        name: 'App'
}

</script>
