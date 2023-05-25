<template>
  <tr>
    <th scope="row">{{ item.article }}</th>
    <td> {{ item.content }} </td>
    <td> AUTHOR </td>
  </tr>
</template>

<script>
export default {
  name:'CommentTableItem',
  props: {
    item : Object
  }
}
</script>
