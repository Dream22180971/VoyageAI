import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Result from '../views/Result.vue'
import Inspiration from '../views/Inspiration.vue'
import Guide from '../views/Guide.vue'
import Community from '../views/Community.vue'
import About from '../views/About.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/result', name: 'Result', component: Result, props: true },
  { path: '/inspiration', name: 'Inspiration', component: Inspiration },
  { path: '/guide', name: 'Guide', component: Guide },
  { path: '/community', name: 'Community', component: Community },
  { path: '/about', name: 'About', component: About }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
