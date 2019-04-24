import VueRouter from 'vue-router'
import Home from './components/Home'
import ManageContent from './components/ManageContent'
import ManageImages from './components/ManageImages'
import VixenDetail from './components/VixenDetail'

const routes = [
  { path: '/', component: Home },
  { path: '/vixens', component: ManageContent },
  { path: '/vixens/:id', component: VixenDetail },
  { path: '/images', component: ManageImages }
]

const router = new VueRouter({
  routes, // short for `routes: routes`
  mode: "history"
})

export default router;