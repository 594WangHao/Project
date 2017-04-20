import Vue from 'vue'
import VueMaterial from 'vue-material'
import VueCharts from 'vue-charts'
import 'vue-material/dist/vue-material.css'
import 'material-design-icons/iconfont/material-icons.css'

import router from './router/'
import store from './store/'

import App from './App.vue'

Vue.use(VueMaterial)
Vue.use(VueCharts)

Vue.material.registerTheme('default', {
  primary: 'blue',
  accent: 'red',
  warn: 'yellow',
  background: 'white',
  color: 'white',
})

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
