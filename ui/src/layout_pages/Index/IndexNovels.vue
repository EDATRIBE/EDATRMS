<template>
  <div class="q-pt-sm">

    <!--Tools-->
    <q-expansion-item
      dense
      dark
      expand-icon-toggle
      class="q-mb-sm "
      header-class="bl q-pa-none "
      expand-icon-class="q-pr-sm text-secondary"
      expand-icon="filter_alt"
      expanded-icon="filter_alt"
    >
      <!--Header-->
      <template v-slot:header>
        <div class="row  items-center text-body1 full-width ">
          <q-btn-toggle
            text-color="grey-7"
            dense
            size="0.75em"
            flat
            class="no-border-radius"
            v-model="model"
            toggle-color="secondary"
            :options="[
              {label:'date', icon: 'fas fa-sort-numeric-down-alt', value: 'one'},
              {label:'alphabet', icon: 'fas fa-sort-alpha-down', value: 'two'}
            ]"
          />
        </div>
      </template>
      xxx
    </q-expansion-item>

    <!--Content-->
    <div class="row q-col-gutter-x-md q-col-gutter-y-lg">
      <div class="col-md-2 col-sm-3 col-xs-6" v-for="i in 20" :key="i">
        <q-card class="bg-grey-4 shadow-8" flat square>
          <img :src="require('assets/aaa.jpg')">
          <q-card-section class="q-pa-xs text-white text-body1 text-weight-bold bg-dark ov">
            {{ lorem }}
          </q-card-section>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "IndexNovels",
  data: () => ({
    tab: 'Animations',
    text: '',
    model: '',
    LD: true,
    expanded: [],
    scrollInfo: {},
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
