<template>
  <div class="articlelist">
    <h1>This is articlelist page</h1>
    <SingleArticle
    v-for="article in articles"
    :key="article.pk"
    :article="article"/>
  </div>
</template>

<script>
import SingleArticle from '@/components/SingleArticle.vue'

export default {
  name: 'ArticleListView',
  components: {
    SingleArticle
  },
  created() {
    this.$store.dispatch('getArticles')
  },
  computed : {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>
