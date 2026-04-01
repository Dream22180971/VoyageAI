import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Result from '../views/Result.vue'

// 导入页面组件（如果存在）
// import Inspiration from '../views/Inspiration.vue'
// import Guide from '../views/Guide.vue'
// import Community from '../views/Community.vue'
// import About from '../views/About.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/result',
    name: 'Result',
    component: Result,
    props: true
  },
  {
    path: '/inspiration',
    name: 'Inspiration',
    component: Home // 暂时使用Home组件，后续可以替换为专门的页面
  },
  {
    path: '/guide',
    name: 'Guide',
    component: Home // 暂时使用Home组件，后续可以替换为专门的页面
  },
  {
    path: '/community',
    name: 'Community',
    component: Home // 暂时使用Home组件，后续可以替换为专门的页面
  },
  {
    path: '/about',
    name: 'About',
    component: Home // 暂时使用Home组件，后续可以替换为专门的页面
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
