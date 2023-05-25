<template>
  <div>
    <div class="Home-head mt-4">
      <MainAdvertise  :movie_id="visibleSlidesRecomendate.length > 0 ? visibleSlidesRecomendate[0].id :238"  />
    </div>
    <div class="Home-body" v-if="Recently">
      <MovieList title="Recomendate" :movies="visibleSlidesRecomendate" @wheel="handleWheelRecomendate" />
      <MovieList title="Recently" :movies="visibleSlidesRecently" @wheel="handleWheelRecently" />
      <MovieList title="Popular" :movies="visibleSlidesPopular" @wheel="handleWheelPopular" />
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue";
import MainAdvertise from "@/components/MainAdvertise.vue";

export default {
  name: "HomeView",
  components: {
    MovieList,
    MainAdvertise,
  },
  data() {
    return {
      currentSlideRecomendate: 0,
      currentSlideRecently: 0,
      currentSlidePopular: 0,
      maxSlides: 5,
      Recomendation:[],
      Recently:[],
      Popular:[]
    };
  },
  methods: {
    getMovies(){
      this.$store.dispatch('getMovies')
      this.Recomendation = this.$store.state.Recomendation
      this.Recently = this.$store.state.Recently
      this.Popular = this.$store.state.Popular
    },
    // Separate handleWheel methods for each list
    handleWheelRecomendate(event) {
      event.preventDefault();
      const delta = Math.sign(event.deltaY);
      if (delta > 0) {
        // Scrolling down (next slide)
        if (this.currentSlideRecomendate < this.Recomendation.length - this.maxSlides) {
          this.currentSlideRecomendate++;
        } else {
          this.currentSlideRecomendate = 0; // Wrap to the beginning
        }
      } else {
        // Scrolling up (previous slide)
        if (this.currentSlideRecomendate > 0) {
          this.currentSlideRecomendate--;
        } else {
          this.currentSlideRecomendate = this.Recomendation.length - this.maxSlides; // Wrap to the end
        }
      }
    },
    handleWheelRecently(event) {
      event.preventDefault();
      const delta = Math.sign(event.deltaY);
      if (delta > 0) {
        // Scrolling down (next slide)
        if (this.currentSlideRecently < this.Recently.length - this.maxSlides) {
          this.currentSlideRecently++;
        } else {
          this.currentSlideRecently = 0; // Wrap to the beginning
        }
      } else {
        // Scrolling up (previous slide)
        if (this.currentSlideRecently > 0) {
          this.currentSlideRecently--;
        } else {
          this.currentSlideRecently = this.Recently.length - this.maxSlides; // Wrap to the end
        }
      }
    },
    handleWheelPopular(event) {
      event.preventDefault();
      const delta = Math.sign(event.deltaY);
      if (delta > 0) {
        // Scrolling down (next slide)
        if (this.currentSlidePopular < this.Popular.length - this.maxSlides) {
          this.currentSlidePopular++;
        } else {
          this.currentSlidePopular = 0; // Wrap to the beginning
        }
      } else {
        // Scrolling up (previous slide)
        if (this.currentSlidePopular > 0) {
          this.currentSlidePopular--;
        } else {
          this.currentSlidePopular = this.Popular.length - this.maxSlides; // Wrap to the end
        }
      }
    },
  },
  created() {
    // Fetch the complete movie list for all three categories
    this.getMovies();
  },
  computed:{
    // Separate computed properties for each list
    visibleSlidesRecomendate() {
      if(!this.Recomendation){return []}
      const startIndex = this.currentSlideRecomendate;
      const endIndex = this.currentSlideRecomendate + this.maxSlides - 1;
      return this.Recomendation.slice(startIndex, endIndex + 1);
    },
    visibleSlidesRecently() {
      if(!this.Recently){return []}
      const startIndex = this.currentSlideRecently;
      const endIndex = this.currentSlideRecently + this.maxSlides - 1;
      return this.Recently.slice(startIndex, endIndex + 1);
    },
    visibleSlidesPopular() {
      if(!this.Popular){return []}
      const startIndex = this.currentSlidePopular;
      const endIndex = this.currentSlidePopular + this.maxSlides - 1;
      return this.Popular.slice(startIndex, endIndex + 1);
    },
    isDataLoaded() {
    return this.Recomendation && this.Recently && this.Popular;
    },
  }
};
</script>

<style scoped>
.Home-body {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.Home-head {
  display: flex;
  flex-direction: column;
  align-items: center;
}

</style>