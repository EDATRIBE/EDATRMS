<template>
  <q-page class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em" v-if="!LD">
    <q-scroll-observer @scroll="onScroll" />
    <div class="q-mx-auto" style="width: 95%">
      <div class="column">
        <!--SEARCH-->
        <q-input
          dense dark class="text-h5 bg-dark-light q-mb-md" style="width: 100%" standout=""
          v-model="searchBuffer"
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
          outside-arrows
        >
          <q-route-tab
            ripple class="text-primary text-weight-medium" name="Animations" style="width: 50%"
            to="/index/animations"
          >
            <q-icon class="q-mr-xs" size="1.7em" name="movie"></q-icon>{{$t('ui.index.animations')}}
          </q-route-tab>
          <q-route-tab
            ripple class="text-secondary text-weight-medium" name="Novels"  style="width: 50%"
            to="/index/novels"
          >
            <q-icon class="q-mr-xs" size="1.7em" name="import_contacts"></q-icon>{{$t('ui.index.novels')}}
          </q-route-tab>
          <q-route-tab
            ripple class="text-accent text-weight-medium" name="IPsAndTags"  style="width: 50%"
            v-if="currentUser&&currentUser.staff"
            to="/index/ips_and_tags"
          >
            <q-icon class="q-mr-xs" size="1.7em" name="source"></q-icon>{{$t('ui.index.ips')}}
            <span class="q-mx-sm">|</span>
            <q-icon class="q-mr-xs" size="1.2em" name="fas fa-hashtag"></q-icon>{{$t('ui.index.tags')}}
          </q-route-tab>
        </q-tabs>
        <keep-alive>
          <router-view />
        </keep-alive>
<!--        <q-tab-panels keep-alive v-model="tab" class="bg-dark">-->
<!--          <q-tab-panel name="Animations" class="q-px-none bg-dark ">-->
<!--            <IndexAnimations></IndexAnimations>-->
<!--          </q-tab-panel>-->
<!--          <q-tab-panel name="Novels" class="q-px-none bg-dark ">-->
<!--            <IndexNovels></IndexNovels>-->
<!--          </q-tab-panel>-->
<!--          <q-tab-panel name="IPsAndTags" class="q-px-none bg-dark " v-if="currentUser&&currentUser.staff">-->
<!--            <index-i-ps></index-i-ps>-->
<!--            <index-tags></index-tags>-->
<!--          </q-tab-panel>-->
<!--        </q-tab-panels>-->
      </div>
    </div>

    <q-page-sticky expand position="top" class="bg-dark q-px-md q-py-sm" v-show="scrollInfo.position>38">
      <q-toolbar style="width: 95.2%" class="q-px-none">
        <q-input
          dense dark class="text-h5 bg-dark-light" style="width: 100%" standout=""
          v-model="searchBuffer"
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
import IndexTags from "src/layout_pages/Index/IndexTags";

export default {
  name: "Index",
  components: {
    // IndexTags,
    // IndexIPs,
    // IndexNovels,
    // IndexAnimations
  },
  activated() {
    if(this.$route.query.tab){
      this.tab=this.$route.query.tab
    }
    if(this.$route.query.search){
      this.searchBuffer=this.$route.query.search
    }
  },
  data: () => ({
    LD: true,
    scrollInfo: {},
    searchBuffer: '',
    tab: 'Animations',
    ips: [],
  }),
  methods: {
    foo() {
    },
    onScroll (info) {
      this.scrollInfo = info
    }
  },
  created() {
    this.LD = false
  },
  computed: {
    // animations() {
    //   let animations = []
    //   for (let i = 0; i < this.ips.length; i++) {
    //     for (let j = 0; j < this.ips[i].animations.length; j++) {
    //       animations.push(this.ips[i].animations[j])
    //     }
    //   }
    //   return animations
    // },
    // novels() {
    //   let novels = []
    //   for (let i = 0; i < this.ips.length; i++) {
    //     for (let j = 0; j < this.ips[i].novels.length; j++) {
    //       novels.push(this.ips[i].novels[j])
    //     }
    //   }
    //   return novels
    // },
    currentUser() {
      return this.$store.state.account.user
    },
    currentIPS() {
      return this.$store.state.ip.ips
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
