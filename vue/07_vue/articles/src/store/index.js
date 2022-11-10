import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    article_id: 3,
    articles: [
    {
      id: 1,
      title: 'title',
      content: 'content',
      createdAt: new Date().getTime(),  // db가 없기 때문에 새로 랜더링되는것..
    },
    {
      id: 2,
      title: 'title2',
      content: 'content2',
      createdAt: new Date().getTime(),
    },
]
  },
  getters: {
  },
  mutations: {
    CREATE_ARTICLE(state, article) {
      state.articles.push(article)
      state.article_id = state.article_id + 1  // style guid에서는 ++ 권장X
    },
    DELETE_ARTICLE(state, article_id) {
      state.articles = state.articles.filter((article) => {
        return !(article.id === article_id)
      })
    },
  },
  actions: {
    createArticle(context, payload) {
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createAt: new Date().getTime()
      }
      context.commit('CREATE_ARTICLE', article)
    }
  },
  modules: {
  }
})
