<template>
  <div class="q-py-xl" style="width: 100%;" >
    <!--Common-->
    <div v-if="!isEditing">
      <div class="row justify-center">
        <q-avatar size="250px"  v-ripple class="cursor-pointer " v-if="user !== null">
          <img contain :src="require('assets/3333.png')">
        </q-avatar>
      </div>
      <div class="row q-pt-md  items-center  text-white text-h5 text-weight-medium">
        二仙桥野猪佩奇
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
        <div ><q-icon size="1.2em" class="q-mr-sm"  name="email"></q-icon> </div>
        <div  class="text-justify">
          amaindex@outlook.com
        </div>
      </div>
      <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
        <div><q-icon size="1.2em" class="q-mr-sm"  name="phone"></q-icon> </div>
        <div class="text-justify">
          17685472365
        </div>
      </div>
      <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
        <div><q-icon size="1.2em" class="q-mr-sm"  name="fas fa-info"></q-icon> </div>
        <div class="text-justify">
          春江潮水连海平，海上明月共潮生。
          滟滟随波千万里，何处春江无月明！
        </div>
      </div>
      <q-separator class="q-mt-sm" color="white"></q-separator>
      <div class="row q-mt-md justify-center">
        <q-btn
          class="full-width text-weight-bold" color="white" text-color="dark"
          @click="isEditing=true"
        >
          EDIT PROFILE
        </q-btn>
      </div>
      <div class="row q-mt-md justify-center">
        <q-btn  class="full-width text-weight-bold" color="white" text-color="dark">
          SIGN OUT
        </q-btn>
      </div>
    </div>
    <!--Editing-->
    <div v-if="isEditing">
      <div class="row justify-center">
        <file-pond
          style="width: 250px"
          name="test"
          ref="pond"
          class="cursor-pointer"
          label-idle="Drop files here..."
          accepted-file-types="image/jpeg, image/png"
          v-bind:files="myFiles"
          v-on:init="handleFilePondInit"
          allowImageCrop="true"
          imagePreviewHeight="170px"
          imageCropAspectRatio="1:1"
          stylePanelLayout="compact circle"
          styleButtonRemoveItemPosition= "center bottom"
        />
      </div>
      <div class="row q-pt-xs  items-center  text-white text-h5 text-weight-medium">
        <q-input
          dense
          dark
          class="bg-dark-light"
          style="width: 100%"
          v-model="text"
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
          v-model="text"
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
          v-model="text"
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
          v-model="text"
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
          v-model="text"
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
          v-model="text"
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
          @click="isEditing=false"
        >
          Cancel
        </q-btn>
        <q-btn  class="full-width text-weight-bold q-mt-sm" color="white" text-color="dark">
          Submit
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
  data () {
    return {
      drawer: false,
      myFiles: [],
      text: 'sdf',
      isEditing: false,
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
    edit(){

    }
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  }
}
</script>

<style scoped>

</style>
