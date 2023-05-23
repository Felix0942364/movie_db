<template>
  <div class="watchlists">
    <img :src="watchlist.cover_image" v-if="watchlist.cover_image" />
    <img src="@/assets/img/base_profile2.png" />
    <h1>{{watchlist.title}}</h1>
    <h2>상세보기</h2>
    <p>{{watchlist}}</p>
    <WatchlistItems
    v-for="movie, index in watchlist.movies"
    :key="index"
    :movie="movie"/>
  </div>
</template>

<script>
import WatchlistItems from "@/components/WatchlistItems.vue"

export default {
  name: 'WatchLists',
  props: {
    watchlist: Object
  },
  components: {
    WatchlistItems
  },
}
</script>
