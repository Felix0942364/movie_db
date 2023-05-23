<template>
  <div>
    <div class="Home-head">
      <img width="120px" src="@/assets/img/big_logo_white.png">
    </div>
    <div class="Home-body wrapper">
      <div class="Popular_Year">
        <div class="popular-list row row-cols-1 row-cols-md-5 gy-3"
        :style="{ transform: `translateX(${slideOffset}px)` }"
        @wheel="handleWheel">
          <MovieCard 
          v-for="(movie, idx) in visibleSlides"
          :key="idx"
          :movie="movie"/>
        </div>
      </div>
    </div> 
  </div>
</template>
<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard.vue'
export default {
  name: 'HomeView',
  components: {
    MovieCard
  },
  data(){
    return{
      currentSlide: 0,
      slideWidth: 20,
      currentOffset: 0,
      containerWidth: 900,
      maxSlides: 9,
      TrendingList : []
    }
  },

  methods:{
    getMovies(){
      this.$store.dispatch('getMovies')
      this.TrendingList = this.$store.state.movies
    },
    handleWheel(event) {
      event.preventDefault(); // Prevent default scrolling behavior
      
      const delta = Math.sign(event.deltaY); // Get the direction of the mouse wheel
      if (delta > 0) {
        // Scrolling down (next slide)
        if (this.currentSlide < this.TrendingList.length - this.maxSlides) {
          this.currentSlide++;
        } else {
          this.currentSlide = 0; // Wrap to the beginning
        }
      } else {
        // Scrolling up (previous slide)
        if (this.currentSlide > 0) {
          this.currentSlide--;
        } else {
          this.currentSlide = this.TrendingList.length - this.maxSlides; // Wrap to the end
        }
      
      }
    },
  },
  computed:{
    visibleSlides() {
    const maxSlides = Math.floor(this.containerWidth / (this.slideWidth * this.containerWidth / 100));
    const startIndex = this.currentSlide;
    const endIndex = this.currentSlide + maxSlides - 1;
    console.log(maxSlides)
    return this.TrendingList.slice(startIndex, endIndex + 1);
  },
    slideOffset() {
      // Calculate the horizontal offset to move the slides
      return -this.currentSlide * this.slideWidth * this.containerWidth / 100;
    },
  },
  created(){
    this.getMovies()
    this.containerWidth = document.getElementById('popular-list').clientWidth;
  }

}
</script>


<style>
.Home-body {
  overflow: hidden;
}

.popular-list {
  display: flex;
  transition: transform 0.5s;
  flex-wrap: nowrap; /* Prevent slides from wrapping */
  overflow: hidden; /* Hide overflow for responsive behavior */
}


.slide {
  flex: 0 0 auto; /* Allow slides to shrink and grow based on container width */
  width: 100%; /* Occupy full width of the container */
  max-width: 20%; /* Maximum width for each slide */
  box-sizing: border-box; /* Include padding and border in width calculation */
}

</style>