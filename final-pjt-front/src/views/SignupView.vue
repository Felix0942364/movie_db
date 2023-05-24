<template>
  <div class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5" style="min-width:400px;">
          <div class="card bg-dark text-white shadow-lg" style="border-radius: 1rem;">
            <div class="card-body p-5 text-center">

              <div class="mb-md-5 mt-md-4 pb-2">
                <h2 class="fw-bold mb-4 text-uppercase">SIGN UP</h2>
                <!-- <p class="text-white-50 mb-3">Please enter your username and password</p> -->
                <form @submit.prevent="signUp">
                  <div class="form-floating mt-4 mb-4">
                    <input type="text" class="form-control" id="username" placeholder="Username" v-model="username">
                    <label class="text-secondary" for="username" >Username</label>
                  </div>

                  <div class="form-floating mb-4">
                    <input type="password" class="form-control" id="password1" placeholder="Password" v-model="password1">
                    <label class="text-secondary" for="password1">Password</label>
                  </div>

                  <div class="form-floating mb-4">
                    <input type="password" class="form-control" id="password2" placeholder="Password" v-model="password2">
                    <label class="text-secondary" for="password2">Confirm Password</label>
                  </div>
                  <button class="btn btn-outline-light btn-lg px-5 mt-4" type="submit">Sign Up</button>
                </form>
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
  name: 'SignupView',
  data() {
    return {
      username: "",
      password1: "",
      password2: ""
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      
      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style scoped>
.gradient-custom {
  background: linear-gradient(to bottom right,   rgb(255, 174, 120), rgb(0, 0, 0))
}
</style>