<template>
  <div class="comments d-flex flex-column justify-content-center align-items-center">
    <div class='w-75 d-flex justify-content-between'>
      <div>
        <span @click='toProfile(comment.author)'>
          {{ comment.author_name }} :
        </span>
        {{ comment.content }}
      </div>

      <div>
        <span style="margin-left:10px;" v-show="computedLike">{{ comment.comment_likes_count }}</span>

        <img class="logos" src="@/assets/img/like.png" @click="commentLike" v-if="computedLike"/>
        <img class="logos" src="@/assets/img/unlike.png" @click="commentLike" v-else/>
        <span v-if="authorIdentification">
          <img class="logos" src="@/assets/img/edit_icon.png" @click="edit = !edit"/>
          <img class="logos" src="@/assets/img/delete_icon.png" @click="commentDelete"/>
        </span>
      </div>
    </div>
    <div v-show="edit">
      <form @submit.prevent="commentEdit">
        <input type="text" v-model.trim="editText">
        <input type="submit" value="댓글수정"/>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name:"CommentItem",
  props: {
    comment: Object
  },
  data() {
    return {
      editText:"",
      edit:false
    }
  },
  computed: {
    computedLike() {
      return this.comment.liking_users.includes(this.$store.state.id)
    },
    authorIdentification () {
      return this.comment.author === this.$store.state.id
    }
  },
  created() {
    this.editText = this.comment.content
  },
  methods : {
    commentLike() {
      this.$emit('comment-liked', this.comment.id)
    },
    commentDelete() {
      this.$emit('comment-deleted', this.comment.id)
    },
    commentEdit() {
      if (this.editText) {
        this.$emit('comment-edited', this.comment.id, this.editText)
      }
    },
    toProfile(id) {
      this.$router.push({name:'profile', params: { 'userID' : id}})
    }
  },
}
</script>

<style scoped>
.logos {
  height:30px;
  width: 33px;
  /* margin-left:5px; */
}
</style>