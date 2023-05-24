<template>
  <div class="movie-item col-2 mb-3">
    <img
    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="img-fluid"/>
  </div>
</template>

<script>
export default {
  name: 'SingleMovie',
  props: {
    movie:Object
  }
}
</script>

<style scoped>
img{
  aspect-ratio: 1/2
}
.movie-item {
  /* position: relative; */
  /* display: block; */
  /* flex: 1 1 0px; */
  transition: transform 500ms;
}

.movie-item:hover {
  cursor: pointer;
}

.movie-item:focus,
.movie-item:hover {
  transform: scale(1.4);
  z-index: 1;
}

.popular-list:focus-within ~ .movie-item,
.popular-list:hover ~ .movie-item {
  transform: translateX(-25%);
}

.movie-item:focus  .movie-item,
.movie-item:hover  .movie-item {
  transform: translateX(25%);
}
</style>