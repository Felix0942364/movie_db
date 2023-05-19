<template>
  <div class="watchlists">
    <img :src="watchlist.posterpath"/>
    <h2>상세보기</h2>
    <WatchlistItems
    v-for="movie, index in watchlist"
    :key="index"
    :movie="movie"/>
  </div>
</template>

<script>
import WatchlistItems from "@/components/Watchlists.vue"

export default {
  name: 'WatchlistsView',
  props: {
    watchlist: Object
  },
  components: {
    WatchlistItems
  },
}
</script>
