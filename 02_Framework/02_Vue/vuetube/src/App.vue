<template>
  <div id="app">
    <img alt='Vue logo' src='./assets/logo.png'>
    <SearchBar @input-change='onInputChange'/>
    <MainVideo :video='mainVideo'/>
    <VideoList :videos='videos.slice(1)' @select-video-item='onMainVideoChange'/>
  </div>
</template>

<script>
import axios from 'axios'
import MainVideo from '@/components/MainVideo'
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    MainVideo,
    SearchBar,
    VideoList,
  },
  data() {
    return {
      inputValue: null,  // 사용자 검색어
      videos: [],  //검색 영상 목록
      mainVideo: null, // 메인 영상
    }
  },
  methods: {
    onInputChange(inputText) {
      this.inputValue = inputText
      console.log(API_URL)
      console.log(API_KEY)
      // Youtube API 이용하여 검색하기
      axios({
        method: 'get',
        url: API_URL,
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.inputValue,
        },
      })
        .then((response) => {
          console.log(response)
          this.videos = response.data.items  // 영상 목록
          console.log(this.videos)
          this.mainVideo = this.videos[0]  // 첫 영상이 메인 영상
        })
        .catch((error) => {
          console.log(error)
        })
      
    },
    onMainVideoChange(video) {
      this.mainVideo = video
    }

  }

}
</script>

<style>
</style>
