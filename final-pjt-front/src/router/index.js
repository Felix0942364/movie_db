import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchView from '../views/SearchView.vue'
import CommunityView from '../views/CommunityView.vue'
import WatchlistView from '../views/WatchlistView.vue'
import ProfileView from '../views/ProfileView.vue'
import ArticleListView from '../views/ArticleListView.vue'
import SingupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/watchlist',
    name: 'watchlist',
    component: WatchlistView
  },
  {
    path: '/watchlist/articlelist',
    name: 'articlelist',
    component: ArticleListView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SingupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router