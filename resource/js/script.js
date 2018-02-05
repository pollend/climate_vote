import Vue from 'vue'

import 'jquery'
import 'popper.js'
import 'bootstrap'
import 'bootstrap/js/dist/tooltip'

import App from './App.vue'
import bFormSlider from 'vue-bootstrap-slider'

Vue.use(bFormSlider)
window.onload = function () {
  new Vue({
    render: h => h(App)
  }).$mount('#app')
}
