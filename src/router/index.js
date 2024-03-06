import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FPRouter from '../views/FPRouter.vue'
import CadastrarQuestoesRoutes from '../views/CadastrarQuestoesRouter.vue'
import FDBRouter from '../views/FBDRouter.vue'
import EngSoftRouter from '../views/EngSoftRouter.vue'
import RedesRouter from '../views/RedesRouter.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/cadastrar_questoes',
    name: '/cadastrar_questoes',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/CadastrarQuestoesRouter.vue')
  },
  {
    path: '/fundamentos_de_programacao',
    name: 'fundamentos_de_programacao',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/FPRouter.vue')
  },
  {
    path: '/fundamento_banco_de_dados',
    name: 'fundamento_banco_de_dados',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/FBDRouter.vue')
  },
  {
    path: '/engenharia_de_software',
    name: 'engenharia_de_software',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/EngSoftRouter.vue')
  },
  {
    path: '/redes',
    name: 'redes',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/RedesRouter.vue')
  },
  {
    path: '/questoes_erradas',
    name: 'questoes_erradas',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/RevisarQuestoesRouter.vue')
  },
  {
    path: '/sistemas_operacionais',
    name: 'sistemas_operacionais',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/SistemasOperacionais.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

