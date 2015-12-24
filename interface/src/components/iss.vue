<style>
.iss {
  flex: 1;
  height: 300px;
  background-color: black;
  color: white;
  justify-content: center;
  display: flex;
  flex-direction: column;
}
</style>

<template>
<div
  class='iss'
>
  <p v-if='remaining > 0'>Next passage is {{ new Date(nextDate * 1000).toLocaleString() }}</p>
  <p v-else>Latest passage was {{ new Date(nextDate * 1000).toLocaleString() }}</p>
  <p v-if='remaining > 0'>Will last {{ duration }} seconds</p>
  <p v-else>Lasted {{ duration }}s</p>
  <p v-if='remaining > 0'>Arriving in {{ remaining }}s</p>
  <p v-else>Was {{ remaining }} seconds ago</p>
</div>
</template>

<script>
export default {
  props: [
    'nextDate',
    'duration'
  ],
  ready: function () {
    let _this = this
    setInterval(function () {
      const nextDate = _this.nextDate * 1000
      const now = new Date().valueOf()
      const timeLeft = Math.floor((nextDate - now) / 1000)
      _this.$set(
        'remaining',
        timeLeft
      )
    }, 1000)
  }
}
</script>
