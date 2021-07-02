<template>
  <q-page class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em" v-if="!LD">
    <q-scroll-observer @scroll="onScroll" />
    <div class="q-mx-auto" style="width: 95%">
      <div class="column">
        <!--SEARCH-->
        <q-input
          dense dark class="text-h5 bg-dark-light q-mb-md" style="width: 100%" standout=""
          v-model="text"
        >
          <template v-slot:append>
            <q-btn dense round color="gery" flat icon="mdi-magnify"/>
          </template>
        </q-input>
        <!--TABS-->
        <q-tabs
          style="width: 100%"
          v-model="tab"
          class="text-grey"
          align="justify"
          inline-label
          dense
        >
          <q-tab ripple class="text-primary" name="Animations" :label="$t('ui.index.animations')" icon="movie" style="width: 50%"/>
          <q-tab ripple class="text-secondary" name="Novels" :label="$t('ui.index.novels')" icon="import_contacts" style="width: 50%"/>
          <q-tab ripple class="text-accent" name="IPs" :label="$t('ui.index.ips')" icon="source" style="width: 50%" v-if="user&&user.staff"/>
        </q-tabs>
        <q-tab-panels keep-alive v-model="tab" class="bg-dark">
          <q-tab-panel name="Animations" class="q-px-none bg-dark q-pt-xs">
            <IndexAnimations></IndexAnimations>
          </q-tab-panel>
          <q-tab-panel name="Novels" class="q-px-none bg-dark q-pt-xs">
            <IndexNovels></IndexNovels>
          </q-tab-panel>
          <q-tab-panel name="IPs" class="q-px-none bg-dark q-pt-xs" v-if="user&&user.staff">
            <index-i-ps></index-i-ps>
          </q-tab-panel>
        </q-tab-panels>
      </div>
    </div>

    <q-page-sticky expand position="top" class="bg-dark q-px-md q-py-sm" v-show="scrollInfo.position>150">
      <q-toolbar style="width: 95.2%" class="q-px-none">
        <q-input
          dense dark class="text-h5 bg-dark-light" style="width: 100%" standout=""
          v-model="text"
        >
          <template v-slot:append>
            <q-btn dense round color="gery" flat icon="mdi-magnify"/>
          </template>
        </q-input>
      </q-toolbar>
    </q-page-sticky>
  </q-page>
</template>

<script>
import IndexAnimations from "src/layout_pages/Index/IndexAnimations";
import IndexNovels from "src/layout_pages/Index/IndexNovels";
import IndexIPs from "src/layout_pages/Index/IndexIPs";

export default {
  name: "Index",
  components: {
    IndexIPs,
    IndexNovels,
    IndexAnimations
  },
  data: () => ({
    tab: 'Animations',
    text: '',
    LD: true,
    expanded: [],
    scrollInfo: {},
    ips: [],
    lorem: 'Kazuto "Kirito" Kirigaya enters a virtual-reality, massively multiplayer online role playing game called Sword Art Online. There is no escape from this world unless the player clears the game; however getting a "game over" results in the death of the player.'
  }),
  methods: {
    foo() {
      console.log('this.animations')
      console.log(this.animations)
      console.log('this.novels')
      console.log(this.novels)
    },
    onScroll (info) {
      this.scrollInfo = info
    }
  },
  mounted() {
    this.$axios.get('api/ip/list').then((response) => {
      const rd = response.data
      console.log('return data:')
      console.log(rd)
      if (rd.code === 'success') {
        this.ips = rd.data.ips
        console.log('ips:')
        console.log(this.ips)
      }
      this.LD = false
    }).catch(function (error) {
      console.log(error)
    })
  },
  computed: {
    animations() {
      let animations = []
      for (let i = 0; i < this.ips.length; i++) {
        for (let j = 0; j < this.ips[i].animations.length; j++) {
          animations.push(this.ips[i].animations[j])
        }
      }
      return animations
    },
    novels() {
      let novels = []
      for (let i = 0; i < this.ips.length; i++) {
        for (let j = 0; j < this.ips[i].novels.length; j++) {
          novels.push(this.ips[i].novels[j])
        }
      }
      return novels
    },
    user() {
      return this.$store.state.user
    }
  }
}
</script>

<style lang="sass" scoped>
.ip-card
  width: 100%
  margin-top: 10px

a
  text-decoration: none

.ov
  overflow: hidden
  -webkit-line-clamp: 2
  text-overflow: ellipsis
  display: -webkit-box
  -webkit-box-orient: vertical
</style>
