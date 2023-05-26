<template>
  <div class="profile_container p-5">

    <div class="profile p-5">
      <img :src="'http://localhost:8000' + user.profile_img" v-if="user?.profile_img"/>
      <img src="@/assets/img/base_profile.png" v-else/>
      <h1 class="pt-3 pb-0"> {{ user?.username }} </h1>
      <p>{{user?.profile_message}} </p>
      
      <div class="d-flex flex-row py-1 px-5 mb-3 justify-content-around">
        <div class="followings d-flex flex-column" data-bs-toggle="modal" data-bs-target="#following">
          <span class="count">{{user?.following_count}}</span>
          <span class="label">Following</span>
        </div>

        <div class="modal fade" id="following" tabindex="-1" aria-labelledby="following" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5 text-secondary" id="following">FOLLOWING</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <FollowItem
                :follows="user?.following"
                />
              </div>
            </div>
          </div>
        </div>
        

        <div class="followers d-flex flex-column" data-bs-toggle="modal" data-bs-target="#followers">
          <span class="count">{{user?.followers_count}}</span>
          <span class="label">Followers</span>
        </div>

        <!-- Modal -->
        <div class="modal fade" id="followers" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5 text-secondary" id="exampleModalLabel">FOLLOWERS</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <FollowItem
                :follows="user?.followers"
                />
              </div>
            </div>
          </div>
        </div>
      </div>


      <button class="bottom-button btn-grad" v-if="owner" data-bs-toggle="modal" data-bs-target="#edit-profile">프로필 수정</button>
      <button class="bottom-button btn-grad" @click='follow' v-else-if="followed">언팔로우</button>
      <button class="bottom-button btn-grad" @click='follow' v-else>팔로우</button>

        <!-- Modal -->
      <div class="modal fade" id="edit-profile" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5 text-secondary" id="exampleModalLabel">{{user?.username}}님의 프로필</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <div>
                <input type="file" class="w-100" value="파일 선택" style="color:black" ref="fileInput" @change="handleFileChange">
              </div>
              <!-- <p class="text-secondary" v-if="loadedProfileImg" > {{ loadedProfileImg.name }} </p> -->
              <div class="form-floating my-3">
                <input type="text" class="form-control" id="profile-msg" placeholder="재생목록 제목" v-model="editProfileMsg">
                <label class="text-secondary" for="profile-msg">상태 메시지</label>
              </div>

            </div>
            <div class="modal-footer">
              <button class="btn btn-primary" data-bs-dismiss="modal" @click.prevent="editProfile">수정하기</button>
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="board">
      <div class="watchlist d-flex flex-column align-items-start container-fluid p-0">
        <h2>{{ user?.username }} 님의 재생목록</h2>
        <div class="d-flex">
          <WatchLists
          :watchlists="user?.watchlists"
          :owner="owner"
          @added-watchlist="getProfile"/>
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
              v-for="article in user?.articles"
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
              v-for="article in user?.liked_articles"
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
      <!-- <h1> {{ user }}</h1> -->
      <footer></footer>
    </div>
  </div>
</template>

<script>
// import UserPreference from '@/components/UserPreference.vue'
import WatchLists from '@/components/WatchLists.vue'
import TableItem from '@/components/TableItem.vue'
import CommentTableItem from '@/components/CommentTableItem.vue'
import FollowItem from '@/components/FollowItem.vue'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  components: {
    FollowItem,
    WatchLists,
    TableItem,
    CommentTableItem,
  },
  data() {
    return {
      newWatchlistTitle:"",
      disclosure:"",
      user:null,
      selectedTab:1,

      owner:false,
      followed:false,

      loadedProfileImg:File,
      editProfileMsg: "",
    }
  },
  computed: {
    myProfile() {
      return this.getProfile()
    },
  },
  created() {
    this.getProfile()
  },
  methods : {
    beforeRouteUpdate(to, from, next) {
      this.getProfile()
      next()
    },
    getProfile() {
      axios({
        method:'get',
        url: `${API_URL}/accounts/profile/${this.$route.params.userID}/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.user = res.data 
          this.editProfileMsg = res.data.profile_message
          this.owner = (this.$store.state.id === this.$route.params.userID)? true: false
          this.followed = (this.user.followers.some((obj) => (obj.id === this.$store.state.id)))
        })
        .catch(err => console.log(err))
    },
    
    follow() {
      axios({
        method: 'post',
        url: `http://localhost:8000/accounts/profile/${this.$route.params.userID}/follow/`,
        headers: {
          Authorization : `Token ${this.$store.state.token}`
        }
      })
        .then(() => this.getProfile())
        .catch(err => console.log(err))
    },
    // addWatchList() {
    //   if (!this.newWatchlistTitle) alert('내용을 입력해주세요.')
    //   else if (!this.disclosure) alert('공개 여부를 설정해 주세요.')
    //   axios({
    //     method : 'post',
    //     url: `${API_URL}/api/watchlists/`,
    //     data: {
    //       title: this.newWatchlistTitle,
    //       scope_of_disclosure: this.disclosure
    //     },
    //     headers: {
    //       Authorization : `Token ${this.$store.state.token}`
    //     }
    //   }) 
    //     .then((res) => {
    //       console.log(res)
    //       this.getMyWatchList()
    //     })
    //     .catch(err => console.log(err))
    //   // this.newWatchlist = ""
    // },

    handleFileChange(event) {
      console.log(event.target.files)
      this.loadedProfileImg = event.target.files[0]
      console.log(this.loadedProfileImg)
    },

    editProfile(){
      let formData = new FormData();

      formData.append('profile_img', this.loadedProfileImg)
      formData.append('profile_message', this.editProfileMsg)
      console.log(formData, this.editProfileMsg)

      axios({
        method: 'post',
        url:`http://127.0.0.1:8000/accounts/profile/${this.$store.state.id}/`,
        data: formData,
        headers: {
          'Content-Type': 'multipart/form-data', 
          'Authorization': `token ${this.$store.state.token}`
        }
      })
      // axios.post(`http://127.0.0.1:8000/accounts/profile/${this.$store.state.id}/`, formData, config)
        .then(res => {
          console.log(res.data)
          this.getProfile()
        })
        .catch(err => console.log(err))
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
  /* background-image: url('@/assets/img/temp_bg_img.jpg'); */
  object-fit: center;
  object-position: center;
  
}

.profile {
  width: 25%;
  min-width: 400px;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
  /* border-radius: 2rem; */
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
  box-shadow: 0 5px 20px #eeeeee8c;
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
  box-shadow: 0 5px 10px #eeeeee8c;
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
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border-bottom: 1px solid #ff7637;
  padding: 10px;
}

</style>