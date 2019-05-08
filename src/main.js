import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import VeeValidate from 'vee-validate'

Vue.config.productionTip = false

Vue.prototype.$base_url = "http://fletcher.cse.taylor.edu:5000"

Vue.use(VueRouter);
Vue.use(VeeValidate);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
