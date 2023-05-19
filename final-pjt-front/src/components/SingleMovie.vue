<template>
  <div class="hello">
    <img
    :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"/>
    <h1>{{ movie.title }}</h1>
    <h1>{{ movie.overview }}</h1>
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
