<template>
  <div class="watchlist">
    <h1>This is watchlists page</h1>
    <h2>고사리가 맛있다</h2>
    <!-- <button @click="addWatchList">추가하기</button> -->
    <form @submit.prevent="addWatchList">
      <input type="text" id="newWatchlist" v-model="newWatchlist"><br>
      <input type="submit" id="submit">
    </form>
    <WatchLists
    v-for="(watchlist, index) in myWatchList"
    :key="index"
    :watchlist="watchlist"
    />
  </div>
</template>

<script>
import axios from 'axios'
import WatchLists from "@/components/WatchLists.vue"
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'WatchlistsView',
  components: {
    WatchLists
  },
  data() {
    return {
      newWatchlist:"",
    }
  },
  created () {
    this.getMyWatchList()
  },
  methods: {
    getMyWatchList() {
      this.$store.dispatch('getMyWatchList')
    },
    addWatchList() {
      const title = this.newWatchlist 
      console.log(title, this.$store.state.token)
      axios({
        method : 'post',
        url: `${API_URL}/api/watchlists/`,
        data: { title },
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      }) 
        .then((res) => {
          console.log(res)
          this.getMyWatchList()
        })
        .catch(err => console.log(err))
      // this.newWatchlist = ""
    }
  },
  computed: {
    myWatchList() {
      return this.$store.state.watchlists
    },
  }
}
</script>
