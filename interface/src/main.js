import Vue from 'vue'
import Resource from 'vue-resource'
import User from './components/user.vue'
import Iss from './components/iss.vue'

Vue.use(Resource)

let mv = new Vue({
  el: '#content',
  components: { User, Iss },
  ready: function ready () {
    // Fetching House
    this.$http.get('http://127.0.0.1:5984/homza/house')
    .then(
      function (response) {
        if (response.status === 200) {
          this.$set('home', response.data)
        }
      }
    )
    // Fetching Users
    this.$http.get('http://127.0.0.1:5984/homza/_design/users/_view/by_name')
    .then(
      function (response) {
        if (response.status === 200) {
          this.$set('users', response.data.rows)
        }
      }
    )
    // Fetching Iss first data
    this.$http.get('http://127.0.0.1:5984/homza/iss')
    .then(
      function (response) {
        if (response.status === 200) {
          this.$set('iss', response.data)
        }
      }
    )
  }
})
