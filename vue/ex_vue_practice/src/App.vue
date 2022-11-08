<template>
  <div id="app">
    <h1>Cat Image</h1>
    <button @click="getCatImage">Get Cat</button>
    <img :src='imgSrc' alt='고양이사진임!'>
  </div>
</template>
 
<script>

export default {
  name: 'App',
  computed: {
    imgSrc() {
      return this.$store.state.imgSrc
    }
  },
  methods: {
    getCatImage() {
      return this.$store.dispatch('getCatImage')
    },
  },
  mounted() {
    // this.getCatImage()
  },
  updated() {
    console.log('이미지 리소스가 업데이트 되었습니다.')
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
