<template>
  <div class="article mt-3 p-3">
    <h1 class="mt-3">{{ article?.title }}</h1>
    <h2 @click='toProfile(article.author)'> by {{article?.author_name}}</h2>
    <div class="mx-3 my-2">
      <div v-html="article?.content"></div>
    </div>
    <p>생성: 
      <span>{{ article?.created_at.slice(0,4) }}년 </span>
      <span>{{ article?.created_at.slice(5,7) }}월 </span>
      <span>{{ article?.created_at.slice(8,10) }}일 </span>
      <span>{{ article?.created_at.slice(11,13) }}시 </span>
      <span>{{ article?.created_at.slice(14,16) }}분 </span>
      <span>{{ article?.created_at.slice(17,19) }}초 </span>
    </p>
    <p>수정: 
      <span>{{ article?.updated_at.slice(0,4) }}년 </span>
      <span>{{ article?.updated_at.slice(5,7) }}월 </span>
      <span>{{ article?.updated_at.slice(8,10) }}일 </span>
      <span>{{ article?.updated_at.slice(11,13) }}시 </span>
      <span>{{ article?.updated_at.slice(14,16) }}분 </span>
      <span>{{ article?.updated_at.slice(17,19) }}초 </span>
    </p>
    <span v-show="article?.article_likes_count != 0"> {{ article?.article_likes_count }} </span>
    
    <!-- <button @click="articleLike" v-if="computedLike">♥</button>
    <button @click="articleLike" v-else>♡</button>
    <span v-if="authorIdentification">
      <button @click="articleEdit">Edit</button>
      <button @click="articleDelete">Delete</button>
    </span> -->
    <img class="logos" src="@/assets/img/like.png" @click="articleLike" v-if="computedLike"/>
    <img class="logos" src="@/assets/img/unlike.png" @click="articleLike" v-else/>
    <span v-if="authorIdentification">
      <img class="logos" src="@/assets/img/edit_icon.png" @click="articleEdit"/>
      <img class="logos" src="@/assets/img/delete_icon.png" @click="articleDelete"/>
    </span>

    <hr>
    <h3 v-if="article?.comment_count">댓글 : {{ article?.comment_count }} 개</h3>
    <h3 v-else>댓글을 달아주세요</h3>
    <CommentsList
    :comments="article?.comment_set"
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
      return this.article?.liking_users.includes(this.$store.state.id)? true:false
    },
    authorIdentification () {
      return this.article?.author === this.$store.state.id
    }
  },
  created() {
    this.getArticle()
  },
  methods : {
    getArticle() {
      axios({
        method: 'get',
        url: API_URL + `/api/articles/${this.$route.params.articleID}/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.article = res.data
      })
      .catch(err => console.log(err))
    },

    toProfile(id) {
      this.$router.push({name:'profile', params: { 'userID' : id}})
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
      this.$router.push({name:'editArticle',params:{articleID:this.$route.params.articleID}})
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
    commentEdit(id, text) {
      axios({
        method: 'put',
        url: `${API_URL}/api/comments/${id}/`,
        data: {
          'content' : text 
        },
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }        
      })
        .then(() => this.getArticle())
        .catch(err => console.log(err))
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

<style scoped>
.article{
  max-width: 800px;
  margin: auto;
  background-color: burlywood;
}
.logos {
  height:40px;
  width: 45px;
  /* margin-left:5px; */
}
</style>