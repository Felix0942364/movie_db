import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index.js'

import HomeView from '@/views/HomeView.vue'
import SearchView from '@/views/SearchView.vue'
import CommunityView from '@/views/CommunityView.vue'

import ProfileView from '@/views/ProfileView.vue'
import SingupView from '@/views/SignupView.vue'
import LoginView from '@/views/LoginView.vue'

import ArticleListView from '@/views/ArticleListView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleEditView from '@/views/ArticleEditView.vue'

import MovieDetailView from '@/views/MovieDetailView.vue'

import ErrorView from '@/views/ErrorView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
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
    path: '/community/article/:articleID',
    name: 'articleDetail',
    component: ArticleDetailView
  },
  {
    path: '/community/create',
    name: 'createArticle',
    component: ArticleCreateView
  },
  {
    path: '/community/edit/:articleID',
    name: 'editArticle',
    component: ArticleEditView
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
  {
    path: '/detail/:movie_id',
    name: 'detail',
    component: MovieDetailView
  },
  {
    path: '*',
    name: 'error',
    component: ErrorView
  }
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const auth = store.getters["isAuthenticated"]
  const authPages = [
    'home',
    'search',
    'community',
    'articledetail',
    'createArticle',
    'watchlists',
    'articlelist',
    'profile',
  ]
  const isAuthRequired = authPages.includes(to.name)
  
  if (isAuthRequired && !auth) {
    next({name:'login'})
  } else {
    next()
  }
})

export default router