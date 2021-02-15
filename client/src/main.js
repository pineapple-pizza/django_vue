import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'

require('@/store/subscriber')

Vue.config.productionTip = false

// store.dispatch('auth/attempt', localStorage.getItem('token')).then(() => {
  new Vue({
    vuetify,
    router,
    store,
    render: h => h(App)
  }).$mount('#app')
// })

