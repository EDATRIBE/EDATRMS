<template>
  <div class="q-py-xl" style="width: 100%;" >
    <!--Common-->
    <div v-if="!editing.isEditing">
      <div class="row justify-center">
        <q-avatar size="250px"  v-ripple class="cursor-pointer " v-if="user !== null">
          <img contain :src="user.avatar.url">
        </q-avatar>
      </div>
      <div
        class="row q-pt-md  items-center  text-h5 text-weight-medium"
        @click="foo"
        :class="{'text-accent':this.user.staff}"
      >
        {{ user.name }}
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
        <div ><q-icon size="1.2em" class="q-mr-sm"  name="email"></q-icon> </div>
        <div  class="text-justify">
          {{user.email}}
        </div>
      </div>
      <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
        <div><q-icon size="1.2em" class="q-mr-sm"  name="phone"></q-icon> </div>
        <div class="text-justify">
          {{user.mobile}}
        </div>
      </div>
      <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
        <div><q-icon size="1.2em" class="q-mr-sm"  name="fas fa-info"></q-icon> </div>
        <div class="text-justify">
          {{user.intro}}
        </div>
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row q-mt-md justify-center">
        <q-btn
          class="full-width text-weight-bold" color="white" text-color="dark"
          @click="editing.isEditing=true"
        >
          EDIT PROFILE
        </q-btn>
      </div>
      <div class="row q-mt-md justify-center">
        <q-btn
          class="full-width text-weight-bold" color="white" text-color="dark"
          @click="signOut"
        >
          SIGN OUT
        </q-btn>
      </div>
    </div>
    <!--Editing-->
    <div v-if="editing.isEditing">
      <div class="row justify-center">
        <file-pond
          style="width: 250px"
          name="file_pond_file"
          ref="pond"
          class="cursor-pointer"
          label-idle="DROP OR CLICK"
          accepted-file-types="image/jpeg, image/png"
          :files="editing.avatarFile"
          :server="editing.server"
          @init="handleFilePondInit"
          allowImageCrop="true"
          imageCropAspectRatio="1:1"
          stylePanelLayout="compact circle"
          styleButtonRemoveItemPosition="center bottom"
          styleButtonProcessItemPosition="center bottom"
          styleLoadIndicatorPosition="center bottom"
          styleProgressIndicatorPosition="center bottom"
        />
      </div>
      <div class="row q-pt-xs  items-center  text-white text-h5 text-weight-medium">
        <q-input
          dense
          dark
          class="bg-dark-light"
          style="width: 100%"
          v-model="editing.data.name"
          clear-icon="close"
          standout=""
          label="User Name"
        >
          <template v-slot:prepend>
            <q-icon name="fas fa-user"/>
          </template>
        </q-input>
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row q-pt-sm text-white text-justify text-body1">
        <q-input
          dense
          dark
          class="bg-dark-light"
          style="width: 100%"
          v-model="editing.data.password"
          clear-icon="close"
          standout=""
          label="New Password"
        >
          <template v-slot:prepend>
            <q-icon name="fas fa-key"/>
          </template>
        </q-input>
        <q-input
          dense
          dark
          class="bg-dark-light q-mt-sm"
          style="width: 100%"
          v-model="editing.data.confirmPassword"
          clear-icon="close"
          standout=""
          label="Confirm Password"
        >
          <template v-slot:prepend>
            <q-icon name="fas fa-key"/>
          </template>
        </q-input>
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row q-pt-sm text-white text-justify text-body1">
        <q-input
          dense
          dark
          class="bg-dark-light"
          style="width: 100%"
          v-model="editing.data.email"
          clear-icon="close"
          standout=""
          label="Email"
        >
          <template v-slot:prepend>
            <q-icon name="email"/>
          </template>
        </q-input>
        <q-input
          dense
          dark
          class="bg-dark-light q-mt-sm"
          style="width: 100%"
          v-model="editing.data.mobile"
          clear-icon="close"
          standout=""
          label="Phone"
        >
          <template v-slot:prepend>
            <q-icon name="phone"/>
          </template>
        </q-input>
        <q-input
          dense
          dark
          autogrow
          class="bg-dark-light q-mt-sm"
          style="width: 100%"
          v-model="editing.data.intro"
          clear-icon="close"
          standout=""
          color="white"
          label="Intro"
        >
          <template v-slot:prepend>
            <q-icon name="fas fa-info"/>
          </template>
        </q-input>
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row q-mt-sm justify-center">
        <q-btn
          class="full-width text-weight-bold" color="white" text-color="dark"
          @click="editing.isEditing=false"
        >
          Cancel
        </q-btn>
        <q-btn
          class="full-width text-weight-bold q-mt-sm" color="white" text-color="dark"
          @click="commitEditing"
        >
          Commit
        </q-btn>
      </div>
    </div>
  </div>
