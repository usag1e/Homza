<style>
.metro {
  flex: 1;
  height: 300px;
  justify-content: center;
  display: flex;
  flex-direction: column;
}

.line {
  height: 75px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: white;
}

.status {
  font-weight: bold;
}

.green {
  background-color: #008800;
}
.orange {
  background-color: #EE8800;
}
.yellow {
  background-color: #FFC40D;
}
.blue {
  background-color: #052ECF;
}
</style>

<template>
<div
  class='metro'
>
  <div class='line green'>
    <p>Traffic: <span class='status'>{{ green ? 'DISRUPTED' : 'OK' }}</span></p>
  </div>
  <div class='line orange'>
    <p>Traffic: <span class='status'>{{ orange ? 'DISRUPTED' : 'OK' }}</span></p>
  </div>
  <div class='line yellow'>
    <p>Traffic: <span class='status'>{{ yellow ? 'DISRUPTED' : 'OK' }}</span></p>
  </div>
  <div class='line blue'>
    <p>Traffic: <span class='status'>{{ blue ? 'DISRUPTED' : 'OK' }}</span></p>
  </div>
</div>
</template>

<script>
import {getMetro} from '../utils'

export default {
  ready: function () {
    getMetro(this)
    var _this = this
    setInterval(function () {
      getMetro(_this)
    }, 10 * 60 * 1000)
  }
}
</script>
