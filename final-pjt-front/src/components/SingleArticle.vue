<template>
  <div class="hello">
    <h5>{{ article.title }} : {{ article.content }}</h5>
  </div>
</template>

<script>
export default {
  name: 'SingleArticle',
  props: {
    article:Object
  }
}
</script>