</template>

<script>
// Import FilePond
import vueFilePond from 'vue-filepond';

// Import styles
import 'filepond/dist/filepond.min.css';
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css'
// Import the plugin code
import FilePondPluginImageCrop from 'filepond-plugin-image-crop';
import FilePondPluginImageExifOrientation from 'filepond-plugin-image-exif-orientation'
import FilePondPluginImagePreview from 'filepond-plugin-image-preview'
import FilePondPluginFileValidateSize from 'filepond-plugin-file-validate-size'
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type'
import SignIn from "layouts/SignIn";

// Create FilePond component
const FilePond = vueFilePond(
  FilePondPluginImageExifOrientation,
  FilePondPluginImageCrop,
  FilePondPluginImagePreview,
  FilePondPluginFileValidateSize,
  FilePondPluginFileValidateType
);

export default {
  name: "Profile",
  components: {
    FilePond,
  },
  mounted() {
    this.editing.data = {
      name: this.user.name,
      password: '',
      confirmPassword: '',
      email: this.user.email,
      mobile: this.user.mobile,
      intro: this.user.intro,
      avatarId: this.user.avatar.id
    }
  },
  data () {
    return {
      editing:{
        isEditing: false,
        avatarFile:[],
        data:{},
        server:{
          url: '/api',
          process: '/storage/file/filepond/upload',
          revert: null,
          restore: null,
          load: '/storage/file/filepond/load/',
          fetch: null
        },
      }
    }
  },
  methods: {
    foo(){
      this.$q.notify({
        type: 'success',
        message: `New profile was submitted successfully.`
      })
      this.$q.notify({
        type: 'failure',
        message: `New profile was submitted successfully.`
      })
    },
    handleFilePondInit: function () {
      console.log('FilePond has initialized');
      // example of instance method call on pond reference
      this.$refs.pond.getFiles();
      this.editing.avatarFile=[{
        source: this.user.avatar.id,
        options: {
          type: 'local'
        }
      }]
      console.log(this.editing.avatarFile)
    },
    commitEditing(){
      const currentAvatarList = this.$refs.pond.getFiles()
      if(currentAvatarList.length === 0){
        delete this.editing.data.avatarId
      }else {
        if(currentAvatarList[0].status === 5 || currentAvatarList[0].status === 2){
          this.editing.data.avatarId = Number(currentAvatarList[0].serverId)
        }
      }
      if(this.editing.data.password !== this.editing.data.confirmPassword){
        console.log('密码不一致')
      }else {
        delete this.editing.data.confirmPassword
        if (this.editing.data.password === ''){
          delete this.editing.data.password
        }
      }
      console.log(this.editing.data)

      this.$axios.post('api/account/edit', this.editing.data).then((response) => {
        let rd = response.data
        if (rd.code === 'success') {
          console.log('rd.data.user')
          console.log(rd.data.user)
          this.$store.commit('setUser',rd.data.user)
          this.$q.notify({
            type: 'success',
            message: `New profile was submitted successfully.`
          })
          this.editing.isEditing=false
        }else {
          console.log(response)
        }
      }).catch((error) => {
        console.log(error)
      })

    },
    signOut(){
      this.$axios.get('api/account/logout').then((response) => {
        const rd = response.data
        console.log('return data:')
        console.log(rd)
        if (rd.code === 'success') {
          this.$store.commit('setUser',null)
          console.log('user:')
          console.log(this.user)
        }
        this.$q.notify({
          type: 'success',
          message: `Sign out successfully.`
        })
      }).catch(function (error) {
        console.log(error)
      })
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  }
}
</script>

<!--<style >-->
<!--.filepond&#45;&#45;drop-label {-->
<!--  color: white;-->
<!--}-->

<!--.filepond&#45;&#45;panel-root {-->
<!--  background-color: #373C41;-->
<!--}-->
<!--</style>-->
