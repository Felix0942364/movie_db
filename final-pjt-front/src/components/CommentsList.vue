<template>
  <div>
    <form @submit.prevent="createComment">
      <input type="text" id="commentInput" v-model.trim="commentInput">
      <input type="submit" value="댓글입력"/>
    </form>
    <CommentItem
    v-for="comment in comments"
    :key="comment.id"
    :comment="comment"/>
  </div>
</template>

<script>
import CommentItem from '@/components/CommentItem.vue'

export default {
  name: 'CommentsList',
  components: {
    CommentItem,
  },
  data() {
    return {
      commentInput : null,
    }
  },
  props: {
    comments:Object,
  },
  methods : {
    createComment() {
      if (this.commentInput) {
        this.$emit("comment-created", this.commentInput)
        this.commentInput=null
      } else {
        alert('댓글 내용을 입력해주세요')
      }
    }
  }
}
</script>
