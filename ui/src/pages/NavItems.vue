<template>
  <div>
    <div v-if="this.$q.screen.gt.sm" class="row">
      <q-btn dense flat  no-caps class="btn-fixed-width text-h6 q-mr-sm">{{$t("ui.navItems.index")}}</q-btn>
      <q-btn dense flat  no-caps class="btn-fixed-width text-h6 q-mr-sm">{{$t("ui.navItems.contributors")}}</q-btn>
      <q-btn dense flat  no-caps class="btn-fixed-width text-h6 q-mr-sm" @click="foo">{{$t("ui.navItems.about")}}</q-btn>
    </div>
    <div v-if="!this.$q.screen.gt.sm" class="bg-dark no-border-radius">
      <q-btn-dropdown   flat dense no-caps class="text-body1 q-mx-sm" dropdown-icon="menu" no-icon-animation content-class="bg-dark-light">
        <div class="column q-pa-sm">
          <q-btn align="left" flat dense no-caps class="text-body1 text-white">Index</q-btn>
          <q-btn align="left" flat dense no-caps class="text-body1 text-white">Contributors</q-btn>
          <q-btn align="left" flat dense no-caps class="text-body1 text-white" @click="foo">About</q-btn>
        </div>
      </q-btn-dropdown>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavItems",
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
}
</script>

<style scoped>

</style>
