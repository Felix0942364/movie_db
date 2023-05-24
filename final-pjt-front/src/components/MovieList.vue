<template>
  <div class="container mb-5">
    <h3 class="d-flex justify-content-start">{{ title }}</h3>
    <div class="movie-list row gy-3"
      :style="{ transform: `translateX(${slideOffset}px)` }"
      @wheel="$emit('wheel', $event)">
      <MovieCard
        v-for="(movie, idx) in movies"
        :key="idx"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard.vue";

export default {
  name: "MovieList",
  components: {
    MovieCard,
  },
  props: {
    title: {
      type: String,
      required: true,
    },
    movies: {
      type: Array,
      required: true,
    },
  },
  computed: {
    slideOffset() {
      // Calculate the horizontal offset to move the slides
      return -this.currentSlide * this.slideWidth * this.containerWidth / 100;
    },
  },
  // Assuming the slideWidth and containerWidth properties are available
};
</script>

<style scoped>
.movie-list {
  display: flex;
  transition: transform 0.5s;
  flex-wrap: nowrap;
  overflow: hidden;
}

.slide {
  flex: 0 0 auto;
  width: 100%;
  max-width: 20%;
  box-sizing: border-box;
}
</style>