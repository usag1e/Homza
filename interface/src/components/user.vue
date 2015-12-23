<style>
  .user {
    flex: 1;
    width: 200px;
    height: 200px;
  }
</style>

<template>
  <div
    class='user'
    :class='{ here: isHere }'
    title='{{ name }}'
    style='background-image: url({{ image }});'
  >
  </div>
</template>

<script>
  exports.default = {
    props: [
      'name',
      'image',
      'isHere'
    ]
  }
</script>
