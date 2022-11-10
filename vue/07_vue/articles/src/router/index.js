import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'
import CreateView from '../views/CreateView.vue'
import DetailView from '../views/DetailView.vue'
import NotFound404 from '../views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    path: '/404-not-found',  // 숫자로 시작하기 때문에 detail 보다 위로 올림, 아니면 주소를 바꿔야함
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/:id',
    name: 'detail',
    component: DetailView
  },
  {
    path: '*',  // detail이 마지막이기 때문에 이거 없어도 404로 넘어감, 그래도 보통 사용해야하는 경우가 많음
    redirect: { name: 'NotFound404' }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
