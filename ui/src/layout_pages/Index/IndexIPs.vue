<template>
  <div class="q-col-gutter-y-sm">
    <!--Tools-->
    <q-expansion-item
      dense
      dark
      expand-icon-toggle
      header-class="bl q-pa-none "
      expand-icon-class="q-pr-sm text-accent"
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
            toggle-color="accent"
            :options="[
              {label:'date', icon: 'fas fa-sort-numeric-down-alt', value: 'one'},
              {label:'alphabet', icon: 'fas fa-sort-alpha-down', value: 'two'}
            ]"
          />
          <q-space></q-space>
          <q-icon name="fas fa-plus" color="accent" size="1.25em" class="q-mx-sm"></q-icon>
        </div>
      </template>

    </q-expansion-item>

    <!--Content-->
    <div v-for="i in 10" :key="i">
      <!--IPS-->
      <q-expansion-item
        dense
        dark
        expand-icon-toggle
        class="bg-dark-light bl"
        header-class="bl q-pa-none bg-dark-light"
        expand-icon-class="q-px-sm text-accent"
      >
        <!--IPHeader-->
        <template v-slot:header>
          <div class="row q-pl-md  items-center text-body1 full-width ">
            <q-icon name="source" color="accent" size="1.3em" class="q-mr-md"></q-icon>
            IPXXXXXXXX
            <q-space></q-space>
            <q-btn flat color="accent" icon="add">animation</q-btn>
            <q-btn flat color="accent" icon="add">novel</q-btn>
            <q-btn flat color="accent" >edit</q-btn>
            <q-btn flat color="red">delete</q-btn>
          </div>
        </template>

        <!--IPContent-->
        <div class="q-pl-md ">

          <!--Animations-->
          <q-expansion-item
            dense
            dark
            expand-icon-toggle
            class="bg-dark-light bl1 q-mt-sm"
            header-class="bl q-pa-none bg-dark-light"
            expand-icon-class="q-px-sm text-primary"
          >
            <!--AnimationsHeader-->
            <template v-slot:header>
              <div class="row q-pl-md  items-center text-body1 full-width ">
                <q-icon name="movie" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                AnimationPXXXXXXXX
                <q-space></q-space>
                <q-btn icon="add" flat color="primary">video</q-btn>
                <q-btn icon="add" flat color="primary">caption</q-btn>
                <q-btn flat color="primary">edit</q-btn>
                <q-btn flat color="red">delete</q-btn>
              </div>
            </template>

            <!--AnimationsContent-->
            <div class="q-pl-md ">
              <!--AnimationsVideo-->
              <q-item dense dark class="bg-dark-light q-pa-none bl1 q-mt-sm" style="padding-right: 39.5px">
                <div class="row q-pl-md items-center text-body1 full-width ">
                  <q-icon name="fas fa-film" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                  VideoXXXXXXXX
                  <q-space></q-space>
                  <q-btn flat color="primary">edit</q-btn>
                  <q-btn flat color="red">delete</q-btn>
                </div>
              </q-item>
              <!--AnimationsCaption-->
              <q-item dense dark class="bg-dark-light q-pa-none bl1 q-mt-sm" style="padding-right: 39.5px">
                <div class="row q-pl-md items-center text-body1 full-width ">
                  <q-icon name="fas fa-closed-captioning" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                  CaptionXXXXXXXX
                  <q-space></q-space>
                  <q-btn flat color="primary">edit</q-btn>
                  <q-btn flat color="red">delete</q-btn>
                </div>
              </q-item>
            </div>
          </q-expansion-item>
          <!--Animations-->
          <q-expansion-item
            dense
            dark
            expand-icon-toggle
            class="bg-dark-light bl1 q-mt-sm"
            header-class="bl q-pa-none bg-dark-light"
            expand-icon-class="q-px-sm text-primary"
          >
            <!--AnimationsHeader-->
            <template v-slot:header>
              <div class="row q-pl-md  items-center text-body1 full-width ">
                <q-icon name="movie" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                AnimationPXXXXXXXX
                <q-space></q-space>
                <q-btn icon="add" flat color="primary">video</q-btn>
                <q-btn icon="add" flat color="primary">caption</q-btn>
                <q-btn flat color="primary">edit</q-btn>
                <q-btn flat color="red">delete</q-btn>
              </div>
            </template>

            <!--AnimationsContent-->
            <div class="q-pl-md ">
              <!--AnimationsVideo-->
              <q-item dense dark class="bg-dark-light q-pa-none bl1 q-mt-sm" style="padding-right: 39.5px">
                <div class="row q-pl-md items-center text-body1 full-width ">
                  <q-icon name="fas fa-film" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                  VideoXXXXXXXX
                  <q-space></q-space>
                  <q-btn flat color="primary">edit</q-btn>
                  <q-btn flat color="red">delete</q-btn>
                </div>
              </q-item>
              <!--AnimationsCaption-->
              <q-item dense dark class="bg-dark-light q-pa-none bl1 q-mt-sm" style="padding-right: 39.5px">
                <div class="row q-pl-md items-center text-body1 full-width ">
                  <q-icon name="fas fa-closed-captioning" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                  CaptionXXXXXXXX
                  <q-space></q-space>
                  <q-btn flat color="primary">edit</q-btn>
                  <q-btn flat color="red">delete</q-btn>
                </div>
              </q-item>
            </div>
          </q-expansion-item>
          <!--Animations-->
          <q-expansion-item
            dense
            dark
            expand-icon-toggle
            class="bg-dark-light bl1 q-mt-sm"
            header-class="bl q-pa-none bg-dark-light"
            expand-icon-class="q-px-sm text-primary"
          >
            <!--AnimationsHeader-->
            <template v-slot:header>
              <div class="row q-pl-md  items-center text-body1 full-width ">
                <q-icon name="movie" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                AnimationPXXXXXXXX
                <q-space></q-space>
                <q-btn icon="add" flat color="primary">video</q-btn>
                <q-btn icon="add" flat color="primary">caption</q-btn>
                <q-btn flat color="primary">edit</q-btn>
                <q-btn flat color="red">delete</q-btn>
              </div>
            </template>

            <!--AnimationsContent-->
            <div class="q-pl-md ">
              <!--AnimationsVideo-->
              <q-item dense dark class="bg-dark-light q-pa-none bl1 q-mt-sm" style="padding-right: 39.5px">
                <div class="row q-pl-md items-center text-body1 full-width ">
                  <q-icon name="fas fa-film" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                  VideoXXXXXXXX
                  <q-space></q-space>
                  <q-btn flat color="primary">edit</q-btn>
                  <q-btn flat color="red">delete</q-btn>
                </div>
              </q-item>
              <!--AnimationsCaption-->
              <q-item dense dark class="bg-dark-light q-pa-none bl1 q-mt-sm" style="padding-right: 39.5px">
                <div class="row q-pl-md items-center text-body1 full-width ">
                  <q-icon name="fas fa-closed-captioning" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                  CaptionXXXXXXXX
                  <q-space></q-space>
                  <q-btn flat color="primary">edit</q-btn>
                  <q-btn flat color="red">delete</q-btn>
                </div>
              </q-item>
            </div>
          </q-expansion-item>

          <!--Novel-->
          <q-item dense dark class="bg-dark-light q-pa-none bl2 q-mt-sm" style="padding-right: 39.5px">
            <div class="row q-pl-md items-center text-body1 full-width ">
              <q-icon name="import_contacts" color="secondary" size="1.3em" class="q-mr-md"></q-icon>
              NovelPXXXXXXXX
              <q-space></q-space>
              <q-btn flat color="secondary">edit</q-btn>
              <q-btn flat color="red">delete</q-btn>
            </div>
          </q-item>
        </div>

      </q-expansion-item>
    </div>
  </div>
</template>

<script>
export default {
  name: "IndexIPs",
  data: () => ({
    model:'',
  }),
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

.bl4
  border: solid
  border-color: $accent
  border-width: 1px
</style>
