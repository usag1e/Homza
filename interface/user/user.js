var User = Vue.extend({
  data: function(){
    return {
      name: 'Adrien',
      image: 'images/adrien.jpg',
      isHere: true
    }
  },
  template: 'templates/user.html' 
})

var adrien = new User()
