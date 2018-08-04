import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import patientsList from '@/components/patientsList'
import dashboard from '@/components/dashboard'
import procedures from '@/components/procedures'
import conditions from '@/components/conditions'
import log from '@/components/log'
import summary from '@/components/summary'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/patients',
      name: 'patient',
      component: patientsList
    },
    {
      path: '/patient/:id',
      name: 'id',
      component: dashboard
    },
    {
      path: '/procedure',
      name: 'procedure',
      component: procedures
    },
    {
      path: '/patient/:id/conditions',
      name: 'conditions',
      component: conditions
    },
    {
      path: '/patient/:id/log',
      name: 'log',
      component: log
    },
    {
      path: '/patient/:id/summary',
      name: 'summary',
      component: summary
    }
  ]
})
