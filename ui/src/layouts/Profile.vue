<template>
  <div class="q-py-xl" style="width: 100%;" >
    <!--Common-->
    <div v-if="!userEditBuffer.isEditing">
      <div class="row justify-center">
        <q-avatar size="250px"  class="cursor-pointer " v-if="currentUser !== null">
          <img contain :src="currentUser.avatar?currentUser.avatar.url:this.genAvatar(currentUser.name)" >
        </q-avatar>
      </div>
      <div
        class="row q-pt-md  items-center  text-h5 text-weight-medium"
      >
        {{ currentUser.name }}
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
        <div ><q-icon size="1.2em" class="q-mr-sm"  name="email"></q-icon> </div>
        <div  class="text-justify">
          {{currentUser.email}}
        </div>
      </div>
      <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
        <div><q-icon size="1.1em" class="q-mr-sm"  name="fab fa-qq"></q-icon> </div>
        <div class="text-justify">
          {{currentUser.qq}}
        </div>
      </div>
      <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
        <div><q-icon size="1.1em" class="q-mr-sm"  name="fas fa-info"></q-icon> </div>
        <div class="text-justify">
          {{currentUser.intro}}
        </div>
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row q-mt-md justify-center">
        <q-btn
          class="full-width text-weight-bold" color="white" text-color="dark"
          @click="userEditBuffer.isEditing=true;readonly=true"
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
    <div v-if="userEditBuffer.isEditing">
      <div class="row justify-center">
        <file-pond
          style="width: 250px"
          name="file_pond_file"
          ref="pond"
          class="cursor-pointer"
          label-idle="DROP OR CLICK"
          accepted-file-types="image/jpeg, image/png"
          :files="userEditBuffer.avatarFile"
          :server="userEditBuffer.server"
          @init="handleFilePondInit"
          allowImageCrop="true"
          imageCropAspectRatio="1:1"
          stylePanelLayout="compact circle"
        />
      </div>
      <div class="row q-pt-xs  items-center  text-white text-h5 text-weight-medium">
        <q-field
          dense
          dark
          class="bg-dark-light"
          style="width: 100%"
          :value="userEditBuffer.data.name"
          clear-icon="close"
          standout=""
          label="Name"
          readonly
        >
          <template v-slot:control>
            <div class="self-center full-width no-outline" tabindex="0">{{userEditBuffer.data.name}}</div>
          </template>
          <template v-slot:prepend>
            <q-icon size="0.8em" name="fas fa-user"/>
          </template>
        </q-field>
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row q-pt-sm text-white text-justify text-body1">
        <q-input
          dense
          dark
          class="bg-dark-light"
          style="width: 100%"
          v-model="userEditBuffer.data.password"
          clear-icon="close"
          standout=""
          label="New Password"
        >
          <template v-slot:prepend>
            <q-icon size="0.8em" name="fas fa-key"/>
          </template>
        </q-input>
        <q-input
          dense
          dark
          class="bg-dark-light q-mt-sm"
          style="width: 100%"
          v-model="userEditBuffer.data.confirmPassword"
          clear-icon="close"
          standout=""
          label="Confirm Password"
        >
          <template v-slot:prepend>
            <q-icon size="0.8em" name="fas fa-key"/>
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
          v-model="userEditBuffer.data.email"
          clear-icon="close"
          standout=""
          label="Email"
        >
          <template v-slot:prepend>
            <q-icon size="0.8em" name="fas fa-envelope"/>
          </template>
        </q-input>
        <q-input
          dense
          dark
          class="bg-dark-light q-mt-sm"
          style="width: 100%"
          v-model="userEditBuffer.data.qq"
          clear-icon="close"
          standout=""
          label="QQ"
        >
          <template v-slot:prepend>
            <q-icon size="0.8em" name="fab fa-qq"/>
          </template>
        </q-input>
        <q-input
          dense
          dark
          autogrow
          class="bg-dark-light q-mt-sm"
          style="width: 100%"
          v-model="userEditBuffer.data.intro"
          clear-icon="close"
          standout=""
          label="Intro"
        >
          <template v-slot:prepend>
            <q-icon size="0.8em" name="fas fa-info"/>
          </template>
        </q-input>
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row q-mt-sm justify-center">
        <q-btn
          class="full-width text-weight-bold" color="white" text-color="dark"
          @click="userEditBuffer.isEditing=false"
        >
          Cancel
        </q-btn>
        <q-btn
          class="full-width text-weight-bold q-mt-sm" color="white" text-color="dark"
          @click="commitEdit"
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
    this.initUserEditBufferData()
  },
  data () {
    return {
      userEditBuffer:{
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
      // this.$refs.pond.getFiles();
      if (this.currentUser.avatar){
        this.userEditBuffer.avatarFile=[{
          source: this.currentUser.avatar?this.currentUser.avatar.id:null,
          options: {
            type: 'local'
          }
        }]
      }
      // console.log(this.userEditBuffer.avatarFile)
    },
    initUserEditBufferData(){
      this.userEditBuffer.data = {
        name: this.currentUser.name,
        password: '',
        confirmPassword: '',
        email: this.currentUser.email,
        qq: this.currentUser.qq,
        intro: this.currentUser.intro,
        avatarId: this.currentUser.avatar?this.currentUser.avatar.id:null
      }
    },
    commitEdit(){
      const currentAvatarList = this.$refs.pond.getFiles()
      if(currentAvatarList.length === 0){
        delete this.userEditBuffer.data.avatarId
      }else {
        if(currentAvatarList[0].status === 5 || currentAvatarList[0].status === 2){
          this.userEditBuffer.data.avatarId = Number(currentAvatarList[0].serverId)
        }
      }
      if(this.userEditBuffer.data.password !== this.userEditBuffer.data.confirmPassword){
        console.log('密码不一致')
      }else {
        delete this.userEditBuffer.data.confirmPassword
        if (this.userEditBuffer.data.password === ''){
          delete this.userEditBuffer.data.password
        }
      }
      console.log(this.userEditBuffer.data)

      delete this.userEditBuffer.data.name

      this.$axios.post('api/account/edit', this.userEditBuffer.data).then((response) => {
        let rd = response.data
        if (rd.code === 'success') {
          console.log('rd.data.user')
          console.log(rd.data.user)
          this.$store.commit('setUser',rd.data.user)
          this.$q.notify({
            type: 'success',
            message: `New profile was submitted successfully.`
          })
          this.initUserEditBufferData()
          this.userEditBuffer.isEditing=false
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
          console.log(this.currentUser)
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
    currentUser() {
      return this.$store.state.account.user
    }
  }
}
</script>
