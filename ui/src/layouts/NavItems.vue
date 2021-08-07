<template>
  <div>
    <div v-if="$q.screen.gt.sm" class="row">
      <q-btn
        dense flat  no-caps class="btn-fixed-width text-h6 q-ml-sm"
        @click="$router.push('/')"
      >
        {{$t("ui.navItems.index")}}
      </q-btn>
      <q-btn
        dense flat  no-caps class="btn-fixed-width text-h6 q-ml-sm"
        @click="$router.push('/con')"
      >
        {{$t("ui.navItems.contributors")}}
      </q-btn>
      <q-btn
        dense flat  no-caps class="btn-fixed-width text-h6 q-ml-sm"
        @click="$router.push('/ann')"
      >
        {{$t("ui.navItems.announcements")}}
      </q-btn>

    </div>
    <div v-if="!$q.screen.gt.sm" class="no-border-radius">
      <q-btn-dropdown
          flat dense no-caps class="text-body1 q-ml-sm"
          dropdown-icon="menu" no-icon-animation
          content-class="bg-dark-light"
      >
        <div class="column q-pa-sm">
          <q-btn align="left" flat dense no-caps class="text-body1 text-white">{{$t("ui.navItems.index")}}</q-btn>
          <q-btn align="left" flat dense no-caps class="text-body1 text-white">{{$t("ui.navItems.contributors")}}</q-btn>
          <q-btn align="left" flat dense no-caps class="text-body1 text-white">{{$t("ui.navItems.announcements")}}</q-btn>
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
      this.$q.notify({
        type: 'success',
        message: `New profile was submitted successfully.`
      })
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
