<template>
  <div>
    <div class="Home-head">
      <img width="120px" src="@/assets/img/big_logo_white.png">
    </div>
    <div class="Home-body">
      <div class="Trending">
        <!-- MovieCards -->
        <div class="popular-list row row-cols-1 row-cols-md-5 gy-3">
          <MovieCard
            v-for="(movie, idx) in TrendingList"
            :key="idx"
            :movie="movie"/>
        </div>
      </div>
      <div class="Popular_Year">
        <!-- MovieCards -->
        <div class="popular-list row row-cols-1 row-cols-md-5 gy-3">
          <MovieCard
            v-for="(movie, idx) in TrendingList"
            :key="idx"
            :movie="movie"/>
        </div>
      </div>
      <div class="Latest">
        <!-- MovieCards -->
        <div class="popular-list row row-cols-1 row-cols-md-5 gy-3">
          <MovieCard
            v-for="(movie, idx) in TrendingList"
            :key="idx"
            :movie="movie"/>
        </div>
      </div>     
    </div> 
  </div>
</template>
<script>
// @ is an alias to /src
// import CKEDITOR from 'https://cdn.ckeditor.com/ckeditor5/37.1.0/super-build/ckeditor.js'
export default {
  name: 'HomeView',
  components: {
  },
  // data(){
  //   return{
  //     TrendingList : []
  //   }
  // },
  methods:{
    getMovies(){
      this.$store.dispatch('getMovies')
    }
  },
  computed:{
    TrendingList(){
      return this.$store.state.movies
    }
  },
  created(){
    this.getMovies()
  }

}
</script>


