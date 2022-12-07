<template>
  <div>
    <li @click="selectVideoItem">
      <img :src="video.snippet.thumbnails.default.url" alt="video-thumbnail">
      <span>{{ video.snippet.title }}</span>
    </li>
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods: {
    selectVideoItem() {
      this.$emit('select-video-item', this.video)
    }
  }
}
</script>

<style>

</style>