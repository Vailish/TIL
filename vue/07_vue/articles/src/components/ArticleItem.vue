<template>
  <div @click='goDetail(article.id)'>
    <p>글 번호 : {{ article.id }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  methods: {
    goDetail(id) {  // 인자 비어있으면 이렇게 넘겨서 쓸 수 있음
      this.$router.push({ name: 'detail', params: {id} })
      // this.$router.push({ name: 'detail', params: {id: `${this.article.id}` }})  // 이렇게 해도됨
    }
  }
}
</script>

<style>

</style>