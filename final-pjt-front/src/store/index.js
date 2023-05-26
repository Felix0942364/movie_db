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
    id: null,
    user: null,
    token: null,
    watchlists: null,
    Recomendation:null,
    Recently:null,
    Popular:null,
  },
  getters: {
    isAuthenticated(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    GET_MOVIES(state, payload){
      state.Recomendation = payload['Recomendation']
      state.Recently =  payload['Recently']
      state.Popular =  payload['Popular']
    },
    GET_WATCHLIST(state, watchlists) {
      state.watchlists = watchlists
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      state.articles = null
      state.movies = null
      state.watchlists = null
    },
    SAVE_ID(state, data) {  
      state.user = data
      state.id = data.pk
      router.push({name:'home'})
    },
    REMOVE_TOKEN(state) {
      state.articles = null
      state.movies = null
      state.token = null
      state.id = null 
      router.push({name:'home'})
    },
  },
  actions: {
    getMovies(context){
      const requests = [
        axios.get('https://api.themoviedb.org/3/movie/top_rated', {
          params: {
            api_key: process.env.VUE_APP_TMDB_KEY,
            language: 'ko-KR',
            page: 1
          }
        }),
        axios.get('https://api.themoviedb.org/3/movie/popular', {
          params: {
            api_key: process.env.VUE_APP_TMDB_KEY,
            language: 'ko-KR',
            page: 1
          }
        }),
        axios.get('https://api.themoviedb.org/3/movie/now_playing', {
          params: {
            api_key: process.env.VUE_APP_TMDB_KEY,
            language: 'ko-KR',
            page: 1
          }
        })
      ];
    
      axios
        .all(requests)
        .then(axios.spread((res1, res2, res3) => {
          const payload = {'Recomendation': res1.data.results, 'Recently': res2.data.results, 'Popular': res3.data.results}
          context.commit('GET_MOVIES',payload);
        }))
        .catch((err) => {
          console.log(err);
        });
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
        .then((res1) => {
          context.commit('SAVE_TOKEN', res1.data.key)
          axios({
            method : 'get',
            url : `${API_URL}/accounts/user/`,
            headers : { Authorization : `Token ${context.state.token}` }
          })
            .then((res2) => {
              console.log(res2.data)
              context.commit('SAVE_ID', res2.data)
            })
            .catch(err => console.log(err))

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
        .then((res1) => {
          context.commit('SAVE_TOKEN', res1.data.key)
          axios({
            method : 'get',
            url : `${API_URL}/accounts/user/`,
            headers : { Authorization : `Token ${context.state.token}` }
          })
            .then((res2) => {
              context.commit('SAVE_ID', res2.data.pk)
              axios({
                method : 'get',
                url : `${API_URL}/accounts/user/`,
                headers : { Authorization : `Token ${context.state.token}` }
              })
                .then((res2) => {
                  context.commit('SAVE_ID', res2.data)
                  context.dispatch('getMyWatchList')
                })
                .catch(err => console.log(err))
            })
            .catch(err => console.log(err))

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
