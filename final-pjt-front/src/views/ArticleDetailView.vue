<template>
  <div class="article">
    <h1>{{ article?.title }}</h1>
    <div v-html="article?.content"></div>
    <!-- <p>{{ article?.content }}</p> -->
    <p>{{ article?.created_at }}</p>
    <p>{{ article?.updated_at }}</p>
    <ArticleLikes/>

    <h2 v-if="article.like_user">♥♡</h2>

    <p>raw {{ article }}</p>
    <h2 v-if="article?.comment_count">댓글 : {{ article?.comment_count }} 개</h2>
    <h2 v-else>댓글을 달아주세요</h2>
    <CommentsList
    :comments="article.comment_set"
    @comment-created="createComment"
    />
  </div>
</template>

<script>
import CommentsList from '@/components/CommentsList.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  components: {
    CommentsList
  },
  data() {
    return {
      article: null,
    }
  },
  created() {
    this.getArticle()
  },
  methods : {
    getArticle() {
      axios({
        method: 'get',
        url: API_URL + "/api/articles/" + this.$route.params.articleID,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        // console.log(res.data)
        this.article = res.data
      })
      .catch(err => console.log(err))
    },
    createComment(comment) {
      axios({
        method: 'post',
        url: API_URL + "/api/articles/" + this.$route.params.articleID + '/comments/',
        data: {content : comment},
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.getArticle()
        })
        .catch(err => console.log(err))
    }
  }
}
</script>
