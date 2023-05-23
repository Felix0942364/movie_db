import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
// import { get } from 'core-js/core/dict'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins : [
    createPersistedState(),
  ],
  state: {
    movies: null,
    articles: null,
    watchlists: null,
    token: null
  },
  getters: {
    isAuthenticated(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    GET_MOVIES(state, movies){
      state.movies = movies
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    GET_WATCHLIST(state, watchlists) {
      state.watchlists = watchlists
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      state.articles = null
      state.movies = null
      state.watchlists = null
      router.push({name:'home'})
    },
    REMOVE_TOKEN(state) {
      state.token = null
      router.push({name:'home'})
    },
  },
  actions: {
    getMovies(context){
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated?',
        params:{
          api_key: process.env.VUE_APP_API_KEY,
          language: 'ko-KR',
          page:1
        }
      })
      .then((res)=>{
        console.log(res.data.results)
        context.commit('GET_MOVIES',res.data.results)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/articles/`,
        headers: {
          Authorization : `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log(res.data)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },

    getMyWatchList(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/watchlists/`,
        headers: {
          Authorization : `Token ${context.state.token}`
        }
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_WATCHLIST', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },

    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      axios({
        method: 'post',
        // url: `http://127.0.0.1:8000/accounts/signup/`,
        url: `http://localhost:8000/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => console.log(err))
        
    },

    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `http://localhost:8000/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => console.log(err))
    },

    logOut(context) {
      context.commit('REMOVE_TOKEN')
    }

  },
  modules: {
  }
})
