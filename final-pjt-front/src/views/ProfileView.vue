<template>
  <div class="profile_container">

    <div class="profile p-5">
      <img :src="imgSrc" v-if="imgSrc"/>
      <img src="@/assets/img/base_profile.png" v-else/>
      <h1 class="pt-3 pb-0"> {{ user.username }} </h1>
      <p v-if="user.profile_message"> {{user.profile_message}} </p>
      
      <div class="d-flex flex-row py-1 px-5 mb-3 justify-content-around">
        <div class="followings d-flex flex-column">
          <span class="count">{{user.following_count}}</span>
          <span class="label">Followings</span>
        </div>
        
        <div class="followers d-flex flex-column">
          <span class="count">{{user.followers_count}}</span>
          <span class="label">Followers</span>
        </div>
      </div>
      
      <button class="bottom-button btn-grad" v-if="user.id === this.$store.state.id">프로필 수정</button>
      <button class="bottom-button btn-grad" v-else>팔로우</button>
      
      <div v-if="user.preferences.length != 0">
        <h1> 취향 </h1>
        <UserPreference
        v-for="preference in user.preferences"
        :key="preference.id"
        :preference="preference"
        />
      </div>
    </div>

    <div class="board">
      <div class="watchlist d-flex flex-column align-items-start">
        <h2>{{ user.username }} 님의 재생목록</h2>
        <div class="d-flex">
          <WatchLists :watchlists="user.watchlists"/>
        </div>
      </div>
      <br>

      <div>
        <ul class="nav nav-tabs text-primary">
          <li class="nav-item" @click="selectedTab=1">
            <p class="nav-link" :class="{active:selectedTab===1}" aria-current="page" >작성한 글들</p>
          </li>
          <li class="nav-item" @click="selectedTab=2">
            <p class="nav-link" :class="{active:selectedTab===2}">좋아한 글들</p>
          </li>
          <li class="nav-item" @click="selectedTab=3">
            <p class="nav-link" :class="{active:selectedTab===3}">작성한 댓글</p>
          </li>
          <li class="nav-item" @click="selectedTab=4">
            <p class="nav-link" :class="{active:selectedTab===4}">좋아한 댓글</p>
          </li>
        </ul>
      </div>

      <div class="container" v-if="selectedTab === 1">
        <table class="table text-white mt-3">
          <thead>
            <tr>
              <th scope="col">게시글 번호</th>
              <th scope="col">제목</th>
              <th scope="col">작성자</th>
              <th scope="col">작성일자</th>
            </tr>
          </thead>
          <tbody>
            <TableItem
              v-for="article in user.articles"
              :key="article.id"
              :item="article"
            />
          </tbody>
        </table>
      </div>
      <div class="container" v-if="selectedTab === 2">
        <table class="table text-white mt-3">
          <thead>
            <tr>
              <th scope="col">게시글 번호</th>
              <th scope="col">제목</th>
              <th scope="col">작성자</th>
              <th scope="col">작성일자</th>
            </tr>
          </thead>
          <tbody>
            <TableItem
              v-for="article in user.liked_articles"
              :key="article.id"
              :item="article"
            />
          </tbody>
        </table>
      </div>
      <div class="container" v-if="selectedTab === 3">
        <table class="table text-white mt-3">
          <thead>
            <tr>
              <th scope="col">게시글</th>
              <th scope="col">작성댓글</th>
              <th scope="col">작성일자</th>
            </tr>
          </thead>
          <tbody>
            <CommentTableItem
              v-for="comment in user.comments"
              :key="comment.id"
              :item="comment"
            />
          </tbody>
        </table>
      </div>
      <div class="container" v-if="selectedTab === 4">
        <table class="table text-white mt-3">
          <thead>
            <tr>
              <th scope="col">게시글</th>
              <th scope="col">댓글</th>
              <th scope="col">좋아한 일자</th>
            </tr>
          </thead>
          <tbody>
            <CommentTableItem
              v-for="comment in user.liked_comments"
              :key="comment.id"
              :item="comment"
            />
          </tbody>
        </table>
      </div>
      <footer></footer>
    </div>
  </div>
