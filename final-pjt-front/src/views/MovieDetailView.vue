<template>
  <div class="MovieDetail card my-4 d-block mx-auto" style="width: 800px; ">
    <img v-if="movie" :src="pURL + movie.backdrop_path" class="card-img "  style="height: 1500px; opacity: 0.25; object-fit: cover;">
    <div class="MovieDetail-content card-img-overlay" style="">
      <div class="MovieDetail-header card-title my-3">
        <h1>{{ movie?.title }}</h1>
      </div>
      <div class="MovieDetail-body">
        <h4>{{ movie?.tagline}}</h4>
        <br>
        <div class="video-container my-3">
          <iframe 
          :src="vURL" 
          frameborder="1" 
          autoplay="1"
          allowfullscreen="1"
          width="720px"
          height="480px">
        </iframe>
        </div>
        <br>
        <h5 class="mx-5 lh-base">{{ movie?.overview }}</h5>
      </div>
      <br>
      <span v-for="(genre,idx) in movie?.genres" :key="idx">{{genre.name}} </span>
      <p>{{ movie?.release_date }}</p>
      <p>관객 평점: {{ movie?.vote_average  }}
      </p>
      <div class="MovieLike">
        <button @click="movieLike" v-if="true">♥</button>
        <button @click="movieLike" v-else>♡</button>
      </div>
    </div>
    <!-- <span v-show="movie?.movie_likes_count != 0"> {{ movie?.movie_likes_count }} </span> -->
    <br>
    <MovieList title="Recommendations" :movies="visibleSlidesRecomendate" @wheel="handleWheelRecomendate" />
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
    movieLike(){
      return
    }
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
</style>