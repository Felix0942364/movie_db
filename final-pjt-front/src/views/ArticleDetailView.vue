<template>
  <div class="article">
    <h1>{{ article?.title }}</h1>
    <div v-html="article?.content"></div>
    <!-- <p>{{ article?.content }}</p> -->
    <p>{{ article?.created_at }}</p>
    <p>{{ article?.updated_at }}</p>
    <span v-show="computedLike"> {{ article?.article_likes_count }} </span>
    <button @click="articleLike" v-if="computedLike">♥</button>
    <button @click="articleLike" v-else>♡</button>
    <span v-if="authorIdentification">
      <button @click="articleEdit">Edit</button>
      <button @click="articleDelete">Delete</button>
    </span>

    <p>raw {{ article }}</p>
    <h2 v-if="article?.comment_count">댓글 : {{ article?.comment_count }} 개</h2>
    <h2 v-else>댓글을 달아주세요</h2>
    <CommentsList
    :comments="article.comment_set"
    @comment-created="commentCreate"
    @comment-deleted="commentDelete"
    @comment-edited="commentEdit"
    @comment-liked="commentLike"
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
  computed : {
    computedLike() {
      return this.article.liking_users.includes(this.$store.state.id)
    },
    authorIdentification () {
      return this.article.author === this.$store.state.id
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
        this.article = res.data
      })
      .catch(err => console.log(err))
    },

    commentCreate(comment) {
      axios({
        method: 'post',
        url: `${API_URL}/api/articles/${this.$route.params.articleID}/comments/`,
        data: {content : comment},
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.getArticle()
        })
        .catch(err => console.log(err))
    },

    articleDelete() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/articles/${this.$route.params.articleID}/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }        
      })
        .then(res => console.log(res))
        .catch(err => console.log(err))
      this.$router.push({name : 'articlelist'})
    },
    articleEdit() {
      return
    },
    articleLike() {
      axios({
        method: 'post',
        url: `${API_URL}/api/articles/${this.$route.params.articleID}/like/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }        
      })
        .then(() => this.getArticle())
        .catch(err => console.log(err))
    },
    
    commentDelete(id) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/comments/${id}/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }        
      })
        .then(() => this.getArticle())
        .catch(err => console.log(err))
    },
    commentEdit(id) {
      id
      return
    },
    commentLike(id) {
      axios({
        method: 'post',
        url: `${API_URL}/api/comments/${id}/like/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }        
      })
        .then(() => this.getArticle())
        .catch(err => console.log(err))
    }
  },
}
</script>
