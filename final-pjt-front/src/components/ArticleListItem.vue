<template>
  <tr @click="toDetail">
    <th scope="row">{{article.id}}</th>
    <td> {{ article.title }} </td>
    <td> {{ article.author_name }} </td>
    <td> {{ article.like_count }} </td> 
    <td>
      <span>{{ article?.created_at.slice(0,4) }}년 </span>
      <span>{{ article?.created_at.slice(5,7) }}월 </span>
      <span>{{ article?.created_at.slice(8,10) }}일 </span>
    </td>
    <!-- <button @click="toDetail">{{ article.title }}</button> -->
  </tr>
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

<style scoped>
tr {
  cursor: pointer;
}

tr:hover {
  
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(255, 255, 255, 0.164));
}

th, td {
  border-bottom: 1px solid #444444;
  padding: 10px;
}
</style>