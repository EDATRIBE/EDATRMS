<template>
  <div class="q-py-xl" style="width: 100%;">
    <div class="row justify-center">
      <q-icon name="fas fa-users-cog" size="8em" color="white"></q-icon>
    </div>
    <div class="row justify-center text-white text-h3 text-weight-medium">
      STAFFS
    </div>
    <div class="row justify-center text-white text-h3 text-weight-medium">
      ENTRANCE
    </div>
    <div class="row justify-center q-mt-sm">
      <q-input
        dark
        dense
        class="text-h5 bg-dark-light q-mb-sm"
        v-model="text"
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
        v-model="text"
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
      <q-btn class="full-width text-weight-bold" color="white" text-color="dark">
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
      myFiles: [],
      text: 'textoo'
    }
  }
}
</script>

<style scoped>

</style>
