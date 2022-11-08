import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    imgSrc: 'https://pbs.twimg.com/media/DkdzUXwVsAAxypO?format=jpg&name=small'
  },
  getters: {
  },
  mutations: {
    GET_CAT_SUCCESS(state, response) {
      state.imgSrc = response.data[0].url
    },
    GET_CAT_FAILURE(error) {
      console.log(error)
    }
  },
  actions: {
    getCatImage: function({ commit }) {
      const requestUrl = 'https://api.thecatapi.com/v1/images/search'

      axios.get(requestUrl)
      .then((response) => {
        commit('GET_CAT_SUCCESS', response)
      })
      .catch((error) =>{
        commit('GET_CAT_FAILURE', error)
      })
    }
    
  },
})
