import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store',
  },
  getters: {
    messageLength(state) {
      return state.message.length
    }
  },
  mutations: {
    CHANGE_MESSAGE(state, newMessage) {  // actions와 구분해서 mutations와 구분을 하기 위해서 대문자로씀
      console.log(state)
      console.log(newMessage)
      state.message = newMessage
    }
  },
  actions: {
    changeMessage(context, newMessage) { // context : vuex.Store의 모든 녀석을 나타냄
      // console.log(context)
      // console.log(newMessage)
      // context.commit('mutation 메서드 이름', newMessage)
      context.commit('CHANGE_MESSAGE', newMessage)
    }
  },
  modules: {
  }
})
