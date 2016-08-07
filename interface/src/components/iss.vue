<style>
.iss {
  flex: 1;
  height: 300px;
  background-color: #222244;
  color: white;
  justify-content: center;
  display: flex;
  flex-direction: column;
}

#sky {
  width: 100%;
  height: 100%;
}

.star {
  fill: white;
}

#iss-trajectory {
  width: -50%;
}

.iss-trajectory {
  fill: none;
  stroke: white;
  stroke-width: 0.25;
}

.hide-iss {
  display: none;
}
</style>

<template>
<div
  class='iss'
>
  <svg
    id='sky'
  >
    <g id='stars-background'>
      <circle class='star' cx='2%' cy='50' r='2' />
      <circle class='star' cx='10%' cy='150' r='1' />
      <circle class='star' cx='15%' cy='30' r='1' />
      <circle class='star' cx='20%' cy='80' r='1.5' />
      <circle class='star' cx='31%' cy='95' r='1.45' />
      <circle class='star' cx='30%' cy='75' r='1.15' />
      <circle class='star' cx='50%' cy='60' r='1.25' />
      <circle class='star' cx='65%' cy='90' r='1.75' />
      <circle class='star' cx='72%' cy='110' r='1.05' />
      <circle class='star' cx='85%' cy='50' r='0.55' />
      <circle class='star' cx='92%' cy='80' r='1.55' />
    </g>
    <g
      id='iss-trajectory'
    >
      <path d="M 0 {{ heightStart }} L {{ widthMax }} 0" class="iss-trajectory" />
      <circle class='star' :class='{ "hide-iss": !isHappening }' cx='{{ issx }}' cy='{{ issy }}' r='5' />
    </g>
  </svg>
  <div v-if='isHappening'>
    <p>Current passage started {{ new Date(nextDate * 1000).toLocaleString() }}</p>
    <p>Still up for {{ duration + remainingBeforeStart }} seconds</p>
    <p>It's visible right now!</p>
  </div>
  <div v-if='!isHappening && remainingBeforeStart > 0'>
    <p>Next passage is {{ new Date(nextDate * 1000).toLocaleString() }}</p>
    <p>Will last {{ duration }} seconds</p>
    <p>Arriving in {{ remainingBeforeStart }} seconds</p>
  </div>
  <div v-if='!isHappening && remainingBeforeStart < 0'>
    <p>Latest passage was {{ new Date(nextDate * 1000).toLocaleString() }}</p>
    <p>Lasted {{ duration }}s</p>
    <p>Was visible {{ Math.abs(remainingBeforeStart + duration) }} seconds ago</p>
  </div>
</div>
</template>

<script>
import {getISS} from '../utils'

export default {
  props: [
    'nextDate',
    'duration'
  ],
  data: function () {
    getISS(this)

    return {
      isHappening: false,
      remainingBeforeStart: 0,
      issx: '0%',
      issy: 0,
      heightStart: 130,
      heightMax: 0,
      widthStart: 0,
      widthMax: 3000
    }
  },
  ready: function () {
    let _this = this
    setInterval(function () {
      const nextDate = _this.nextDate * 1000
      const now = new Date().valueOf()
      const timeLeftBeforeStart = Math.floor((nextDate - now) / 1000)
      _this.$set(
        'remainingBeforeStart',
        timeLeftBeforeStart
      )
      const isHappening = timeLeftBeforeStart < 0 &&
        timeLeftBeforeStart + _this.duration > 0
      _this.$set(
        'isHappening',
        isHappening
      )
      if (isHappening) {
        const widthEnd = document.getElementById('sky').width.animVal.value
        const heightEnd = _this.heightStart / _this.widthMax * widthEnd
        const percentOfVisibilityTime = 100 - ((timeLeftBeforeStart +
          _this.duration) * 100 / _this.duration)
        const x = percentOfVisibilityTime + '%'
        const y = _this.heightStart - percentOfVisibilityTime / 100 * heightEnd
        _this.$set('issx', x)
        _this.$set('issy', y)
      } else if (timeLeftBeforeStart < -_this.duration) {
        getISS(_this)
      }
    }, 1000)
  }
}
</script>
