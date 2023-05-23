<template>
  <div class="comments">
    {{ comment.content }}
    <span v-show="computedLike">{{ comment.comment_likes_count }}</span>
    <img class="logos" src="@/assets/img/like.png" @click="commentLike" v-if="computedLike"/>
    <img class="logos" src="@/assets/img/unlike.png" @click="commentLike" v-else/>
    <span v-if="authorIdentification">
      <img class="logos" src="@/assets/img/edit_icon.png" @click="commentEdit"/>
      <img class="logos" src="@/assets/img/delete_icon.png" @click="commentDelete"/>
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
