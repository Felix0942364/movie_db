<template>
  <div class="search mt-5">
    <form @submit.prevent="search">
      <input type="searchInput" id="searchInput" v-model="searchInput">
      <input type="submit" value="search">
    </form>
    <div class="my-3">
      <h1 v-if="query===null&&searchInput===null">검색어를 입력하시오~~!</h1>
      <h1 v-if="query"><span style="text-decoration: underline;">{{ query }}</span>에 대한 검색 결과 {{ movies.length }} 건 <button @click="query=null;movies=[]">X</button></h1>
    </div>
    <div class="container gy-3 mx-auto mt-5">
      <div class="row">
        <SingleMovie
          v-for="movie in movies"
          :key="movie.id"
          :movie="movie"
          />
          <infinite-loading @infinite="infiniteHandler">
            <div slot="no-more" style="color: rgb(102, 102, 102); font-size: 14px; padding: 10px 0px;">목록의 끝입니다 :)</div>
          </infinite-loading> 
      </div>
    </div>
  </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'
import SingleMovie from '@/components/SingleMovie.vue'
export default {
  name: 'SearchView',
  components: {
    SingleMovie,
    InfiniteLoading
  },
  data() {
    return {
      searchInput:null,
      query:null,
      movies:[]
    }
  },
  methods: {
    infiniteHandler(){
      console.log(123)
    },
    search() {
      const TMDB_KEY = process.env.VUE_APP_TMDB_KEY
      this.query = this.searchInput
      axios({
        method:'get',
        baseURL: "https://api.themoviedb.org/3/search/movie",
        params: {
          language:'ko-KR',
          query : this.searchInput,
          api_key : TMDB_KEY,
        } 
      })
        .then((res) => {
          console.log(res.data.results)
          let buffer = []
          res.data.results.forEach(movie => {
            if(movie.poster_path){
              buffer.push(movie)
            }
          });
          this.movies = buffer
          this.searchInput = null
        })
        .catch(err => console.log(err))
    }
  }
}
</script>
