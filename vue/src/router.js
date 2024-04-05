import { createMemoryHistory, createRouter } from 'vue-router'

import HomeView from './components/homepage.vue'

const routes = [
  { path: '/home', component: HomeView}
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router;
