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
