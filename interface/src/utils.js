export function getHouse (thisObject) {
  // Fetching House
  thisObject.$http.get('http://' + API_URL + ':5984/homza/house')
  .then(
    function (response) {
      if (response.status === 200) {
        thisObject.$set('home', response.data)
      }
    }
  )
}

export function getUsers (thisObject) {
  // Fetching Users
  thisObject.$http.get('http://' + API_URL + ':5984/homza/_design/users/_view/by_name')
  .then(
    function (response) {
      if (response.status === 200) {
        thisObject.$set('users', response.data.rows)
      }
    }
  )
}

export function getUser (thisObject, name) {
  // Fetching User
  console.log
  thisObject.$http.get('http://' + API_URL + ':5984/homza/' + thisObject.name)
  .then(
    function (response) {
      if (response.status === 200) {
        thisObject.$set('isHere', response.data.isHere)
        thisObject.$set('image', response.data.image)
      }
    }
  )
}

export function getISS (thisObject) {
  // Fetching Iss data
  thisObject.$http.get('http://' + API_URL + ':5984/homza/iss')
  .then(
    function (response) {
      if (response.status === 200) {
        thisObject.$set('nextDate', response.data.date)
        thisObject.$set('duration', response.data.duration)
      }
    }
  )
}

export function getMetro (thisObject) {
  // Fetching Weather data
  thisObject.$http.get('http://' + API_URL + ':5984/homza/subway')
  .then(
    function (response) {
      if (response.status === 200) {
        thisObject.$set('green', response.data.metro1)
        thisObject.$set('orange', response.data.metro2)
        thisObject.$set('yellow', response.data.metro4)
        thisObject.$set('blue', response.data.metro5)
      }
    }
  )
}

export function getWeather (thisObject) {
  // Fetching Weather data
  thisObject.$http.get('http://' + API_URL + ':5984/homza/weather')
  .then(
    function (response) {
      if (response.status === 200) {
        thisObject.$set('weather', response.data)
      }
    }
  )
}
