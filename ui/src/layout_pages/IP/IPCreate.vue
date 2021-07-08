<template>
  <q-page padding class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em" v-if="!LD">
    <div class="q-mx-auto" style="width: 95%">
      <div class="column full-width">
        <div style="width: 100%" class="q-pl-md bl">
          <div class="row q-pb-md">
            <p class="q-my-none text-accent text-h4 ">NEW IP</p>
          </div>
        </div>
        <div style="width: 100%" class="q-pl-md bl">
          <div class="row items-center q-py-md">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">TAGS</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-select
                class="bg-dark-light"
                dark
                dense
                options-dense
                options-selected-class="text-accent"
                standout=""
                v-model="modelMultiple"
                multiple
                hide-bottom-space
                :options="options"
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
          <q-separator color="grey" style="opacity: 30%"></q-separator>
          <div class="row items-center q-py-md">
            <div class="col-md-2 col-xs-12">
              <p class="q-my-none text-grey text-body1 text-weight-medium">INTRO</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="text-h6 bg-dark-light" standout=""
                v-model="text"
                hide-bottom-space autogrow
              >
              </q-input>
            </div>
          </div>
          <q-separator color="grey" style="opacity: 20%"></q-separator>
          <div class="row items-center q-py-md">
            <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">TYPE</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="text-h5 bg-dark-light" standout=""
                v-model="text"
              >
              </q-input>
            </div>
          </div>
          <q-separator color="grey" style="opacity: 20%"></q-separator>
          <div class="row q-py-md">
            <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">EPS NUM</p>
            </div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="text-h5 bg-dark-light" standout=""
                v-model="text"
              >
              </q-input>
            </div>
          </div>
          <q-separator color="grey" style="opacity: 20%"></q-separator>
          <div class="row q-py-md">
            <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">PRODUCED
              BY</p></div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="text-h5 bg-dark-light" standout=""
                v-model="text"
              >
              </q-input>
            </div>
          </div>
          <q-separator color="grey" style="opacity: 20%"></q-separator>
          <div class="row q-py-md">
            <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">WRITTEN
              BY</p></div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="text-h5 bg-dark-light" standout=""
                v-model="text"
              >
              </q-input>
            </div>
          </div>
          <q-separator color="grey" style="opacity: 20%"></q-separator>
          <div class="row q-py-md">
            <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">RELEASED
              AT</p></div>
            <div class="col-md-10 col-xs-12">
              <q-input
                dense dark class="text-h5 bg-dark-light" standout=""
                v-model="text"
              >
              </q-input>
            </div>
          </div>
        </div>
        <div style="width: 100%" class="q-pl-md">
          <div class="row justify-end q-pa-md">
            <q-btn class="q-ml-md"  dense flat color="accent">cancel</q-btn>
            <q-btn class="q-ml-md"  dense flat color="accent">commit</q-btn>
          </div>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: "IPCreate",
  data: ()=>{
    return{
      modelMultiple: [ {
        label: 'Google',
        value: 'google',
      } ],
      text:'',
      options: [
        {
          label: 'Google',
          value: 'google',
        },
        {
          label: 'Facebook',
          value: 'fb',
        },
        {
          label: 'Twitter',
          value: 'twt',
        },
        {
          label: 'Apple',
          value: 'app',
        },
        {
          label: 'Oracle',
          value: 'ora',
        },
      ]
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

