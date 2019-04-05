import VueRouter from 'vue-router'
import Home from './components/Home'
import Ping from './components/Ping'
import Pong from './components/Pong'
import ManageContent from './components/ManageContent'

const routes = [
  { path: '/', component: Home },
  { path: '/ping', component: Ping },
  { path: '/pong', component: Pong },
  { path: '/vixens', component: ManageContent }
]

const router = new VueRouter({
  routes, // short for `routes: routes`
  mode: "history"
})

export default router;