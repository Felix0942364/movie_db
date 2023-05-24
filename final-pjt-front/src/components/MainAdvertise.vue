<template>
  <div class="card mx-3 mb-5">
    <img :src="pURL + MainMovie.backdrop_path" class="card-img" style="opacity: 0.4;"> 
    <div class="card-img-overlay d-flex align-items-center">
      <img :src="pURL + MainMovie.poster_path" class="img-thumbnail" style="max-height: 400px;">
      <div class="d-flex flex-column ms-5">
        <h1 class="card-title mb-5 mt-0" style="font-weight: bold;">{{ MainMovie.title }}</h1>
        <h5 class="card-text-bg-dark">{{ MainMovie.tagline }}</h5>
        <p style="text-overflow: ellipsis;" class="card-text-bg-dark">{{ MainMovie.overview }}</p>
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
  },
  computed: {  
    MainMovie() {
      return this.mainMovie
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
</style>