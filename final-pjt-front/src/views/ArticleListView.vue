<template>
  <div class="articlelist">
    <h1>This is articlelist page</h1>
    <router-link :to="{name:'createArticle'}">[새로운 글]</router-link> 
    <router-view/>
    <ArticleListItem
    v-for="article in this.articles"
    :key="article.pk"
    :article="article"/>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'
import axios from 'axios'
 
export default {
  name: 'ArticleListView',
  data() {
    return {
      articles:null
    }
  },
  components: {
    ArticleListItem
  },
  created() {
    this.getArticles()
  },
  beforeRouteUpdate(to, from, next) {
    this.getArticles()
    next()
  },
  methods : {
    getArticles() {
      axios({
        method: 'get',
        url: `${process.env.VUE_APP_BE_API_BASE_URL}/api/articles/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        // .then(res => {this.articles = res.data})
        .then(res => {this.articles = res.data})
        .catch(err => console.log(err))
    },
  },
  computed : {
  }
}
</script>
