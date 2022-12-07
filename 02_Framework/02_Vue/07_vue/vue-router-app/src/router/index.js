import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView'
import LoginView from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'
import DogView from '@/views/DogView'

Vue.use(VueRouter) // django urls.py랑 비슷...

const isLoggedIn = true

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  { // 얘가 lazy-loading임, 위랑 같은 거지만, 차이점이 있다면 미리 로딩을하냐 그 차이임.
    // 첫 로딩에 렌더링 하지않고 해당 라우터가 동작할 때 컴포넌트를 랜더링 함
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.  // 지연로딩
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 되어있음')
        next({ name: 'home'})
      } else {
        next()
      }
    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView,
  },
  {
    path: '*',
    redirect: '/404',
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// // 전역가드
// router.beforeEach((to, from, next) => {
//   // console.log('to', to)      // to : 이동할 URL 정보가 담긴 Route 객체
//   // console.log('from', from)  // 
//   // console.log('next', next)
//   // next()

//   // 로그인 여부
//   const isLoggedIn = false
//   // 로그인이 필요한 페이지
//   // const authPages = ['hello', 'home', 'about']
//   const allowAllpages = ['login']

//   // const isAuthRequired = authPages.includes(to.name)
//   const isAuthRequired = !allowAllpages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn ) {
//     console.log('login으로 이동!')
//     next({ name: 'login' })
//   } else {
//     console.log('to로 이동!')
//     next()
//   }
// })

export default router
