<template>
  <tr @click="toDetail">
    <th scope="row">{{ item.id }}</th>
    <td> {{ item.title }} </td>
    <td> {{ item.author_name }} </td>
    <td>
      <span>{{ item.created_at.slice(0,4) }}년 </span>
      <span>{{ item.created_at.slice(5,7) }}월 </span>
      <span>{{ item.created_at.slice(8,10) }}일 </span>
    </td>
  </tr>
</template>

<script>
export default {
  name:'TableItem',
  props: {
    item : Object
  },
  methods : {
    toDetail() {
      this.$router.push({name:'articleDetail', params: {articleID : this.item.id}})
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
