<template>
  <q-layout view="hHh lpr fFf">
    <q-header class="bg-dark">
      <q-toolbar class="q-px-lg q-py-sm">
        <q-icon name="fas fa-atom" size="2.5rem" />
        <h class="text-h4 q-mx-sm">EDATRMS</h>
        <q-input
          class="q-mx-sm"
          rounded dense dark outlined
          v-model="text" color="white"
          clearable
          clear-icon="close"
        >
          <template v-slot:prepend>
            <q-icon name="mdi-magnify" color="white"/>
          </template>
        </q-input>
        <q-space/>
        <h class="text-h5 q-mx-sm">Staffs</h>
        <h class="text-h5 q-mx-sm">About</h>
        <q-separator vertical color="grey" inset class="q-mx-sm"></q-separator>
        <q-icon class="q-ml-sm" name="mdi-badge-account-horizontal-outline" size="2em"/>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
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
