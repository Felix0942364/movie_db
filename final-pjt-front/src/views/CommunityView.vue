<template>
  <div class="community">
    <router-link to="/watchlist/articlelist">ArtilcleList</router-link>|
    <router-link :to="{name:'createArticle'}">[CREATE]</router-link> 
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
