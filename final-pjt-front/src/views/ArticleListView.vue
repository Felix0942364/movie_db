<template>
  <div class="articlelist">
    <h1>This is articlelist page</h1>
    <ArticleListItem
    v-for="article in articles"
    :key="article.pk"
    :article="article"/>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'

export default {
  name: 'ArticleListView',
  components: {
    ArticleListItem
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
