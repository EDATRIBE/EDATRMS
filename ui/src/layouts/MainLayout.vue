<template>
  <q-layout view="hHh lpr fFf">
    <q-header class="bg-dark" reveal>
      <q-toolbar style="width: 95%" class="q-py-sm q-mx-auto">
        <q-icon name="fas fa-atom" size="2.5rem" />
        <div class="text-h4 q-mr-sm">EDAT-RMS</div>
        <q-space/>
        <q-btn flat dense no-caps class="text-body1 q-mx-sm">Contributors</q-btn>
        <q-btn flat dense no-caps class="text-body1 q-mx-sm" @click="foo">About</q-btn>
        <q-separator vertical color="grey"  inset="true" class="q-mx-sm"></q-separator>
<!--        <q-icon class="q-ml-sm" name="mdi-badge-account-horizontal-outline" size="2em"/>-->
        <q-btn
          round outline class="q-ml-sm"
          size="0.8em"  icon="mdi-badge-account-horizontal-outline"
          v-if="user === null"
          @click="drawer = !drawer"
        />
        <q-avatar size="2.35em"  v-ripple class="cursor-pointer q-ml-sm" v-if="user !== null">
          <img  @click="drawer = !drawer" :src="require('../assets/3333.png')">
        </q-avatar>
      </q-toolbar>
    </q-header>
    <q-drawer
      side="right"
      v-model="drawer"
      :width="350"
      dark
      overlay
      content-class="bg-dark"
      bordered
      class="q-pa-none"
      :breakpoint="10000"
    >
      <q-scroll-area class="fit q-pt-md">
        <div v-if="user === null" class="q-pa-lg" style="width: 100%;" >
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
              class="text-h5 bg-dark q-mb-sm"
              v-model="text"
              clear-icon="close"
              outlined
              color="white"
            >
              <template v-slot:prepend>
                <q-btn dense round color="white" flat icon="fas fa-user"/>
              </template>
            </q-input>
            <q-input
              dark
              dense
              class="text-h5 bg-dark q-mb-sm"
              v-model="text"
              clear-icon="close"
              color="white"
              outlined
            >
              <template v-slot:prepend>
                <q-btn dense round color="white" flat icon="fas fa-key"/>
              </template>
            </q-input>
          </div>
          <div class="row justify-center ">
            <q-btn outline class="full-width text-weight-bold" color="white" text-color="white">
              SIGN IN
            </q-btn>
          </div>
        </div>
        <div v-if="user !== null" class="q-pa-lg" style="width: 100%;" >
          <div class="row justify-center">
            <q-avatar size="250px"  v-ripple class="cursor-pointer " v-if="user !== null">
              <img contain :src="require('../assets/3333.png')">
            </q-avatar>
          </div>
          <div class="row q-py-md  items-center  text-white text-h5 text-weight-medium">
            二仙桥野猪佩奇
          </div>
          <q-separator color="white"></q-separator>
          <div class="row q-pt-sm text-white text-justify text-body1">
            <div style="width: 10%"><q-icon size="1.2em" class="q-mr-sm"  name="email"></q-icon> </div>
            <div style="width: 90%" class="text-justify">
              amaindex@outlook.com
            </div>
          </div>
          <div class="row q-pt-sm text-white text-justify text-body1">
            <div style="width: 10%"><q-icon size="1.2em" class="q-mr-sm"  name="phone"></q-icon> </div>
            <div style="width: 90%" class="text-justify">
              17685472365
            </div>
          </div>
          <div class="row q-pt-sm text-white text-justify text-body1">
            <div style="width: 10%"><q-icon size="1em" class="q-mr-sm"  name="fas fa-info"></q-icon> </div>
            <div style="width: 90%" class="text-justify">
              春江潮水连海平，海上明月共潮生。
              滟滟随波千万里，何处春江无月明！
            </div>
          </div>
          <q-separator class="q-mt-sm" color="white"></q-separator>
          <div class="row q-mt-md justify-center">
            <q-btn outline class="full-width text-weight-bold" color="white" text-color="white">
              EDIT PROFILE
            </q-btn>
          </div>
          <div class="row q-mt-md justify-center">
            <q-btn outline class="full-width text-weight-bold" color="white" text-color="white">
              SIGN OUT
            </q-btn>
          </div>
        </div>
      </q-scroll-area>
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
    <div class="bg-dark-deep q-ma-none q-pa-none" style="width: 100%; height: 300px">

    </div>
  </q-layout>
</template>

<script>
const menuList = [
  {
    icon: 'inbox',
    label: 'Inbox',
    separator: true
  },
  {
    icon: 'send',
    label: 'Outbox',
    separator: false
  },
  {
    icon: 'delete',
    label: 'Trash',
    separator: false
  },
  {
    icon: 'error',
    label: 'Spam',
    separator: true
  },
  {
    icon: 'settings',
    label: 'Settings',
    separator: false
  },
  {
    icon: 'feedback',
    label: 'Send Feedback',
    separator: false
  },
  {
    icon: 'help',
    iconColor: 'primary',
    label: 'Help',
    separator: false
  }
]
export default {
  name: 'MainLayout',
  components: {},
  created() {
    this.$axios.get('api/account/info').then((response) => {
      const rd = response.data
      console.log('return data:')
      console.log(rd)
      if (rd.code === 'success') {
        this.$store.commit('setUser',rd.data.user)
        console.log('user:')
        console.log(this.user)
      }
      this.LD = false
    }).catch(function (error) {
      console.log(error)
    })
  },
  data () {
    return {
      drawer: false,
      menuList
    }
  },
  methods: {
    foo(){
      this.$store.commit('setUser',null)
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  }
}
</script>
