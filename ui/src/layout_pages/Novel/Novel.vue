<template>
  <q-page padding class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em" v-if="!LD">
    <q-scroll-observer @scroll="onScroll"/>
    <div class="q-mx-auto" style="width: 97%">
      <div class="row q-col-gutter-x-lg justify-center">
        <!--LEFT-->
        <div class="column col-md-3 col-xs-12 q-pb-md">
          <q-img :src="novel.images.vertical.url">
          </q-img>
          <q-btn dense color="secondary" class="q-mt-sm">
            REPORT A PROBLEM
            <q-icon class="q-pl-sm" name="construction" size="1.5em"></q-icon>
          </q-btn>
        </div>
        <!--RIGHT-->
        <div class="column col-md-9 col-xs-12 q-pb-md">
          <!--TITLE-->
          <div style="width: 100%" class="q-px-md q-pb-md bl">
            <p class="q-my-none text-white  text-h2">{{ novel.name }}</p>
          </div>
          <!--INFOS-->
          <div style="width: 100%" class="q-pa-md bl">
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12">
                <q-icon color="secondary" name="fas fa-info-circle" size="2.5em"></q-icon>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-secondary  text-h4"></p></div>
            </div>
            <q-separator color="grey" style="opacity: 30%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">INTRO</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1 text-justify">
                {{ novel.intros.enIntro }}</p></div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">VOL NUM</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{
                  novel.volumesNum
                }}</p></div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">WRITTEN
                BY</p></div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{
                  novel.writtenBy
                }}</p></div>
            </div>
            <!--            <q-separator color="grey" style="opacity: 20%"></q-separator>-->
            <!--            <div class="row q-py-md">-->
            <!--              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">RELEASED-->
            <!--                AT</p></div>-->
            <!--              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{-->
            <!--                  animation.releasedAt-->
            <!--                }}</p></div>-->
            <!--            </div>-->
          </div>
          <!--FILE-->
          <div style="width: 100%" class="q-pa-md bl">
            <div class="row q-py-md ">
              <div class="col-md-2 col-xs-12">
                <q-icon color="secondary" name="fas fa-file-archive" size="2.5em"></q-icon>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-white text-h4"></p></div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">TYPE</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ novel.fileMeta.type }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">SIZE</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ novel.fileMeta.size }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">
                INTEGRATED</p>
              </div>
              <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">{{ novel.integrated }}</p>
              </div>
            </div>
            <q-separator color="grey" style="opacity: 20%"></q-separator>
            <div class="row q-py-md">
              <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">DOWNLOAD</p>
              </div>
              <div class="col-md-10 col-xs-12">
                <a :href="novel.fileAddresses.baiduCloud.url"><p class="q-my-none text-secondary text-body1">
                  {{ novel.fileAddresses.baiduCloud.password }}</p></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import {scroll} from 'quasar'


export default {
  name: "Novel",
  data() {
    return {
      novel: {},
      tab: 'Animations',
      text: '',
      LD: true,
      expanded: [],
      scrollInfo: {},
      ips: [],
      lorem: 'Kazuto "Kirito" Kirigaya enters a virtual-reality, massively multiplayer online role playing game called Sword Art Online. There is no escape from this world unless the player clears the game; however getting a "game over" results in the death of the player.'
    }
  },
  methods: {
    foo() {
    },
    onScroll(info) {
      this.scrollInfo = info
    }
  },
  mounted() {
    this.$axios.get('api/novel/info/1').then((response) => {
      const rd = response.data
      console.log('return data:')
      console.log(rd)
      if (rd.code === 'success') {
        this.novel = rd.data.novel
        console.log('animation:')
        console.log(this.novel)
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
  border-left-color: $secondary
  border-width: 3px
</style>
