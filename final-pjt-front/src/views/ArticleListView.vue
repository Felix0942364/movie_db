<template>
  <div class="articlelist">
    <div class="container mt-3 p-3">
      <div class="d-flex justify-content-between align-items-center px-3 pt-2">
        <h1>게시판</h1>
        <button class="btn btn-secondary" @click="$router.push({name:'createArticle'})">새글 작성</button> 
      </div>
      <!-- <hr> -->
      <div class="px-3">
        <table class="table text-white mt-3">
          <thead>
            <tr>
              <th scope="col">게시글 번호</th>
              <th scope="col">제목</th>
              <th scope="col">작성자</th>
              <th scope="col">좋아요</th>
              <th scope="col">작성일자</th>
            </tr>
          </thead>
          <tbody>
            <ArticleListItem
            v-for="article in this.articles"
            :key="article.pk"
            :article="article"/>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'
import axios from 'axios'
 
export default {
  name: 'ArticleListView',
  data() {
    return {
      articles:null
    }
  },
  components: {
    ArticleListItem
  },
  created() {
    this.getArticles()
  },
  beforeRouteUpdate(to, from, next) {
    this.getArticles()
    next()
  },
  methods : {
    getArticles() {
      axios({
        method: 'get',
        url: `${process.env.VUE_APP_BE_API_BASE_URL}/api/articles/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        // .then(res => {this.articles = res.data})
        .then(res => {this.articles = res.data})
        .catch(err => console.log(err))
    },
  },
  computed : {
  }
}
</script>

<style scoped>
.container {
  border-radius: 1rem;
  background-color: rgba(255, 255, 255, 0.158);
}

table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border-bottom: 1px solid #ff7637;
  padding: 10px;
}
</style>