<template>
  <div class="watchlist-container">
    <div class="watchlist" v-if="owner">
      <img src="@/assets/img/add_watchlist.png" data-bs-toggle="modal" data-bs-target="#add-watch-list"/>
      <p> 새로운 재생목록 추가</p>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="add-watch-list" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5 text-secondary" id="exampleModalLabel">재생목록 생성</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="addWatchList">
              <div class="form-floating mb-3">
                <input type="text" class="form-control" id="username" placeholder="재생목록 제목" v-model="newWatchlistTitle">
                <label class="text-secondary" for="username" >재생목록 제목</label>
              </div>
              <div class="form-check text-secondary">
                <input class="form-check-input" type="checkbox" id="flexCheckDefault" v-model="disclosure">
                <p style="text-align:left">체크시 비공개로 설정합니다.</p>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary" @click="addWatchList" data-bs-dismiss="modal">생성</button>
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

    
    <WatchlistItems
    v-for="watchlist in watchlists"
    :key="watchlist.id"
    :watchlist="watchlist"
    />
  </div>
</template>

<script>
import WatchlistItems from "@/components/WatchlistItems.vue"
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'WatchLists',
  data() {
    return {
      newWatchlistTitle:"",
      disclosure:false,
    }
  },
  props: {
    watchlists: Array,
    owner:Boolean,
  },
  components: {
    WatchlistItems
  },
  methods: {
    addWatchList() {
      if (!this.newWatchlistTitle) alert('내용을 입력해주세요.')
      
      axios({
        method : 'post',
        url: `${API_URL}/api/watchlists/`,
        data: {
          title: this.newWatchlistTitle,
          scope_of_disclosure: this.disclosure? 1:2
          },
          headers: {
            Authorization : `Token ${this.$store.state.token}`
          }
        }) 
          .then(() => {
            this.$emit('added-watchlist')
          })
          .catch(err => console.log(err))
      // this.newWatchlist = ""
    }
  }
}
</script>

<style scoped>
img {
  width: 190px;
  height: 190px;
}
.modal {
  position: absolute;
  top: 0;
  left: 0;

  width: 100%;
  height: 100%;

  display: none;

  background-color: rgba(0, 0, 0, 0.4);
}
/* 
body {
  margin : 0;
} */
/* div {
  box-sizing: border-box;
} */
.black-bg {
  width: 100%; height:100%;
  background: rgba(0,0,0,0.5);
  position: fixed; padding: 20px;
}
.white-bg {
  width: 100%; background: white;
  border-radius: 8px;
  padding: 20px;
} 

.watchlist-container {
  width: 100%;
  display:flex;
}

.watchlist {
  margin-right: 1em;
}
</style>