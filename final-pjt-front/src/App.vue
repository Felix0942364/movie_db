<template>
  <div id="app">
    <nav>
      <div class="nav-logo">
        <router-link to="/"><img alt="Vue logo" src="@/assets/img/logo.png"  class="logo-image"></router-link> 
        <router-link to="/" id="homelink">Home</router-link> 
      </div>   
      <div class="nav-list">
        <router-link to="/search">Search</router-link> 
        <router-link to="/community">Community</router-link> 
        <router-link to="/watchlists">My Watchlists</router-link> 
      </div>
      <div class="nav-profile">
        <div v-if="this.$store.getters.isAuthenticated">
          <router-link to="/profile">Profile</router-link> 
          <p @click="logOut">Log Out</p> 
        </div>
        <div v-else>
          <router-link to="/login">Log In</router-link>
          <router-link to="/signup">Sign Up</router-link>
        </div>
      </div>
    </nav>
    <br>
    <router-view/>
  </div>
</template>

<script>
export default ({
  name:'app',
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    }
  }
})
</script>



<style src="@/assets/style_sheet.css">
</style>

