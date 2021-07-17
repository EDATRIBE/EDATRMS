<template>
  <div class="q-pt-sm">
    <IPDeleteDialog :is-deleting.sync="isDeleting"></IPDeleteDialog>
    <div class="q-col-gutter-y-sm" v-if="ready">
      <!--Tools-->
      <div>
        <q-expansion-item
          dense
          dark
          expand-icon-toggle
          header-class="bl q-pa-none "
          expand-icon-class="q-pr-sm text-accent"
          expand-icon="filter_alt"
          expanded-icon="filter_alt"
          :duration="200"
        >
          <!--Header-->
          <template v-slot:header>
            <div class="row  items-center text-body1 full-width ">
              <q-btn-toggle
                text-color="grey-7"
                size="0.75em"
                unelevated
                class="no-border-radius bg-dark-light"
                v-model="model"
                toggle-color="accent"
                toggle-text-color="dark"
                :options="[
              {label:'date', icon: 'fas fa-sort-numeric-down-alt', value: 'one'},
              {label:'alphabet', icon: 'fas fa-sort-alpha-down', value: 'two'}
            ]"
              />
              <q-space></q-space>
              <q-icon
                name="fas fa-plus" color="accent" size="1.25em" class="q-mx-sm cursor-pointer"
                @click="$router.push('/ip/create')"
              />
            </div>
          </template>

        </q-expansion-item>
      </div>
      <!--Content-->
      <div v-for="(ip,i) in currentIPS" :key="i+'ip'+ip.id">
        <!--IPS-->
        <q-expansion-item
          dense
          dark
          expand-icon-toggle
          class="bg-dark-light bl"
          header-class="bl q-pa-none bg-dark-light"
          expand-icon-class="q-px-sm text-accent"
          :duration="200"
        >
          <!--IPHeader-->
          <template v-slot:header>
            <div class="row no-wrap q-pl-md  items-center text-body1 full-width ">
              <q-icon name="source" color="accent" size="1.3em" class="q-mr-md"></q-icon>
              {{ ip.reservedNames[$i18n.locale] || ip.name }}
              <div class="row q-mx-md">
                <q-chip
                  v-for="(tag,i) in ip.tags" :key="i+'tag'+ip.id+tag.id"
                  size="0.7em" square dense text-color="dark" color="accent" class="q-py-none"
                >
                  {{ tag.reservedNames[$i18n.locale] || tag.name }}
                </q-chip>
              </div>
              <q-space></q-space>
              <q-btn flat color="accent" icon="add">animation</q-btn>
              <q-btn flat color="accent" icon="add">novel</q-btn>
              <q-btn
                flat color="accent"
                @click="isDeleting=true"
              >
                edit
              </q-btn>
              <q-btn
                flat color="red"
                @click="commitIPDelete(ip.id)"
              >
                delete
              </q-btn>
            </div>
          </template>

          <!--IPContent-->
          <div class="q-pl-lg q-pb-sm">

            <!--Animations-->
            <q-expansion-item
              dense
              dark
              expand-icon-toggle
              class="bg-dark-light bl1 q-mt-sm"
              header-class="bl q-pa-none bg-dark-light"
              expand-icon-class="q-px-sm text-primary"
              :duration="200"
              v-for="(animation,i) in ip.animations" :key="i+'ani'+ip.id+animation.id"
            >
              <!--AnimationsHeader-->
              <template v-slot:header>
                <div class="row q-pl-md  items-center text-body1 full-width ">
                  <q-icon name="movie" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                  {{ animation.reservedNames[$i18n.locale] || animation.name }}
                  <q-space></q-space>
                  <q-btn icon="add" flat color="primary">video</q-btn>
                  <q-btn icon="add" flat color="primary">caption</q-btn>
                  <q-btn flat color="primary">edit</q-btn>
                  <q-btn flat color="red">delete</q-btn>
                </div>
              </template>

              <!--AnimationsContent-->
              <div class="q-pl-lg ">
                <!--AnimationsVideo-->
                <q-item
                  dense dark class="bg-dark-light q-pa-none bl1 q-mt-sm" style="padding-right: 39.3px"
                  v-for="(video,i) in animation.videos" :key="i+'vid'+animation.id+video.id"
                >
                  <div class="row q-pl-md items-center text-body1 full-width ">
                    <q-icon name="fas fa-film" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                    {{ video.fileMeta.name || 'video' + i }}
                    <q-space></q-space>
                    <q-btn flat color="primary">edit</q-btn>
                    <q-btn flat color="red">delete</q-btn>
                  </div>
                </q-item>
                <!--AnimationsCaption-->
                <q-item
                  dense dark class="bg-dark-light q-pa-none bl1 q-mt-sm" style="padding-right: 39.3px"
                  v-for="(caption,i) in animation.captions" :key="i+'cap'+animation.id+caption.id"
                >
                  <div class="row q-pl-md items-center text-body1 full-width ">
                    <q-icon name="fas fa-closed-captioning" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                    {{ caption.fileMeta.name || 'caption' + i }}
                    <q-space></q-space>
                    <q-btn flat color="primary">edit</q-btn>
                    <q-btn flat color="red">delete</q-btn>
                  </div>
                </q-item>
              </div>
            </q-expansion-item>


            <!--Novel-->
            <q-item
              dense dark class="bg-dark-light q-pa-none bl2 q-mt-sm" style="padding-right: 39.3px"
              v-for="(novel,i) in ip.novels" :key="i+'nov'+ip.id+novel.id"
            >
              <div class="row q-pl-md items-center text-body1 full-width ">
                <q-icon name="import_contacts" color="secondary" size="1.3em" class="q-mr-md"></q-icon>
                {{ novel.reservedNames[$i18n.locale] || novel.name }}
                <q-space></q-space>
                <q-btn flat color="secondary">edit</q-btn>
                <q-btn flat color="red">delete</q-btn>
              </div>
            </q-item>
          </div>

        </q-expansion-item>
      </div>
    </div>
    <!--pagination-->
    <div class="full-width row justify-center q-my-xs">
      <q-pagination
        v-model="current"
        :max="100"
        color="accent"
        input
        input-class="text-accent"
      />
    </div>
  </div>
</template>

<script>
import IPDeleteDialog from "src/layout_pages/IP/IPDeleteDialog";

export default {
  name: "IndexIPs",
  components: {IPDeleteDialog},
  data() {
    return {
      model: '',
      current: 3,
      isDeleting: false
    }
  },
  methods: {
    foo(i) {
      console.log(i)
    },
    commitIPDelete(id) {
      let temp = {id: id}
      this.$axios.post('api/ip/delete', temp).then((response) => {
        let rd = response.data
        if (rd.code === 'success') {
          this.$q.notify({type: 'success', message: this.$t("messages.success")})
          this.$store.dispatch('getIPs')
        } else {
          console.log(response)
          this.$q.notify({type: 'failure', message: this.$t("messages.failure")})
        }
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  computed: {
    currentIPS() {
      return this.$store.state.ip.ips
    },
    ready() {
      return this.$store.state.ip.ready
    }
  }
}
</script>

<style lang="sass" scoped>
.bl
  border-left: solid
  border-left-color: $accent
  border-width: 2px

.bl1
  border-left: solid
  border-left-color: $primary
  border-width: 2px

.bl2
  border-left: solid
  border-left-color: $secondary
  border-width: 2px

.bl3
  border-left: solid
  border-left-color: white
  border-width: 2px

.bt
  border-top: solid
  border-top-color: $accent
  border-top-width: 2px

//border-bottom: solid
//border-bottom-color: $accent
//border-bottom-width: 2px
</style>
