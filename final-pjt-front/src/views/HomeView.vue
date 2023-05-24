<template>
  <div>
    <div class="Home-head">
      <img width="120px" src="@/assets/img/big_logo_white.png">
    </div>
    <div class="Home-body ">
      <div class="container mb-5" id="recomendate">
        <h1 class="d-flex justify-content-start">Recomendate</h1>
        <div class="popular-list row gy-3 "
        :style="{ transform: `translateX(${slideOffset}px)` }"
        @wheel="handleWheel">
          <MovieCard 
          v-for="(movie, idx) in visibleSlides"
          :key="idx"
          :movie="movie"/>
        </div>
      </div>  
      <div class="Popular_Year container">
        <h1 class="d-flex justify-content-start">Popular_Year</h1>
        <div class="popular-list row gy-3 "
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
      maxSlides: 5,
      TrendingList : []
    }
  },

  methods:{
    getMovies(){
      this.$store.dispatch('getMovies')
      this.TrendingList = this.$store.state.movies
    },
    handleWheel(event) {
      // this.UpdatemaxSlides()
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
    UpdatemaxSlides(){
      const container = document.querySelector('.popular-list');
      var containerWidth = container?.clientWidth ? container.clientWidth : 1200 
      // Determine the number of visible slides based on Bootstrap breakpoints
      if (containerWidth >= 1200) {
        this.maxSlides= 5; // Number of slides for large screens (>= 1200px)
        } else if (containerWidth >= 992) {
          this.maxSlides= 4; // Number of slides for medium screens (992px - 1199px)
        } else if (containerWidth >= 768) {
          this.maxSlides= 3; // Number of slides for small screens (768px - 991px)
        } else if (containerWidth >= 576) {
          this.maxSlides= 2; // Number of slides for extra small screens (576px - 767px)
        } else {
          this.maxSlides= 1; // Number of slides for extra small screens (< 576px)
        }
    },
  },
  computed:{
    
    visibleSlides() {
    const startIndex = this.currentSlide;
    const endIndex = this.currentSlide + this.maxSlides - 1;
    return this.TrendingList.slice(startIndex, endIndex + 1);
  },
    slideOffset() {
      // Calculate the horizontal offset to move the slides
      return -this.currentSlide * this.slideWidth * this.containerWidth / 100;
    },
  },
  created(){
    this.getMovies()
  },

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