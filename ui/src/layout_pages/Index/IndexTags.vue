<template>
  <div class="q-col-gutter-y-sm">
    <!--add tag-->
    <q-dialog v-model="tagCreateBuffer.isCreating">
      <div class="bg-dark column q-pa-lg " style="width: 60vw; max-width: 60vw;">
        <div style="width: 100%" class="q-pl-md bl">
          <div class="row q-pb-md">
            <p class="q-my-none text-accent text-h4 ">NEW TAG</p>
          </div>
        </div>
        <div style="width: 100%" class="q-pl-md bl">
          <div class="row items-center q-py-md">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">NAME</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="text-h6 bg-dark-light" standout=""
                v-model="tagCreateBuffer.data.name"
                hide-bottom-space
              >
              </q-input>
            </div>
          </div>
          <q-separator color="grey" style="opacity: 20%"></q-separator>
          <div class="row items-center q-py-md">
            <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">CN NAME</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="text-h6 bg-dark-light" standout=""
                v-model="tagCreateBuffer.data.reservedNames.cnName"
              >
              </q-input>
            </div>
          </div>
          <q-separator color="grey" style="opacity: 20%"></q-separator>
          <div class="row items-center q-py-md">
            <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">EN NAME</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="text-h6 bg-dark-light" standout=""
                v-model="tagCreateBuffer.data.reservedNames.enName"
              >
              </q-input>
            </div>
          </div>
        </div>
        <div style="width: 100%" class="q-pl-md">
          <div class="row justify-end">
            <q-btn class="q-ml-md"  dense flat color="accent" v-close-popup>cancel</q-btn>
            <q-btn
              class="q-ml-md"  dense flat color="accent"
              @click="commitCreate"
            >
              commit
            </q-btn>
          </div>
        </div>
      </div>
    </q-dialog>
    <!--content-->
    <div>
      <div class="row q-pt-md q-pb-sm q-px-md bg-dark-light bt" >
        <q-chip
          v-for="(tag,i) in tags" :key="'tag'+i"
          class="q-mr-sm q-mb-sm q-ml-none q-mt-none"
          dense
          square
          color="accent"
          removable
          @remove="commitDelete(tag.id)"
          clickable
        >
          <q-icon class="q-mx-xs" name="fas fa-tags" color="dark"></q-icon>
          {{tag.reservedNames[$i18n.locale+'Name']||tag.name}}
        </q-chip>
        <q-chip
          class="q-mr-sm q-mb-sm q-ml-none q-mt-none"
          text-color="dark"
          dense
          square
          color="accent"
          clickable
          outline
          @click="tagCreateBuffer.isCreating = true"
        >
          <q-icon size="1.1em" class="q-mr-xs"  name="fas fa-plus" color="accent"></q-icon>
          New
        </q-chip>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "IndexTags",
  created() {
    this.initTags()
  },
  data: () => ({
    LD: true,
    tags:[],
    tagCreateBuffer:{
      isCreating: false,
      data: {
        name: '',
        reservedNames: {
          enName:'',
          cnName:''
        }
      },
    },
    text: 'false'
  }),
  methods: {
    foo(i){
      console.log(i)
    },
    initTags(){
      this.$axios.get('api/tag/list').then((response) => {
        const rd = response.data
        console.log('return data:')
        console.log(rd)
        if (rd.code === 'success') {
          this.tags = rd.data.tags
        }
        this.LD = false
      }).catch(function (error) {
        console.log(error)
      })
    },
    initTagCreateBufferData(){
      this.tagCreateBuffer.data = {
        name: '',
        reservedNames: {
          enName:'',
          cnName:''
        }
      }
    },
    commitCreate(){
      this.$axios.post('api/tag/create', this.tagCreateBuffer.data).then((response) => {
        let rd = response.data
        if (rd.code === 'success') {
          this.$q.notify({
            type: 'success',
            message: `New tag was submitted successfully.`
          })
          this.initTags()
          this.initTagCreateBufferData()
          this.tagCreateBuffer.isCreating=false
        }else {
          console.log(response)
          this.$q.notify({
            type: 'failure',
            message: `failure`
          })
        }
      }).catch((error) => {
        console.log(error)
      })
    },
    commitDelete(id){
      const data = {
        id:id
      }
      this.$axios.post('api/tag/delete', data).then((response) => {
        let rd = response.data
        if (rd.code === 'success') {
          this.$q.notify({
            type: 'success',
            message: `delete tag was submitted successfully.`
          })
          this.initTags()
        }else {
          console.log(response)
          this.$q.notify({
            type: 'failure',
            message: `failure`
          })
        }
      }).catch((error) => {
        console.log(error)
      })
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
