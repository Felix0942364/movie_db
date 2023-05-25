<template>
  <div class="container">
    <div class="thumbnail">
      <img :src="watchlist.cover_image" v-if="watchlist.cover_image" />
      <img src="@/assets/img/base_thumbnail.png" />
    </div>
    <p> {{ watchlist.title }}</p>
  </div>
</template>

<script>
export default {
  name: "WatchListItems",
  props: {
    watchlist : Object
  }
}
</script>

<style scoped>
img {
  width: 200px;
  height: 200px;
}
</style>