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

input[type=text], select {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
		background-color: #f2f2f2;
		color: black;
}

input[type=password], select {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
		background-color: #f2f2f2;
		color: black;
}

input[type=submit] {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

input[type=submit]:hover {
    background-color: #45a049;
}

#inputs {
    /* border-radius: 5px;
    background-color: #f2f2f2; */
    padding: 20px;
}

</style>

<template>
  <v-app>

	<div v-if="isLoggedIn" id="pwa-view">
		<v-toolbar app:clipped-left="clipped" color="primary" id="toolbar-style">
		  <v-toolbar-title v-text="title"></v-toolbar-title>
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
					  <form action="xyz">
					    <input type="text" id="uname" name="username" placeholder="Username">

					    <input type="password" id="pword" name="password" placeholder="Password">

					    <input type="submit" value="Submit">
					  </form>
					</div>

				</div>
			</v-layout>
	</div>

  </v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      title: 'CheckWrist',
      isLoggedIn: true
    }
  },
  name: 'App'
}
</script>
