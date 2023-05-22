<template>
  <div>
    <button @click.prevent=""/>
  </div>  
</template>

<script>
export default {
  name:'ArticleLikes',
  props: {
    articleID : Int16Array
  },
  data() {
    articleLikes : 0
  },
  created() {
    this.getLike()
  },
  methods : {
    getLike() {
      axios({
        method: 'get',
                
      })
    }
  }
}
</script>