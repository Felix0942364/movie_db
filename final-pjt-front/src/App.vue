<template>
  <div id="app">
    <nav>
      <div class="nav-logo">
        <router-link to="/"><img alt="nav logo" src="@/assets/img/logo_white.png"  class="logo-image"></router-link> 
        <router-link to="/" id="homelink">Home</router-link> 
      </div>   
      <div class="nav-list">
        <router-link to="/search">Search</router-link> 
        <router-link to="/community">Community</router-link> 
      </div>
      <div class="nav-profile">
        <div v-if="this.$store.getters.isAuthenticated">
          <router-link to="/profile">My Page</router-link> 
          <!-- <router-link to="/logout">LogOut</router-link>  -->
          <a @click="logOut">Log Out</a> 
        </div>
        <div v-else>
          <router-link to="/login">Log In</router-link>
          <router-link to="/signup">Sign Up</router-link>
        </div>
      </div>
    </nav>
    <router-view/>
    <footer>
    </footer>
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

