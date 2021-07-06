<template>
  <q-page padding class=" bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
    <div class="q-mx-auto" style="width: 95%">
      <div class="row q-col-gutter-x-lg"><!--do not set padding-->
        <!--LEFT-->
        <div class="col-md-3 col-xs-12 q-pb-md"><!--do not set padding-->
          <div class="bg-dark-light text-white" style="border-radius: 5px">
            <q-list bordered separator v-if="!LD">
              <q-item
                clickable v-ripple v-for="(ann,i) in announcements" :key="'ann'+i" class="q-mb-none"
                @click="loadCurrentText(ann.uri)"
              >
                <q-item-section class="">{{ ann.title }}</q-item-section>
              </q-item>
            </q-list>
          </div>
        </div>

        <!--RIGHT-->
        <div class="col-md-9 col-xs-12 q-pb-md "><!--do not set padding-->
          <!--TITLE-->
          <div style="width: 100%; border-radius: 5px" class="q-py-md q-px-lg bg-dark-light ">
            <q-markdown
              content-class="text-white" :src="currentText"
              no-heading-anchor-links
              no-linkify
            />
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>

import devv from '../../docc/dev.md'

export default {
  name: 'Announcements',
  components: {},
  created() {
    this.$axios.get('api/semi_static/announcements').then((response) => {
      const rd = response.data
      console.log('return data:')
      console.log(rd)
      if (rd.code === 'success') {
        this.announcements = rd.data.announcements
        if(this.announcements.length !== 0){
          this.loadCurrentText(this.announcements[0].uri)
        }
      }
      this.LD = false
    }).catch(function (error) {
      console.log(error)
    })
  },
  data: () => ({
    LD: true,
    announcements : [],
    currentText:''
  }),
  methods: {
    loadCurrentText(uri){
      this.$axios.get('api/'+uri).then((response) => {
        this.currentText = response.data
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style lang="scss">

</style>
