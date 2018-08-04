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

</style>

<template>

<v-app>

    <div v-if="isLoggedIn" id="pwa-view">
        <v-toolbar app:clipped-left="clipped" color="primary" id="toolbar-style">
            <v-toolbar-title v-text="title"></v-toolbar-title>
            <v-spacer></v-spacer>
            <a href="/#">
                <v-btn flat color="accent" v-on:click="logout">Log Out</v-btn>
            </a>
        </v-toolbar>
        <v-content>
            <router-view/>
        </v-content>
    </div>

    <div v-else id="login-view">
        <v-layout align-center justify-center row fill-height>
            <div id="login-box">
                <h1>Login</h1>

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
            }
        },

        methods: {
            login: function() {
                this.userName = document.getElementById('uname').value;
                this.$cookies.set('userName', this.userName);
                this.isLoggedIn = true;
            },
            logout: function() {
                this.$cookies.remove("userName");
                this.isLoggedIn = false;
            }

        },

        mounted: function() {
            this.$nextTick(function() {
                if (this.$cookies.isKey('userName')) {
                    this.userName = this.$cookies.get('userName')
                    this.isLoggedIn = true
                }
            })
        },

        name: 'App'
}

</script>
