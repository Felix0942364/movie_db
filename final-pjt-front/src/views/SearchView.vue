<template>
  <div class="search">
    <form @submit.prevent="search">
      <input type="searchInput" id="searchInput" v-model="searchInput">
      <input type="submit" value="search">
    </form>
    <SingleMovie
    v-for="movie in movies"
    :key="movie.id"
    :movie="movie"
    />    
  </div>
</template>

<script>
import axios from 'axios'
import SingleMovie from '@/components/SingleMovie.vue'

export default {
  name: 'SearchView',
  components: {
    SingleMovie
  },
  data() {
    return {
      searchInput:null,
      movies:null
    }
  },
  methods: {
    search() {
      const TMDB_KEY = process.env.VUE_APP_TMDB_KEY
      axios({
        method:'get',
        baseURL: "https://api.themoviedb.org/3/search/movie",
        params: {
          query : this.searchInput,
          api_key : TMDB_KEY,
        } 
      })
        .then((res) => {
          console.log(res.data.results)
          this.movies = res.data.results
          this.searchInput = null
        })
        .catch(err => console.log(err))
    }
  }
}
</script>
