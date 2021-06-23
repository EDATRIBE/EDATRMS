<template>
  <div class="row q-col-gutter-x-md q-col-gutter-y-lg">
    <div class="col-md-2 col-sm-3 col-xs-6" v-for="i in 20" :key="i">
      <q-card class="bg-grey-4 shadow-8" square>
        <img :src="require('assets/aaa.jpg')">
        <q-card-section class="q-pa-xs text-white text-body1 text-weight-bold bg-dark ov">
          {{ lorem }}
        </q-card-section>
      </q-card>
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
