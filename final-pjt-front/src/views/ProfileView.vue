<template>
  <div class="profile">
    <h1>This is profile page</h1>
    <img :src="imgSrc" v-if="imgSrc"/>
    <img src="@/assets/img/base_profile.png" v-else/>
    <h1> {{ user.username }} </h1>
    <p> 상태 메세지 : {{user.profile_message}} </p>

    <div v-if="user.preferences.length != 0">
      <h1> 취향 </h1>
      <UserPreferences
      v-for="preference in user.preferences"
      :key="preference.id"
      :preference="preference"
      />
    </div>

    <div class="follow" v-if="user.id === this.$store.state.id">
      <button>팔로워</button>
      <button>팔로잉</button>
    </div>
    <div v-else>
      <button>팔로우</button>
    </div>

    <h1>{{ user.username }} 님의 재생목록</h1>
    {{ user.watchlists }}
    <WatchLists
    v-for="(watchlist, index) in user.watchlists"
    :key="index"
    :watchlist="watchlist"
    />
    <h3>
      작성한 글들
    </h3>
    <h3>
      좋아한 글들
    </h3>
    <h3>
      작성한 댓글
    </h3>
    <h3>
      좋아한 댓글
    </h3>

    <h1> {{user}} </h1>
    
  </div>
</template>

<script>
import UserPreference from '@/components/UserPreference.vue'
import WatchLists from '@/components/WatchLists.vue'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  component: {
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
