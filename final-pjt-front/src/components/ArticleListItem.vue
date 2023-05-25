<template>
  <tr @click="toDetail">
    <th scope="row">{{article.id}}</th>
    <td> {{ article.title }} </td>
    <td> {{ article.title }} </td>
    <td> {{ article.title }} </td> 
    <td> {{ article.title }} </td>
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
  background-color: rgba(255, 255, 255, 0.164);
}

</style>