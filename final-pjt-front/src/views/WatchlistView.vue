<template>
  <div class="watchlist">
    <h1>This is watchlists page</h1>
    <h2>고사리가 맛있다</h2>
    <!-- <button @click="addWatchList">추가하기</button> -->
    <form @submit.prevent="addWatchList">
      <select v-model="disclosure">
        <option :value="1">공개</option>
        <option :value="2">비공개</option>
      </select>
      <input type="text" id="newWatchlist" v-model="newWatchlistTitle"><br>
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
      newWatchlistTitle:"",
      disclosure:"",
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
      if (!this.newWatchlistTitle) alert('내용을 입력해주세요.')
      else if (!this.disclosure) alert('공개 여부를 설정해 주세요.')
      axios({
        method : 'post',
        url: `${API_URL}/api/watchlists/`,
        data: {
          title: this.newWatchlistTitle,
          scope_of_disclosure: this.disclosure
          },
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
