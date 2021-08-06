<template>
  <div class="q-py-xl" style="width: 100%; padding-top: 8em">
    <div class="row justify-center">
      <q-icon name="fas fa-users-cog" size="8em" color="white"></q-icon>
    </div>
    <div class="row justify-center text-white text-h3 text-weight-medium">
      ACCESS
    </div>
    <div class="row justify-center text-white text-h3 text-weight-medium">
      VALIDATION
    </div>
    <div class="row justify-center q-mt-sm">
      <q-input
        dark
        dense
        class=" bg-dark-light q-mb-sm full-width"
        v-model="signInData.email"
        standout=""
        label="Email address"
      >
        <template v-slot:prepend>
          <q-icon size="0.8em" name="fas fa-envelope"/>
        </template>
      </q-input>
      <q-input
        dark
        dense
        class=" bg-dark-light q-mb-sm full-width"
        v-model="signInData.password"
        standout=""
        label="Password"
        type="password"
      >
        <template v-slot:prepend>
          <q-icon size="0.8em" name="fas fa-key"/>
        </template>
      </q-input>
    </div>
    <div class="row justify-center ">
      <q-btn
        class="full-width text-weight-bold" color="white" text-color="dark"
        @click="signIn"
      >
        SIGN IN
      </q-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignIn",
  data() {
    return {
      drawer: false,
      signInData: {
        email: '',
        password: ''
      }
    }
  },
  methods: {
    signIn(){
      this.$axios.post('api/account/login', this.signInData).then((response) => {
        let rd = response.data
        if (rd.code === 'success') {
          console.log('rd.data.user')
          console.log(rd.data.user)
          this.$store.commit('setUser',rd.data.user)
        }else {
          console.log(response)
        }
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
