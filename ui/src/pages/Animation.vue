<template>
  <q-page padding class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em" v-if="!LD">
    <q-scroll-observer @scroll="onScroll"/>
    <div class="q-mx-auto" style="width: 95%">
      <div class="row q-col-gutter-x-lg justify-center">
        <!--LEFT-->
        <div class="column col-md-3 col-xs-12 q-pb-md">
          <q-img :src="this.animation.images.vertical.url">
          </q-img>
          <q-btn dense color="primary" class="q-mt-sm">
            REPORT A PROBLEM
            <q-icon class="q-pl-sm" name="construction" size="1.5em"></q-icon>
          </q-btn>
        </div>
        <!--RIGHT-->
        <div class="column col-md-9 col-xs-12 q-pb-md">
          <!--TITLE-->
          <div style="width: 100%" class="q-pa-md bl">
            <div class="col-md-10 col-xs-12"><p class="q-my-none text-white  text-h3">{{ this.animation.name }}</p>
            </div>
          </div>
          <!--INFOS-->
          <div style="width: 100%" class="q-pa-md bl">
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12">
                <q-icon color="primary" name="fas fa-info-circle" size="2.5em"></q-icon>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-primary  text-h4"></p></div>
            </div>
            <q-separator color="grey" style="opacity: 30%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">INTRO</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1 text-justify">
                {{ this.animation.intros.enIntro }}</p></div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">TYPE</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ this.animation.type }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">EPS NUM</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{
                  this.animation.episodesNum
                }}</p></div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">PRODUCED
                BY</p></div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{
                  this.animation.producedBy
                }}</p></div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">WRITTEN
                BY</p></div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{
                  this.animation.writtenBy
                }}</p></div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">RELEASED
                AT</p></div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{
                  this.animation.releasedAt
                }}</p></div>
            </div>
          </div>
          <!--VIDEOS-->
          <div style="width: 100%" class="q-pa-md bl" v-for="(video,i) in animation.videos" :key="'video'+i">
            <div class="row q-py-md ">
              <div class="col-md-2 col-xs-12">
                <q-icon color="primary" name="fas fa-film" size="2.5em"></q-icon>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-white text-h4"></p></div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">TYPE</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ video.fileMeta.type }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">SIZE</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ video.fileMeta.size }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">QUALITY</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">
                {{ video.fileMeta.quality }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">URL</p></div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ video.fileUrl }}</p></div>
            </div>
          </div>
          <!--CPATIONS-->
          <div style="width: 100%" class="q-pa-md bl" v-for="(caption,i) in animation.captions" :key="'caption'+i">
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12">
                <q-icon color="primary" name="fas fa-closed-captioning" size="2.7em"></q-icon>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-white text-h2"></p></div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">TYPE</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ caption.fileMeta.type }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">SIZE</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ caption.fileMeta.size }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">integrated</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ caption.integrated }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">state</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ caption.state }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">releasedAt</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ caption.releasedAt }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">URL</p></div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ caption.fileUrl }}</p></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import {scroll} from 'quasar'

const {getScrollTarget, setScrollPosition} = scroll

export default {
  name: "index.vue",
  data: () => ({
    animation: {},
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
    },
    onScroll(info) {
      this.scrollInfo = info
    }
  },
  mounted() {
    this.$axios.get('api/animation/info/5').then((response) => {
      const rd = response.data
      console.log('return data:')
      console.log(rd)
      if (rd.code === 'success') {
        this.animation = rd.data.animation
        console.log('animation:')
        console.log(this.animation)
      }
      this.LD = false
    }).catch(function (error) {
      console.log(error)
    })
  },
  computed: {}
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

.bl
  border-left: solid
  border-left-color: $primary
  border-width: 3px
</style>
