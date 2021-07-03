<template>
  <div>
    <!--Tools-->
    <q-expansion-item
      dense
      dark
      expand-icon-toggle
      class=" q-mb-sm"
      header-class="bl q-pa-none "
      expand-icon-class="q-pr-sm text-primary"
      expand-icon="filter_alt"
      expanded-icon="filter_alt"
    >
      <!--ToolsHeader-->
      <template v-slot:header>
        <div class="row items-center text-body1 full-width ">
          <q-btn-toggle
            text-color="grey-7"  size="0.75em" flat dense
            class="no-border-radius" toggle-color="primary"
            v-model="order"
            :options="[
              {label:'date', icon: 'fas fa-sort-numeric-down-alt', value: 'date'},
              {label:'alphabet', icon: 'fas fa-sort-alpha-down', value: 'alphabet'}
            ]"
          />
        </div>
      </template>
      <!--ToolsContent-->
      <div class="q-pt-xs q-pb-sm bb">
        <!--region-->
        <q-item dense dark class="q-pa-none bl1">
          <multiple-choice
            class="text-body1"
            :options="[
                {label:'All', value: 'all'},
                {label:'CN', value: 'cn'},
                {label:'JP', value: 'jp'},
                {label:'OTHER', value: 'other'},
              ]"
            v-model="region"
            text-class="text-grey-7"
            b-g-class="bg-dark-light"
            active-text-class="text-white"
            active-b-g-class="bg-primary"
          />
        </q-item>

        <!--type-->
        <q-item dense dark class="q-pa-none bl1 q-mt-sm">
          <multiple-choice
            class="text-body1"
            :options="[
                {label:'ALL',value: 'all'},
                {label:'TV',value: 'tv'},
                {label:'EPS',  value: 'eps'}
              ]"
            v-model="type"
            text-class="text-grey-7"
            b-g-class="bg-dark-light"
            active-text-class="text-white"
            active-b-g-class="bg-primary"
          />
        </q-item>

        <!--date-->
        <q-item dense dark class="q-pa-none bl1 q-mt-sm">
          <multiple-choice
            class="text-body1"
            :options="[
                {label:'ALL',value: 'all'},
                {label:'1960s', value: '1960s'},
                {label:'1970s', value: '1970s'},
                {label:'1980s', value: '1980s'},
                {label:'1990s', value: '1990s'},
                {label:'2000s', value: '2000s'},
                {label:'2010s', value: '2010s'},
                {label:'2020s', value: '2020s'}
              ]"
            v-model="date"
            text-class="text-grey-7"
            b-g-class="bg-dark-light"
            active-text-class="text-white"
            active-b-g-class="bg-primary"
          />
        </q-item>

        <!--quality-->
        <q-item dense dark class="q-pa-none bl1 q-mt-sm">
          <multiple-choice
            class="text-body1"
            :options="[
                {label:'ALL',value: 'all'},
                {label:'360P', value: '360P'},
                {label:'640P', value: '640P'},
                {label:'720P', value: '720P'},
                {label:'960P', value: '960P'},
                {label:'1080P', value: '1080P'}
              ]"
            v-model="quality"
            text-class="text-grey-7"
            b-g-class="bg-dark-light"
            active-text-class="text-white"
            active-b-g-class="bg-primary"
          />
        </q-item>

        <!--videoType-->
        <q-item dense dark class="q-pa-none bl1 q-mt-sm">
          <multiple-choice
            class="text-body1"
            :options="[
                {label:'ALL',value: 'all'},
                {label:'MP4', value: '360P'},
                {label:'MKV', value: '640P'},
                {label:'AV1', value: '720P'},
                {label:'OGG', value: '960P'}
              ]"
            v-model="videoType"
            text-class="text-grey-7"
            b-g-class="bg-dark-light"
            active-text-class="text-white"
            active-b-g-class="bg-primary"
          />
        </q-item>

        <!--captions-->
        <q-item dense dark class="q-pa-none bl1 q-mt-sm">
          <multiple-choice
            class="text-body1"
            :options="[
                {label:'ALL',value: 'all'},
                {label:'CLOSED CAPTION', value: 'true'},
                {label:'NO CAPTION', value: 'false'},
              ]"
            v-model="hasCaption"
            text-class="text-grey-7"
            b-g-class="bg-dark-light"
            active-text-class="text-white"
            active-b-g-class="bg-primary"
          />
        </q-item>
      </div>
    </q-expansion-item>

    <!--Content-->
    <div class="row q-col-gutter-x-md q-col-gutter-y-lg">
      <div class="col-md-2 col-sm-3 col-xs-6" v-for="i in 20" :key="i">
        <q-card class="bg-dark-light" flat square>
          <img :src="require('assets/aaa.jpg')">
          <q-card-section class="q-pa-xs text-white text-body1 text-weight-bold ov">
            {{ lorem }}
          </q-card-section>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script>
import MultipleChoice from "components/MultipleChoice";

export default {
  name: "IndexAnimations",
  components: {MultipleChoice},
  data: () => ({
    tab: 'Animations',
    text: '',
    LD: true,
    expanded: [],
    scrollInfo: {},
    soo: false,
    order: 'date',
    region: 'all',
    type: 'all',
    date: 'all',
    quality: 'all',
    videoType: 'all',
    hasCaption: 'all',
    ips: [],
    lorem: 'Kazuto "Kirito" Kirigaya enters a virtual-reality, massively multiplayer online role playing game called Sword Art Online. There is no escape from this world unless the player clears the game; however getting a "game over" results in the death of the player.'
  }),
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

.bb
  border-bottom: solid
  border-bottom-color: $primary
  border-width: 2px
</style>
