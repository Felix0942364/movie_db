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
        <router-link to="/watchlists">Watchlist</router-link> 
      </div>
      <div class="nav-profile">
        <router-link to="/profile">Profile</router-link> 
      </div>
    </nav>
    <br>
    <router-view/>
  </div>
</template>

<style src="@/assets/style_sheet.css">
</style>

