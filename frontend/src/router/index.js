import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/result', name: 'Result', component: () => import('../views/Result.vue'), props: true },
  { path: '/inspiration', name: 'Inspiration', component: () => import('../views/Inspiration.vue') },
  { path: '/guide', name: 'Guide', component: () => import('../views/Guide.vue') },
  { path: '/community', name: 'Community', component: () => import('../views/Community.vue') },
  { path: '/about', name: 'About', component: () => import('../views/About.vue') }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
