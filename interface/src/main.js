import Vue from 'vue'
import Resource from 'vue-resource'
import User from './components/user.vue'

Vue.use(Resource)

let mv = new Vue({
  el: '#content',
  components: { User },
  ready: function ready () {
    this.$http.get('http://127.0.0.1:5984/homza/house').then(
      function (response) {
        if (response.status === 200) {
          this.$set('home', response.data)
        }
      }
    )
    this.$http.get('http://127.0.0.1:5984/homza/_design/users/_view/by_name').then(
      function (response) {
        if (response.status === 200) {
          this.$set('users', response.data.rows)
        }
      }
    )
  }
})
