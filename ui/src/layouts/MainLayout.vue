<template>
  <q-layout view="hHh lpr fFf">
    <q-header class="bg-dark" reveal>
      <q-toolbar style="width: 95%" class="q-py-md q-mx-auto">
        <q-icon name="fas fa-atom" size="2.5rem" />
        <div class="text-h4 q-mx-sm">EDAT-RMS</div>
        <q-space/>
        <div class="text-h5 q-mx-sm">Staffs</div>
        <div class="text-h5 q-mx-sm">About</div>
        <q-separator vertical color="grey" inset class="q-mx-sm"></q-separator>
        <q-icon class="q-ml-sm" name="mdi-badge-account-horizontal-outline" size="2em"/>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
    <div class="bg-dark-deep q-ma-none q-pa-none" style="width: 100%; height: 300px">

    </div>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

const linksData = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Discord Chat Channel',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Forum',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev'
  },
  {
    title: 'Twitter',
    caption: '@quasarframework',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev'
  },
  {
    title: 'Facebook',
    caption: '@QuasarFramework',
    icon: 'public',
    link: 'https://facebook.quasar.dev'
  },
  {
    title: 'Quasar Awesome',
    caption: 'Community Quasar projects',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev'
  }
];

export default {
  name: 'MainLayout',
  components: {},
  data () {
    return {
      text: '',
      leftDrawerOpen: false,
      essentialLinks: linksData
    }
  }
}
</script>

<!--<style lang="sass">-->
<!--.q-field-->
<!--  &&#45;&#45;dense-->
<!--    .q-field__control, .q-field__marginal-->
<!--    height: 5px !important-->
<!--</style>-->
