<template>
  <div class="px-2">
    <div
    class="d-flex align-items-center text-secondary"
    v-for='follow in follows'
    :key='follow.id'
    @click='toProfile(follow.id)'
    >
      <img class="small-profile" :src="'http://localhost:8000' + follow.profile_img" v-if="follow.profile_img"/>
      <img class="small-profile" src="@/assets/img/base_profile.png" v-else/>
      <h4>{{follow.username}}</h4>
    </div>
  </div>
</template>

<script>
export default {
  name:"FollowItem",
  props: {
    follows:Array,
  },
  methods: {
    toProfile(id) {
      id
      // this.$router.push({name:'profile', params: { 'userID' : id}})
      this.$router.go(this.$router.currentRoute)
    },
  }
}
</script>

<style scoped>
.small-profile {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-left: 0.5em;
  margin-right: 0.5em;
  object-fit: cover;
  object-position: center;
  background-color: white;
  box-shadow: 0 5px 20px #eeeeee8c;
}
</style>