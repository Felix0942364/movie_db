<template>
  <tr>
    <th scope="row">{{ item.id }}</th>
    <td> {{ item.title }} </td>
    <td> {{ item.author }} </td>
    <td> {{ item }} </td>
  </tr>
</template>

<script>
export default {
  name:'TableItem',
  props: {
    item : Object
  }
}
</script>
