<template>
  <div class="community">
    <h1>This is community page</h1>
    <router-link to="/watchlist/articlelist">ArtilcleList</router-link>      
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'CommunityView',
  components: {
  }
}
</script>
