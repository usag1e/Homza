<style>
.weather {
  flex: 1;
  height: 300px;
  justify-content: center;
  display: flex;
  flex-direction: column;
  background-color: rgba(0, 0, 0, 0.2);
}

.cold.weather {
  background-color: rgba(0, 0, 255, 0.2);
}
.warm.weather {
  background-color: rgba(255, 0, 0, 0.2);
}

.temp {
  font-weight: bold;
}

.cold.temp {
  color: #55f;
}
.warm.temp {
  color: #900;
}
</style>

<template>
<div
  class='weather'
  :class='{ cold: weather.temperature < 0, warm: weather.temperature > 20 }'
>
  <p>{{ weather.state }}</p>
  <p><img src='http://openweathermap.org/img/w/{{ weather.icon }}.png' /></p>
  <p>
    <span>Pressure is {{ weather.pressure }} hPa.</span>
    <span>Temperature is <span class='temp' :class='{ cold: weather.temperature < 0, warm: weather.temperature > 20 }'>{{ weather.temperature }} °C</span></span>
  </p>
  <p>Wind is {{ weather.wind }} km/h</p>
  <p>Sun: rises at {{ weather.sunrise }}, sets at {{ weather.sunset }}</p>
</div>
</template>

<script>
export default {
  props: [
    'weather'
  ],
  ready: function () {
    console.log(this.weather)
  }
}
</script>
