<template>
  <div>
    <ul>
      <VideoListItem
        v-for="(video, index) in videos"
        :key='`videoListItem-${index}`'
        :video='video'
        @select-video-item='selectVideoItem'
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    selectVideoItem(video) {
      this.$emit('select-video-item', video)
    }
  }
}
</script>

<style>

</style>