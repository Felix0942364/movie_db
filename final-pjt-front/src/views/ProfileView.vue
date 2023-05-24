<template>
  <div class="profile_container">

    <div class="profile">
      <h1>This is profile page</h1>
      <img :src="imgSrc" v-if="imgSrc"/>
      <img src="@/assets/img/base_profile.png" v-else/>
      <h1> {{ user.username }} </h1>
      <p v-if="user.profile_message"> {{user.profile_message}} </p>

      <div v-if="user.preferences.length != 0">
        <h1> 취향 </h1>
        <UserPreference
        v-for="preference in user.preferences"
        :key="preference.id"
        :preference="preference"
        />
      </div>
      <!-- <div class="btn-group">
        <button>Followers : {{ user.followers_count }}</button>
        <button>Following : {{ user.following_count }}</button>
      </div> -->
      <div class="btn-group" role="group" aria-label="Basic example">
        <button type="button" class="btn btn-secondary">Followers : {{ user.followers_count }}</button>
        <button type="button" class="btn btn-secondary">Following : {{ user.following_count }}</button>
      </div>
      <div class="follow" v-if="user.id === this.$store.state.id"></div>
      <div v-else><button>팔로우</button></div>

    </div>

    <div class="board">
      <div class="watchlist">
        <h1>{{ user.username }} 님의 재생목록</h1>
        <WatchLists
        v-for="(watchlist, index) in user.watchlists"
        :key="index"
        :watchlist="watchlist"
        />
      </div>
      <br>
      <div>
        <ul class="nav nav-tabs">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">작성한 글들</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">좋아한 글들</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">작성한 댓글</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled">좋아한 댓글</a>
          </li>
        </ul>
      </div>
      <h3>작성한 글들</h3>
    
      <h3>좋아한 글들</h3>
      
      <h3>작성한 댓글</h3>
      
      <h3>좋아한 댓글</h3>
      
      <h1> {{user}} </h1>
    </div>
  </div>
</template>

<script>
import UserPreference from '@/components/UserPreference.vue'
import WatchLists from '@/components/WatchLists.vue'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    UserPreference,
    WatchLists,
  },
  data() {
    return {
      user:null
    }
  },
  created() {
    this.getProfile()
  },
  methods : {
    getProfile() {
      axios({
        method:'get',
        url: `${API_URL}/accounts/profile/${this.$store.state.id}/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.user = res.data 
        })
        .catch(err => console.log(err))
    },
  },
  computed: {
    myProfile() {
      return this.getProfile()
    }
  },
}
</script>

<style>
/* CSS for the layout */
.profile_container {
  display: flex;
  justify-content: center;
  background-image: url('@/assets/img/temp_bg_img.jpg');
  object-fit: center;
  object-position: center;
  
}

.profile {
  width: 25%;
  min-width: 400px;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
}

.board {
  width: 70%;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
  /* overflow: scroll; */
}

/* Additional styling for demonstration purposes */
.profile {
  background: lightgray;
  padding: 20px;
}

.board {
  background: rgba(255, 255, 255, 0.61);
  padding: 20px;
}

.profile > img {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  object-fit: cover;
  object-position: center;
  background-color: white;
}

.watchlist {
  padding: 20px;
  display: flex;
  background: gray;
  border-radius: 20px;
}
</style>