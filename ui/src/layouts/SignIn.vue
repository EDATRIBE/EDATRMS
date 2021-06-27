<template>
  <div class="q-py-xl" style="width: 100%; padding-top: 7.5em">
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
        class="text-h5 bg-dark-light q-mb-sm"
        v-model="signInData.name"
        clear-icon="close"
        standout=""
        color="white"
      >
        <template v-slot:prepend>
          <q-icon name="fas fa-user"/>
        </template>
      </q-input>
      <q-input
        dark
        dense
        class="text-h5 bg-dark-light q-mb-sm"
        v-model="signInData.password"
        clear-icon="close"
        color="white"
        standout=""
      >
        <template v-slot:prepend>
          <q-icon name="fas fa-key"/>
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
        name: '',
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
