<template>
    <div class="col my-3">
    <div class="card h-100 mx-auto shadow-lg ">
      <img :src='pURL+movie.poster_path' class="card-img-top"> 
      <!-- <div class="card-body">
        <h5 class="card-title" style="font-weight: bold;">{{ movie.title }}</h5>
        <p class="card-text">{{ movie.overview }}</p>
      </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  data(){
    return{pURL:'https://image.tmdb.org/t/p/original/'}
  },
}
</script>

<style scoped>
.card-text {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}


</style>
