<style>
  .user {
    flex: 1;
    height: 300px;
    background-size: cover;
    background-position: center center;
    opacity: 0.5;
    border: solid 2px;
    border-color: grey;
  }

  .user.here {
    opacity: 1;
    border-color: green;
  }

  .user.away {
    opacity: 0.1;
    border-color: red;
  }
</style>

<template>
  <div
    class='user'
    :class='{ here: isHere == 1, away: isHere == -1 }'
    title='{{ name }}'
    style='background-image: url({{ image }});'
  >
  </div>
</template>

<script>
  export default {
    props: [
      'name',
      'image',
      'isHere'
    ]
  }
</script>
