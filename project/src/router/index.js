import Vue from 'vue'
import Router from 'vue-router'
import FirstView from '@/components/FirstView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'FirstView',
      component: FirstView
    }
  ]
})
