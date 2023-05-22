<template>
  <div class="hello">
    <button @click="toDetail">{{ article.title }}</button>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article:Object
  },
  methods : {
    toDetail() {
      this.$router.push({name:'articleDetail', params: {articleID : this.article.id}})
    }
  }
}
</script>
