<template>
  <q-layout view="hHh lpr fFf">
    <q-header class="bg-dark" reveal>
      <q-toolbar style="width: 95%" class="q-py-md q-mx-auto">
        <q-icon name="fas fa-atom" size="2.35em" />
        <div class="text-h4 q-ml-sm" v-if="this.$q.screen.gt.sm">EDATRMS</div>
        <q-space/>
        <nav-items></nav-items>
        <q-separator vertical color="grey" inset="true" class="q-mx-sm"></q-separator>
        <q-btn-dropdown dense  flat  no-caps class="text-body1 q-mx-sm" dropdown-icon="translate" no-icon-animation content-class="bg-dark-light">
          <div class="column q-pa-sm">
            <q-btn
              align="left" flat dense no-caps class="text-body1 text-white"
              @click="$i18n.locale='en'"
            >
              English
            </q-btn>
            <q-btn
              align="left" flat dense no-caps class="text-body1 text-white"
              @click="$i18n.locale='cn'"
            >
              简体中文
            </q-btn>
          </div>
        </q-btn-dropdown>
        <q-separator vertical color="grey" inset="true" class="q-mx-sm"></q-separator>
        <q-btn
          round outline class="q-ml-sm"
          size="0.78em"  icon="mdi-badge-account-horizontal-outline"
          v-if="user === null"
          @click="drawer = !drawer"
        />
        <q-avatar size="2.35em"  v-ripple class="cursor-pointer q-ml-sm" v-if="user !== null">
          <img  @click="drawer = !drawer" :src="require('../assets/3333.png')">
        </q-avatar>
      </q-toolbar>
    </q-header>
    <!--UserLoginAndProfile-->
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
      <q-scroll-area class="fit q-px-lg">
        <!--SignIn-->
        <sign-in v-if="user === null"></sign-in>
        <!--Profile-->
        <profile v-if="user !== null"></profile>
      </q-scroll-area>
    </q-drawer>
    <q-page-container>
      <keep-alive include="Index">
        <router-view />
      </keep-alive>
    </q-page-container>
    <div class="bg-dark-deep q-ma-none q-pa-none" style="width: 100%; height: 300px">
    </div>
  </q-layout>
</template>

<script>
import SignIn from "layouts/SignIn";
import Profile from "layouts/Profile";
import NavItems from "layouts/NavItems";
export default {
  name: 'MainLayout',
  components: {
    SignIn,
    Profile,
    NavItems
  },
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
      myFiles: [],
      text: 'sdf'
    }
  },
  methods: {
    foo(){
      this.$store.commit('setUser',null)
    },
    handleFilePondInit: function () {
      console.log('FilePond has initialized');

      // example of instance method call on pond reference
      this.$refs.pond.getFiles();
    },
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  }
}
</script>
