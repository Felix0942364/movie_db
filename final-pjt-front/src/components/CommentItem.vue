<template>
  <div>
    {{ comment.content }}
  </div>
</template>

<script>
export default {
  name:"CommentItem",
  props: {
    comment: Object
  }
}
</script>

<style>

</style>