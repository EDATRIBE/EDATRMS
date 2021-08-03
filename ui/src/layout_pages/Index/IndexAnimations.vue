<template>
    <div class="q-pt-sm">

        <!--Tools-->
        <div @mouseleave="expanded=false">
            <q-expansion-item
                v-model="expanded"
                dense
                dark
                expand-icon-toggle
                class="q-mb-sm "
                header-class="bl q-pa-none "
                expand-icon-class="q-pr-sm text-primary"
                expand-icon="filter_alt"
                expanded-icon="filter_alt"
            >
                <!--ToolsHeader-->
                <template v-slot:header>
                    <div class="row items-center text-body1 full-width ">
                        <q-btn-toggle
                            text-color="grey-7" size="0.75em" unelevated
                            class="no-border-radius bg-dark-light" toggle-color="primary" toggle-text-color="dark"
                            v-model="order"
                            :options="[
                              {label:'date', icon: 'fas fa-sort-numeric-down-alt', value: 'date'},
                              {label:'alphabet', icon: 'fas fa-sort-alpha-down', value: 'alphabet'}
                            ]"
                        />
                    </div>
                </template>
                <!--ToolsContent-->
                <div class="q-pt-sm q-pb-sm bb">
                    <!--region-->
                    <q-item dense dark class="q-pa-none bl1">
                        <multiple-choice
                            class="text-body1"
                            :options="[
                                {label:'All', value: 'all'},
                                {label:'CN', value: 'cn'},
                                {label:'JP', value: 'jp'},
                                {label:'OTHER', value: 'other'},
                            ]"
                            v-model="region"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>

                    <!--type-->
                    <q-item dense dark class="q-pa-none bl1 q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="[
                                {label:'ALL',value: 'all'},
                                {label:'TV',value: 'tv'},
                                {label:'EPS',  value: 'eps'}
                            ]"
                            v-model="type"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>

                    <!--date-->
                    <q-item dense dark class="q-pa-none bl1 q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="[
                {label:'ALL',value: 'all'},
                {label:'1960s', value: '1960s'},
                {label:'1970s', value: '1970s'},
                {label:'1980s', value: '1980s'},
                {label:'1990s', value: '1990s'},
                {label:'2000s', value: '2000s'},
                {label:'2010s', value: '2010s'},
                {label:'2020s', value: '2020s'}
              ]"
                            v-model="date"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>

                    <!--quality-->
                    <q-item dense dark class="q-pa-none bl1 q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="[
                {label:'ALL',value: 'all'},
                {label:'360P', value: '360P'},
                {label:'640P', value: '640P'},
                {label:'720P', value: '720P'},
                {label:'960P', value: '960P'},
                {label:'1080P', value: '1080P'}
              ]"
                            v-model="quality"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>

                    <!--videoType-->
                    <q-item dense dark class="q-pa-none bl1 q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="[
                {label:'ALL',value: 'all'},
                {label:'MP4', value: '360P'},
                {label:'MKV', value: '640P'},
                {label:'AV1', value: '720P'},
                {label:'OGG', value: '960P'}
              ]"
                            v-model="videoType"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>

                    <!--captions-->
                    <q-item dense dark class="q-pa-none bl1 q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="[
                {label:'ALL',value: 'all'},
                {label:'CLOSED CAPTION', value: 'true'},
                {label:'NO CAPTION', value: 'false'},
              ]"
                            v-model="hasCaption"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>
                </div>
            </q-expansion-item>
        </div>

        <!--Content-->
        <div class="row q-col-gutter-x-sm q-col-gutter-y-md">
            <div class="col-md-2 col-sm-3 col-xs-6" v-for="i in 20" :key="i">
                <q-card class="bg-dark cursor-pointer" flat  @click="()=>{}">
                    <q-img :src="require('assets/aaa.jpg')" class="my-img" native-context-menu>
                        <div class="absolute-full text-subtitle2 flex flex-center my-text">
                            <q-icon size="4em" name="fas fa-link"></q-icon>
                        </div>
                        <q-chip
                            dense
                            class="absolute q-ma-none text-weight-medium" color="primary"
                            style="right: 0px; top:0px;  opacity: .9; border-radius: 0px 0px 0px 6px;">
                            {{i%2?'EPS':'MOVIE'}}
                        </q-chip>
                    </q-img>
                    <q-card-section class="q-pa-none text-white text-body1 text-weight-bold ov">
                        {{ lorem[i%2] }}
                    </q-card-section>
                </q-card>
            </div>
        </div>
    </div>
</template>

<script>
import MultipleChoice from "components/MultipleChoice";

export default {
    name: "IndexAnimations",
    components: {MultipleChoice},
    data() {
        return {
            tab: 'Animations',
            text: '',
            LD: true,
            expanded: false,
            scrollInfo: {},
            soo: false,
            order: 'date',
            region: 'all',
            type: 'all',
            date: 'all',
            quality: 'all',
            videoType: 'all',
            hasCaption: 'all',
            ips: [],
            lorem: ['Lorem ipsum dolor sit','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec est ligula. Curabitur porta nibh quis convallis elementum. Praesent laoreet, lacus at tristique pretium, nisl metus luctus nibh, vel accumsan ante sapien eget ante. Nunc neque metus, iaculis ut velit at, facilisis posuere urna. Curabitur tempor quis felis commodo interdum. Ut tempus ullamcorper ipsum. Donec egestas, enim sed accumsan efficitur, elit diam feugiat nunc, in pellentesque risus nulla ut felis. Nulla facilisi. Etiam sagittis consectetur urna, ac consectetur nisi hendrerit in. Aliquam eu purus mollis, commodo ipsum at, vestibulum nisi. Etiam et suscipit justo. Fusce at mauris at lectus bibendum porta in imperdiet leo.']
        }
    },
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
    white-space: initial
    visibility: visible

.bb
    border-bottom: solid
    border-bottom-color: $primary
    border-width: 2px

.bt
    border-top: solid
    border-top-color: $primary
    border-top-width: 2px

.my-img .my-text
    visibility: hidden
    opacity: 0
    transition: .3s
.my-img:hover .my-text
    visibility: visible
    opacity: 1
    transition: .3s

//.my-img .my-text
//    visibility: hidden
//    opacity: 0
//
//.my-img:hover .my-text
//    visibility: visible
//    opacity: 1
//
//    animation: 1s forwards
//    animation-name: flipInX
//    -webkit-animation-name: flipInX

</style>
