<template>
  <div class="d-flex">
    <div class="container">
      <img @click="openModal = !openModal" src="@/assets/img/add_watchlist.png"/>
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
          Launch demo modal
        </button>

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                ...
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              </div>
            </div>
          </div>
        </div>
      <p> 새로운 재생목록 추가</p>
    </div>

    <WatchlistItems
    v-for="watchlist in watchlists"
    :key="watchlist.id"
    :watchlist="watchlist"
    />
  </div>
</template>

<script>
import WatchlistItems from "@/components/WatchlistItems.vue"

export default {
  name: 'WatchLists',
  data() {
    return {
      openModal:false
    }
  },
  props: {
    watchlists: Object
  },
  components: {
    WatchlistItems
  },
}
</script>

<style scoped>
img {
  width: 200px;
  height: 200px;
}
</style>