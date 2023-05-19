<template>
  <div class="watchlist">
    <h1>This is watchlists page</h1>
    <h2>고사리가 맛있다</h2>
    <button @click="addWatchList">추가하기</button>
    <Watchlists
    v-for="(watchlist, index) in myWatchList"
    :key="index"
    :watchlist="watchlist"
    />
  </div>
</template>

<script>
import Watchlists from "@/components/Watchlists.vue"

export default {
  name: 'WatchlistsView',
  components: {
    Watchlists
  },
  created () {
    this.getWatchList()
  },
  methods: {
    getWatchList() {
      this.$store.dispatch('getWatchList')
    },
    addWatchList(val) {
      console.log(val)
      console.log('abc')
      console.log('도레미')
    }
  },
  computed: {
    myWatchList() {
      return this.$store.state.watchlists
    },
  }
}
</script>
