<template>
  <!-- 무조건 어떤거든 최상위 태그가 필요함, 안쓰면 오류남 -->
  <div class='border'>
    <h1>예~~ 이것은 내가 만든 새로운 컴포넌트다!</h1>
    <MyComponentItem
      static-props='MyComponent에서 보낸 데이터'
      :dynamic-props='dynamicProps'
      @child-to-parent='parentGetEvent'
      @child-input='getDynamicData'
    />
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',  // 파일명 써주면 됨, 굳이 다르게 할 필요는 없음
  components: {
    // 2. 등록하기
    MyComponentItem,
  },
  data: function () {  // 스코프 문제 떄문에 반드시 return값으로 데이터 잡아줘야함
    return {
      dynamicProps: '이건 동적인 데이터!',
    }
  },
  methods: {
    parentGetEvent: function (childData) {
      console.log('자식 컴포넌트에서 발생한 emit 이벤트를 들었다!!')
      console.log(childData)
    },
    getDynamicData: function (childInputData) {
      console.log(`사용자가 입력한 값은 ${childInputData}입니다.`)
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>