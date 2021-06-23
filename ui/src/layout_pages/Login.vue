<template>
  <q-page class="  q-px-md bg-dark q-pb-xl" style="padding-top: 3.5em">
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
<!--    <div style="width: 350px; height: 100vh" class="q-mx-auto bg-dark">-->
<!--      <q-scroll-area class="fit q-pt-md">-->
<!--        <div v-if="user !== null" class="q-pa-lg" style="width: 100%;">-->
<!--          <div class="row justify-center">-->
<!--            <q-avatar size="250px" v-ripple class="cursor-pointer " v-if="user !== null">-->
<!--              <img contain :src="require('../assets/3333.png')">-->
<!--            </q-avatar>-->
<!--          </div>-->
<!--          <div class="row q-py-md  items-center  text-white text-h5 text-weight-medium">-->
<!--            二仙桥野猪佩奇-->
<!--          </div>-->
<!--          <q-separator color="white"></q-separator>-->
<!--          <div class="row q-pt-sm text-white text-justify text-body1">-->
<!--            <div style="width: 10%">-->
<!--              <q-icon size="1.2em" class="q-mr-sm" name="email"></q-icon>-->
<!--            </div>-->
<!--            <div style="width: 90%" class="text-justify">-->
<!--              amaindex@outlook.com-->
<!--            </div>-->
<!--          </div>-->
<!--          <div class="row q-pt-sm text-white text-justify text-body1">-->
<!--            <div style="width: 10%">-->
<!--              <q-icon size="1.2em" class="q-mr-sm" name="phone"></q-icon>-->
<!--            </div>-->
<!--            <div style="width: 90%" class="text-justify">-->
<!--              17685472365-->
<!--            </div>-->
<!--          </div>-->
<!--          <div class="row q-pt-sm text-white text-justify text-body1">-->
<!--            <div style="width: 10%">-->
<!--              <q-icon size="1em" class="q-mr-sm" name="fas fa-info"></q-icon>-->
<!--            </div>-->
<!--            <div style="width: 90%" class="text-justify">-->
<!--              春江潮水连海平，海上明月共潮生。-->
<!--              滟滟随波千万里，何处春江无月明！-->
<!--            </div>-->
<!--          </div>-->
<!--          <q-separator class="q-mt-sm" color="white"></q-separator>-->
<!--          <div class="row q-mt-md justify-center">-->
<!--            <q-btn outline class="full-width text-weight-bold" color="white" text-color="white">-->
<!--              EDIT PROFILE-->
<!--            </q-btn>-->
<!--          </div>-->
<!--          <div class="row q-mt-md justify-center">-->
<!--            <q-btn outline class="full-width text-weight-bold" color="white" text-color="white">-->
<!--              SIGN OUT-->
<!--            </q-btn>-->
<!--          </div>-->
<!--        </div>-->

<!--      </q-scroll-area>-->
<!--    </div>-->
  </q-page>
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

// Create FilePond component
const FilePond = vueFilePond(
  FilePondPluginImageExifOrientation,
  FilePondPluginImageCrop,
  FilePondPluginImagePreview,
  FilePondPluginFileValidateSize,
  FilePondPluginFileValidateType
);

export default {
  name: "Login.vue",
  data: function () {
    return { myFiles: [] };
  },
  methods: {
    handleFilePondInit: function () {
      console.log('FilePond has initialized');

      // example of instance method call on pond reference
      this.$refs.pond.getFiles();
    },
  },
  components: {
    FilePond,
  },
}

</script>

<style lang="scss">
.filepond--panel-root {
  background-color: wheat;
  border: solid #1E242A;
}
</style>

