import Vue from 'vue'
import Resource from 'vue-resource'
import User from './components/user.vue'
import Iss from './components/iss.vue'
import Weather from './components/weather.vue'
import {getHouse, getUsers} from './utils'

Vue.use(Resource)

let mv = new Vue({
  el: '#content',
  components: { User, Iss, Weather },
  ready: function ready () {
    getHouse(this)
    getUsers(this)
  }
})