</template>

<script>
import UserPreference from '@/components/UserPreference.vue'
import WatchLists from '@/components/WatchLists.vue'
import TableItem from '@/components/TableItem.vue'
import CommentTableItem from '@/components/CommentTableItem.vue'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    UserPreference,
    WatchLists,
    TableItem,
    CommentTableItem,
  },
  data() {
    return {
      newWatchlistTitle:"",
      disclosure:"",
      user:null,
      selectedTab:1
    }
  },
  computed: {
    myWatchList() {
      return this.$store.state.watchlists
    },
    myProfile() {
      return this.getProfile()
    }
  },
  created() {
    this.getProfile()
    this.getMyWatchList()
  },
  methods : {
    getMyWatchList() {
      this.$store.dispatch('getMyWatchList')
    },
    getProfile() {
      axios({
        method:'get',
        url: `${API_URL}/accounts/profile/${this.$store.state.id}/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.user = res.data 
        })
        .catch(err => console.log(err))
    },
    addWatchList() {
      if (!this.newWatchlistTitle) alert('내용을 입력해주세요.')
      else if (!this.disclosure) alert('공개 여부를 설정해 주세요.')
      axios({
        method : 'post',
        url: `${API_URL}/api/watchlists/`,
        data: {
          title: this.newWatchlistTitle,
          scope_of_disclosure: this.disclosure
          },
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      }) 
        .then((res) => {
          console.log(res)
          this.getMyWatchList()
        })
        .catch(err => console.log(err))
      // this.newWatchlist = ""
    }
  },
}
</script>

<style scoped>
/* CSS for the layout */
.nav-tabs .nav-item .nav-link { 
  font-size: large;
  color: #FFF;
}

.nav-tabs .nav-item .nav-link.active {
  color: #121213e8;
  font-weight: bold;
  font-size: larger;
}
/* 
.tab-content {
  border: 1px solid #dee2e6;
  border-top: transparent;
  padding: 15px;
}

.tab-content .tab-pane {
  background-color: #FFF;
  color: #0080FF;
  min-height: 200px;
  height: auto;
} */

.profile_container {
  display: flex;
  justify-content: center;
  background-image: url('@/assets/img/temp_bg_img.jpg');
  object-fit: center;
  object-position: center;
  
}

.profile {
  width: 25%;
  min-width: 400px;
  /* border-top-left-radius: 20px; */
  /* border-bottom-left-radius: 20px; */
  border-radius: 2rem;
}

.board {
  width: 70%;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
  /* overflow: scroll; */
}

/* Additional styling for demonstration purposes */
.profile {
  background: rgba(65, 65, 65, 0.8);
  padding: 20px;
}

.board {
  background: rgba(36, 36, 36, 0.6);
  padding: 20px;
}

.profile > img {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  object-fit: cover;
  object-position: center;
  background-color: white;
}


.followings, .followers {
  text-align: center;
  margin: 0 20px;
}

.count {
  font-size: 24px;
  font-weight: bold;
}

.label {
  font-size: 14px;
  color: gray;
}

.btn-grad {
  background-image: linear-gradient(to right, #ff6600 0%, #F0CB35  51%, #fa620a  100%);
  padding: 5px 10px;
  text-align: center;
  text-transform: uppercase;
  transition: 0.5s;
  background-size: 200% auto;
  color: white;            
  box-shadow: 0 5px 10px #eee;
  border-radius: 10px;
  border: none;
  display: block;
  width:100%;
  opacity: 95%;
}

.btn-grad:hover {
  background-position: right center; /* change the direction of the change here */
  color: #fff;
  text-decoration: none;
}

.watchlist {
  padding: 20px;
  display: flex;
  background: rgba(27, 27, 27, 0.4);
  /* border-radius: 20px; */
}

table {
  color:white;

  border-collapse: collapse;
  width: 100%;
}

th, td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

/* th {
  background-color: #f2f2f2;
} */

tr:nth-child(even) {
  background-color: rgba(249, 249, 249, 0.1);
}
</style>