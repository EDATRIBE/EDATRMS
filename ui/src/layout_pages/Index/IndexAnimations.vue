<template>
  <div>
    <!--Tools-->
    <q-expansion-item
      dense
      dark
      expand-icon-toggle
      class="q-mb-md"
      header-class="bl q-pa-none "
      expand-icon-class="q-pr-sm text-primary"
      expand-icon="filter_alt"
      expanded-icon="filter_alt"
    >
      <!--IPHeader-->
      <template v-slot:header>
        <div class="row  items-center text-body1 full-width ">
          <q-btn-toggle
            text-color="grey-7"
            dense
            size="0.75em"
            flat
            class="no-border-radius"
            v-model="model"
            toggle-color="primary"
            :options="[
              {label:'date', icon: 'fas fa-sort-numeric-down-alt', value: 'one'},
              {label:'alphabet', icon: 'fas fa-sort-alpha-down', value: 'two'}
            ]"
          />
        </div>
      </template>
      <q-item dense dark class="q-pa-none bl1 q-mt-sm" style="padding-right: 39.5px">
        <div class="row items-center text-body1 full-width ">
          <q-btn-toggle
            unelevated
            size="0.75em"
            text-color="grey-7"
            class="no-border-radius bg-dark-light"
            v-model="model1"
            toggle-color="primary"
            :options="[
              {label:'ALL',value: '0'},
              {label:'TV',value: 'one'},
              {label:'EPS',  value: 'two'}
            ]"
          />
        </div>
      </q-item>
      <q-item dense dark class="q-pa-none bl1 q-mt-sm" style="padding-right: 39.5px">
        <div class="row items-center text-body1 full-width ">
          <q-btn-toggle
            unelevated
            size="0.75em"
            text-color="grey-7"
            class="no-border-radius bg-dark-light"
            v-model="model2"
            toggle-color="primary"
            :options="[
              {label:'ALL',value: '0'},
              {label:'1960s',value: 'one'},
              {label:'1970s',  value: 'two'},
              {label:'1960s',value: '3'},
              {label:'1980s',  value: '4'},
              {label:'1990s',value: '5'},
              {label:'2000s',  value: '6'},
              {label:'2010s',value: '7'},
              {label:'2020s',  value: '8'}
            ]"
          />
        </div>
      </q-item>
      <q-item dense dark class="q-pa-none bl1 q-mt-sm" style="padding-right: 39.5px">
        <div class="row items-center text-body1 full-width ">
          <q-btn-toggle
            unelevated
            text-color="grey-7"
            class="no-border-radius bg-dark-light"
            v-model="model3"
            size="0.75em"
            toggle-color="primary"
            :options="[
              {label:'ALL',value: '0'},
              {label:'360P',value: 'one'},
              {label:'480P',  value: 'two'},
              {label:'620P',value: '3'},
              {label:'720P',  value: '4'},
              {label:'920P',value: '5'},
              {label:'1080P',  value: '6'}
            ]"
          />
        </div>
      </q-item>
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
export default {
  name: "IndexAnimations",
  data: () => ({
    tab: 'Animations',
    text: '',
    LD: true,
    expanded: [],
    scrollInfo: {},
    model: '',model1: '',model2: '',model3: '',
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
</style>
