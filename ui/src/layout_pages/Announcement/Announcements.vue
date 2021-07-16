<template>
  <q-page padding class=" bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
    <div class="q-mx-auto" style="width: 95%">
      <div class="row q-col-gutter-x-lg"><!--do not set margin-->
        <!--LEFT-->
        <div class="col-md-3 col-xs-12 q-pb-md"><!--do not set margin-->
          <div class="bg-dark-light text-grey-6" style="border-radius: 5px">
            <q-list bordered separator v-if="!LD">
              <q-item
                clickable v-ripple
                v-for="(ann,i) in announcements" :key="'ann'+i" class="q-mb-none text-body1 text-weight-medium"
                @click="selectAnnouncement(i,ann.uri)"
                active-class="acann"
                :active="i===currentId"
              >
                <q-item-section>
                  <div class="row no-wrap items-center">
                    <q-icon size="1.5em" class="q-mr-md" name="article"></q-icon>
                    {{ ann.title }}
                  </div>

                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </div>

        <!--RIGHT-->
        <div class="col-md-9 col-xs-12 q-pb-md "><!--do not set margin-->
          <div style="width: 100%; border-radius: 5px" class="q-py-md q-px-lg bg-dark-light " v-if="!LD">
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
        if (this.announcements.length !== 0) {
          this.selectAnnouncement(0, this.announcements[0].uri)
        }
      }
    }).catch(function (error) {
      console.log(error)
    })
  },
  data: () => ({
    LD: true,
    announcements: [],
    currentText: '',
    currentId: 0
  }),
  methods: {
    selectAnnouncement(i, uri) {
      this.currentId = i
      this.$axios.get('api/' + uri).then((response) => {
        this.currentText = response.data
        this.LD = false
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style lang="sass" scoped>
.bl
  border-left: solid
  border-left-color: white
  border-width: 2px

.acann
  color: $dark
  background-color: white

  //border-right: solid
  //border-color: white
  //border-width: 2px

</style>
