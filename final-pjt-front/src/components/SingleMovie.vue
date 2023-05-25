<template>
  <div class="movie-item col-lg-2 col-md-3 col-sm-4 mb-3" @click="godetail">
    <img
    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="img-fluid"/>
  </div>
</template>

<script>
export default {
  name: 'SingleMovie',
  props: {
    movie:Object
  },
  methods:{
    godetail(){
      if(this.$route.params.movie_id != this.movie.id){
        this.$router.push({name:'detail',params:{movie_id:this.movie.id}})
      }
    }
  }
}
</script>

<style scoped>
img{
  aspect-ratio: 1/2
}
.movie-item {

  transition: transform 500ms;
}

.movie-item:hover {
  cursor: pointer;
}

/* .movie-item:focus, */
.movie-item:hover {
  transform: scale(1.4);
  z-index: 1;
}

</style>