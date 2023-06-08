import { createRouter, createWebHistory } from "vue-router"
import Home from "@/views/Home.vue"
import News from "@/views/News.vue"


const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/noticias',
    component: News
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router;
