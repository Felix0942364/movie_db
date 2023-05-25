<template>
  <div class="watchlist">
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
  width: 190px;
  height: 190px;
  box-shadow: 0 5px 10px #4b4a4a59;
}
.watchlist {
  margin-right: 1em;
}
</style>