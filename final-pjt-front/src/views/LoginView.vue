<template>
  <div class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5" style="min-width:400px;">
          <div class="card bg-dark text-white shadow-lg" style="border-radius: 1rem;">
            <div class="card-body p-5 text-center">

              <div class="mb-md-5 mt-md-4 pb-5">
                <h2 class="fw-bold mb-2 text-uppercase">LOG IN</h2>
                <p class="text-white-50 mb-3">Please enter your username and password</p>
                <form @submit.prevent="logIn">
                  <div class="form-floating mb-3">
                    <input type="text" class="form-control" id="username" placeholder="Username" v-model="username">
                    <label class="text-secondary" for="username" >Username</label>
                  </div>

                  <div class="form-floating">
                    <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
                    <label class="text-secondary" for="password">Password</label>
                  </div>
                  <button class="btn btn-outline-light btn-lg px-5 mt-4" type="submit">Login</button>
                </form>
              </div>
              
              <div>
                <p class="mb-0">Don't have an account? <router-link to="/signup" class="text-white-50 fw-bold">Sign Up</router-link>
                </p>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: "",
      password: "",
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      const payload = {
        username, password
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>

<style scoped>
.gradient-custom {
  background: linear-gradient(to bottom right,   rgb(255, 174, 120), rgb(0, 0, 0))
}
</style>