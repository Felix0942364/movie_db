<template>
  <div class="profile">
    <h1>This is profile page</h1>
    <img :src="imgSrc" v-if="imgSrc"/>
    <img src="@/assets/img/base_profile.png" v-else/>
    <h1 v-if="user.nickname"> {{ user.nickname }} </h1>
    <h1> {{ user.username }} </h1>
    <p> 상태 메세지 : {{user.profile_message}} </p>
    <h1> {{user}} </h1>
    <h1 v-if="user.email"> EMAIL </h1>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
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
