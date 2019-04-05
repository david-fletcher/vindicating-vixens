import VueRouter from 'vue-router'
import Home from './components/Home'
import ManageContent from './components/ManageContent'

const routes = [
  { path: '/', component: Home },
  { path: '/vixens', component: ManageContent }
]

const router = new VueRouter({
  routes, // short for `routes: routes`
  mode: "history"
})

export default router;