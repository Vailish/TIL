<template>
  <div>
    <button @click="getDogImage">멍멍아 이리온</button><br><br>
    <img v-if="imgSrc" :src="imgSrc" alt="#"><br>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name:'DogComponent',
  data() {
    return {
      imgSrc: null,
    }
  },
  methods:{
    getDogImage() {
      const dogImageSearchURL = 'https://dog.ceo/api/breeds/image/random'
      
      axios({
        method: 'get',
        url: dogImageSearchURL
      })
        .then((response) => {
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  created() {  // create시점에 getDogImage를 호출하겠다
    this.getDogImage()
    console.log('Child created!')
    // create시점에서는 dom이 연결이 안되어있어서 조작X -> mounted에서 할 수 있음    // const button = document.querySelector('button')
    // button.innerText = '멍멍!'
    // axios 쓰는시점... dom 그리기 전이니까
  },
  mounted() {
    const button = document.querySelector('button')
    button.innerText = '멍멍!'
    console.log('Child mounted!')
  },
  updated() {
    console.log('새로운 멍멍이!')
    console.log('Child updated!')
  }
}
</script>

<style>

</style>
