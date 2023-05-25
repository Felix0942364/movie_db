<template>
  <div class="col my-3 mx-3 shadow wrapper" @click="godetail">
    <div class="card front-face ">
        <img :src='pURL+movie.poster_path' class="card-img-top h-100"> 
    </div>
    <div class="card h-100 back-face">
      <h4 class="card-title" style="font-weight: bold;">{{ movie.title }}</h4>
      <h5 class="card-subtitle">{{ movie?.tagline }}</h5>
      <p class="card-text">{{ movie.overview }}</p>
    </div>
  </div>
</template>

<script>
// import MovieDetailView from '@/views/MovieDetailView.vue';
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  components:{
    // MovieDetailView
  },
  data(){
    return{pURL:'https://image.tmdb.org/t/p/original/'}
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

.card-text {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  font-size:10%
}

::selection{
  color: #e2742a;
}
.wrapper{
  height: 150px;
  width: 100px;
  position: relative;
  transform-style: preserve-3d;
  perspective: 1000px;
}
.wrapper .card{
  position: absolute;
  height: 100%;
  width: 100%;
  padding: 5px;
  background: #f8d2b1;
  border-radius: 5%;
  transform: translateY(0deg);
  transform-style: preserve-3d;
  backface-visibility: hidden;
  box-shadow: 0px 10px 15px rgba(0,0,0,0.1);
  transition: transform 0.7s cubic-bezier(0.4,0.2,0.2,1);
}
.wrapper:hover > .front-face{
  transition-delay:0.5s;
  transform: rotateY(-180deg);
}
.wrapper .card img{
  height: 100%;
  width: 100%;
  /* object-fit: cover; */
  border-radius: 10px;
}
.wrapper .back-face{
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  flex-direction: column;
  transform: rotateY(180deg);
}
.wrapper:hover > .back-face{
  transition-delay:0.5s;
  transform: rotateY(0deg);
}
.wrapper .back-face img{
  height: 150px;
  width: 150px;
  padding: 5px;
  border-radius: 50%;
  background: linear-gradient(375deg, #1cc7d0, #2ede98);
}
.wrapper .back-face .info{
  text-align: center;
}
.back-face .info .title{
  font-size: 30px;
  font-weight: 500;
}
/* .back-face ul{
  display: flex;
} */

.back-face ul a:hover{
  color: #1cc7d0;
  border-color: #1cc7d0;
  background: linear-gradient(375deg, transparent, transparent);
}
</style>
