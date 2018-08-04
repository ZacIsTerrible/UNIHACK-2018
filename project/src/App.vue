<style scoped>
#toolbar-style {
	color: white
}

</style>

<template>
  <v-app>
    <v-toolbar app:clipped-left="clipped" color="primary" id="toolbar-style">
      <v-toolbar-title v-text="title"></v-toolbar-title>
    </v-toolbar>
    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      title: 'CheckWrist'
    }
  },
  name: 'App'
}
</script>
