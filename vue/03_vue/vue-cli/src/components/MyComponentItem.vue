<template>
  <div>
    <h3>나는 MyComponent의 하위 컴포넌트</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childToParent">클릭!</button>
    <input
      type="text"
      v-model='childInputData'
      @keyup.enter='childInput'
    >
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  data: function () {
    return {
      childInputData: null
    }
  },

  methods: {
    childToParent: function () {// 달러가 붙는 이유는 객체의 기본 특성값이기 때문, 새로 만드는 녀석이랑 겹치는거 방지
      this.$emit('child-to-parent', '나는 자식이 보낸 데이터다')  // 받는쪽이 html이기 때문에
    }, // emit(이름, 데이터)
    childInput: function () {
      this.$emit( 'child-input',this.childInputData)
      this.childInputData = null
    }
  },
}
</script>

<style>

</style>