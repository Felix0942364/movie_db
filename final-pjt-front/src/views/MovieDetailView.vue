<template>
  <div class="MovieDetail">
    <img v-if="movie" :src="pURL + movie.backdrop_path" class="card-img-overlay "  style="opacity: 0.2; height:1200px;">
    <div class="MovieDetail-header img-overlay">
      <h1>{{ movie?.title }}</h1>
      <p>{{ movie?.tagline}}</p>
    </div>
    <div class="MovieDetail-body">
      <div class="video-container mx-2">
        <iframe :src="vURL" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
        <p>{{ movie?.overview }}</p>
        <span v-for="(genre,idx) in movie?.genres" :key="idx">{{genre.name}} </span>
        <p>{{ movie?.release_date }}</p>
    </div>
    <br>
    <p>{{ movie?.vote_average }}</p>
    <p>{{ movie?.vote_count }}</p>
    <!-- <span v-show="movie?.movie_likes_count != 0"> {{ movie?.movie_likes_count }} </span> -->
    <!-- <button @click="movieLike" v-if="computedLike">♥</button>
    <button @click="movieLike" v-else>♡</button> -->
    
    <hr>
    <MovieList title="Recommendations" :movies="visibleSlidesRecomendate" @wheel="handleWheelRecomendate" />
    <hr>
    <!-- <p>raw {{ movie }}</p> -->

  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue";
const TMDB_URL = 'https://api.themoviedb.org/3/movie/' 
import axios from 'axios'
export default {
  name: 'MovieDetailView',
  data() {
    return {
      pURL: 'https://image.tmdb.org/t/p/original/',
      movie: null,
      recommendations:[],
      vURL: null,
      currentSlideRecomendate: 0,
      maxSlides: 5,
    }
  },
  components:{
    MovieList
  },
  methods : {
    getmovie() {
      axios({
        method: 'get',
        url: TMDB_URL + this.$route.params.movie_id,
        params: {
          api_key: process.env.VUE_APP_TMDB_KEY,
          language: 'ko-KR',
          page: 1
        }
      })
      .then((res) => {
        console.log(res.data)
        this.movie = res.data
      })
      .catch(err => console.log(err))
    },
    getrecommendation(){
      axios({
        method: 'get',
        url: TMDB_URL + this.$route.params.movie_id + '/recommendations',
        params: {
          api_key: process.env.VUE_APP_TMDB_KEY,
          language: 'ko-KR',
          page: 1
        }
      })
      .then((res) => {
        this.recommendations = res.data.results
      })
      .catch(err => console.log(err))
    },
    gettrailer(){
      axios({
        method: 'get',
        url: TMDB_URL + this.$route.params.movie_id + '/videos',
        params: {
          api_key: process.env.VUE_APP_TMDB_KEY,
        }
      })
      .then((res) => {
        console.log(res)
        this.vURL = 'https://www.youtube.com/embed/'+ res.data.results[0]?.key
      })
      .catch(err => console.log(err))
    },
    handleWheelRecomendate(event) {
      event.preventDefault();
      const delta = Math.sign(event.deltaY);
      if (delta > 0) {
        // Scrolling down (next slide)
        if (this.currentSlideRecomendate < this.recommendations.length - this.maxSlides) {
          this.currentSlideRecomendate++;
        } else {
          this.currentSlideRecomendate = 0; // Wrap to the beginning
        }
      } else {
        // Scrolling up (previous slide)
        if (this.currentSlideRecomendate > 0) {
          this.currentSlideRecomendate--;
        } else {
          this.currentSlideRecomendate = this.recommendations.length - this.maxSlides; // Wrap to the end
        }
      }
    },
  },
  created(){
    this.getmovie()
    this.getrecommendation()
    this.gettrailer()
  },
  computed:{
    visibleSlidesRecomendate() {
      if(!this.recommendations){return []}
      const startIndex = this.currentSlideRecomendate;
      const endIndex = this.currentSlideRecomendate + this.maxSlides - 1;
      return this.recommendations.slice(startIndex, endIndex + 1);
    }
  },
  watch: {
    '$route.params.movie_id'(newValue, oldValue) {
      if (newValue !== oldValue) {
        this.getmovie()
        this.getrecommendation()
        this.gettrailer()
      }
    }
  }
}
</script>

<style scoped>
.video-container {
	position: relative;
	padding-bottom: 56.25%;
	padding-top: 30px;
	height: 0;
	overflow: hidden;
}
 
.video-container iframe,
.video-container object,
.video-container embed {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
}
</style>