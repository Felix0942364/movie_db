<template>
  <div>
    {{ comment.content }}
    {{ comment.comment_likes_count }}
    <button @click="commentLike" v-if="computedLike">♥</button>
    <button @click="commentLike" v-else>♡</button>
    <span v-if="authorIdentification">
      <button @click="commentEdit">수정</button>
      <button @click="commentDelete">삭제</button>
    </span>
  </div>
</template>

<script>
export default {
  name:"CommentItem",
  props: {
    comment: Object
  },
  computed: {
    computedLike() {
      return this.comment.liking_users.includes(this.$store.state.id)
    },
    authorIdentification () {
      return this.comment.author === this.$store.state.id
    }
  },
  methods : {
    commentLike() {
      this.$emit('comment-liked', this.comment.id)
    },
    commentDelete() {
      this.$emit('comment-deleted', this.comment.id)
    },
    commentEdit() {
      this.$emit('comment-edited', this.comment.id)
    }
  },
}
</script>
