<template>
  <div class="card mx-3 mb-5" @click="godetail">
    <img v-if="MainMovie" :src="pURL + MainMovie.backdrop_path" class="card-img" style="opacity: 0.2; max-height:650px;">
    <div class="card-img-overlay d-flex align-items-center card-overlay">
      <div class="d-flex mx-5 me-5 overlay-content">
        <div class="me-4">
          <img v-if="MainMovie" :src="pURL + MainMovie.poster_path" class="img-thumbnail" style="max-width: 400px;">
        </div>
        <div class="d-flex flex-column justify-content-center">
          <h1 class="card-title mb-4" style="font-weight: bold;" v-if="MainMovie">{{ MainMovie.title }}</h1>
          <h5 class="card-text-bg-dark" v-if="MainMovie">{{ MainMovie.tagline }}</h5>
          <p style="text-overflow: ellipsis;" class="card-text-bg-dark" v-if="MainMovie">{{ MainMovie.overview }}</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'MovieListItem',
  props: {
    movie_id: Number
  },
  data() {
    return {
      pURL: 'https://image.tmdb.org/t/p/original/',
      mainMovie: null
    }
  },
  methods: {
    getMovieDetail(id) {
      return axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${id}`,
        params: {
          api_key: process.env.VUE_APP_TMDB_KEY,
          language: 'ko-KR',
          page: 1
        }
      })
      .then((res) => {
        return res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    godetail(){
      if(this.$route.params.movie_id != this.movie_id){
        this.$router.push({name:'detail',params:{movie_id:this.movie_id}})
      }
    }
  },
  computed: {  
    MainMovie() {
      return this.mainMovie
    }
  },
  watch: {
    movie_id(newVal) {
      this.getMovieDetail(newVal)
        .then((data) => {
          this.mainMovie = data
        })
    }
  },
  mounted() {
    this.getMovieDetail(this.movie_id)
      .then((data) => {
        this.mainMovie = data
      })
  }
}


</script>

<style scoped>
.card-overlay {
  max-height: 1000px;
  overflow-y: auto;
}

.overlay-content {
  max-width: 100%;
  padding-right: 1rem; /* Add some padding to prevent content from sticking to the edge */
}
</style>