<template v-if="initialized">
  <q-page padding class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
    <div class="q-mx-auto" style="width: 95%">
      <div class="column full-width">

        <!--Title-->
        <div style="width: 100%" class="q-pl-md bl">
          <div class="row q-pb-md">
            <p class="q-my-none text-accent text-h4 ">EDIT IP</p>
          </div>
        </div>

        <!--Fields-->
        <div style="width: 100%" class="q-pl-md bl">
          <!--Name-->
          <div class="row items-center q-py-sm">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">NAME</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="bg-dark-light" standout=""
                v-model="IPEditBuffer.data.name"
              >
              </q-input>
            </div>
          </div>
          <!--cnName-->
          <div class="row items-center q-py-sm">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">NAME-CN</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="bg-dark-light" standout=""
                v-model="IPEditBuffer.data.reservedNames.cn"
              >
              </q-input>
            </div>
          </div>
          <!--enName-->
          <div class="row items-center q-py-sm">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">NAME-EN</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="bg-dark-light" standout=""
                v-model="IPEditBuffer.data.reservedNames.en"
              >
              </q-input>
            </div>
          </div>
          <!--jpName-->
          <div class="row items-center q-py-sm">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">NAME-JP</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class=" bg-dark-light" standout=""
                v-model="IPEditBuffer.data.reservedNames.jp"
              >
              </q-input>
            </div>
          </div>
          <!--rmName-->
          <div class="row items-center q-py-sm">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">NAME-RM</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class=" bg-dark-light" standout=""
                v-model="IPEditBuffer.data.reservedNames.rm"
              >
              </q-input>
            </div>
          </div>
          <!--miscName-->
          <div class="row items-center q-py-sm">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">NAME-MISC</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class=" bg-dark-light" standout=""
                v-model="IPEditBuffer.data.reservedNames.misc"
              >
              </q-input>
            </div>
          </div>
          <q-separator color="grey-7" class="q-my-sm"></q-separator>
          <!--Region-->
          <div class="row items-center q-py-sm">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">REGION</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-select
                class="bg-dark-light"
                dark
                dense
                options-dense
                options-selected-class="text-accent"
                standout=""
                v-model="IPEditBuffer.data.region"
                hide-bottom-space
                :options="regionModels"
                emit-value
                map-options
              >
              </q-select>
            </div>
          </div>
          <!--Tags-->
          <div class="row items-center q-py-sm">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">TAGS</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-select
                class="bg-dark-light"
                dark dense
                options-dense
                options-selected-class="text-accent"
                standout=""
                v-model="selectedTagModelsBuffer.data"
                multiple
                hide-bottom-space
                :options="tagModels"
                use-chips
                stack-label
              >
                <template v-slot:selected-item="scope">
                  <q-chip
                    square
                    removable
                    dark
                    dense
                    text-color="dark"
                    @remove="scope.removeAtIndex(scope.index)"
                    :tabindex="scope.tabindex"
                    color="accent"
                    class="q-my-xs q-mr-xs q-ml-none"
                    spellcheck="false"
                  >
                    {{ scope.opt.label }}
                  </q-chip>
                </template>
              </q-select>
            </div>
          </div>
          <q-separator color="grey-7" class="q-my-sm"></q-separator>
          <!--Comment-->
          <div class="row items-center q-py-sm">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">COMMENT</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class=" bg-dark-light" standout=""
                v-model="IPEditBuffer.data.comment"
              >
              </q-input>
            </div>
          </div>

        </div>

        <!--Actions-->
        <div style="width: 100%" class="q-pl-md">
          <div class="row justify-end q-py-md">
            <q-btn
              class="q-ml-md" dense flat color="accent"
              @click="$router.go(-1)"
            >
              cancel
            </q-btn>
            <q-btn
              class="q-ml-md" dense flat color="accent"
              @click="commitEdit"
            >
              commit
            </q-btn>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "IPEdit",
  created() {
    if (this.readyToInitialize) this.initPage()
  },
  data() {
    return {
      IPEditBuffer: {
        loading: true,
        data: {
          name: '',
          reservedNames: {
            en: '',
            cn: '',
            jp: '',
            rm: '',
            misc: ''
          },
          region: '',
          comment: ''
        }
      },
      selectedTagModelsBuffer: {
        loading: true,
        data: []
      },
    }
  },
  methods: {
    foo() {
    },
    initPage() {
      const ipId = this.$route.query.id
      for (const ip of this.ips) {
        if (ip.id === Number(ipId)) {
          this.initIPEditBuffer(ip)
          this.initSelectedTagModelsBuffer(ip.tags)
        }
      }
    },
    initIPEditBuffer(ip) {
      console.log(this)
      this.IPEditBuffer.data.id = ip.id
      this.IPEditBuffer.data.name = ip.name
      this.IPEditBuffer.data.reservedNames.en = ip.reservedNames.en
      this.IPEditBuffer.data.reservedNames.cn = ip.reservedNames.cn
      this.IPEditBuffer.data.reservedNames.jp = ip.reservedNames.jp
      this.IPEditBuffer.data.reservedNames.rm = ip.reservedNames.rm
      this.IPEditBuffer.data.reservedNames.misc = ip.reservedNames.misc
      this.IPEditBuffer.data.region = ip.region
      this.IPEditBuffer.data.comment = ip.comment
      this.IPEditBuffer.loading = false
    },
    initSelectedTagModelsBuffer(tags) {
      for (const tag of tags) {
        for (const tagModel of this.tagModels) {
          if (tagModel.value === tag.id) this.selectedTagModelsBuffer.data.push(tagModel)
        }
      }
      this.selectedTagModelsBuffer.loading = false
    },
    commitEdit() {
      this.$axios.post('api/ip/edit', this.IPEditBuffer.data).then((response) => {
        let rd = response.data
        if (rd.code === 'success') {
          this.$q.notify({type: 'success', message: this.$t("messages.success")})
          let temp = {
            ipId: rd.data.ip.id,
            tagIds: []
          }
          for (const selectedTagModel of this.selectedTagModelsBuffer.data) {
            temp.tagIds.push(selectedTagModel.value)
          }
          this.$axios.post('api/ip/set/tags', temp).then((response) => {
            let rd = response.data
            if (rd.code === 'success') {
              this.$q.notify({type: 'success', message: this.$t("messages.success")})
            } else {
              console.log(response)
              this.$q.notify({type: 'failure', message: this.$t("messages.failure")})
            }
            this.$store.dispatch('getIPs').then(() => {
              this.$router.push('/index/ips_and_tags')
            })
          }).catch((error) => {
            console.log(error)
          })
        } else {
          console.log(response)
          this.$q.notify({type: 'failure', message: this.$t("messages.failure")})
        }
      }).catch((error) => {
        console.log(error)
        this.$q.notify({type: 'failure', message: this.$t("messages.failure")})
      })
    }
  },
  computed: {
    readyToInitialize() {
      return this.$store.getters.ipsInitialized && this.$store.getters.tagsInitialized
    },
    initialized() {
      return !this.IPEditBuffer.loading && !this.selectedTagModelsBuffer.loading
    },
    ips() {
      return this.$store.state.ip.ips
    },
    tags() {
      return this.$store.state.tag.tags
    },
    tagModels() {
      if (!this.tags) return []
      const temp = []
      for (const tag of this.tags) {
        temp.push({
          label: tag.reservedNames[this.$i18n.locale] || tag.name,
          value: tag.id
        })
      }
      return temp
    },
    regionModels() {
      return [
        {
          label: 'cn',
          value: 'CN'
        },
        {
          label: 'jp',
          value: 'JP'
        },
        {
          label: 'other',
          value: 'OTHER'
        },
      ]
    }
  },
  watch: {
    readyToInitialize() {
      if (this.readyToInitialize) {
        console.log('readyToInitialize,this.ips:')
        console.log(this.ips)
        this.initPage()
      }
    }
  }
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
  border-left-color: $accent
  border-width: 3px
</style>

