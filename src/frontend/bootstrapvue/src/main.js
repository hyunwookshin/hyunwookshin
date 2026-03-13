import Vue from 'vue'
import App from './App.vue'

import {
  BButton,
  BImg,
  BImgLazy,
  BTabs,
  BTab,
  BCard,
  BCardText,
  BCardFooter,
  BLink,
} from 'bootstrap-vue'

Vue.component('b-btn', BButton)
Vue.component('b-img', BImg)
Vue.component('b-img-lazy', BImgLazy)
Vue.component('b-tabs', BTabs)
Vue.component('b-tab', BTab)
Vue.component('b-card', BCard)
Vue.component('b-card-text', BCardText)
Vue.component('b-card-footer', BCardFooter)
Vue.component('b-link', BLink)

Vue.config.productionTip = false

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

new Vue({
  render: h => h(App),
}).$mount('#app')
