<template>
    <div>
        <div v-if="showBgImage" :style="{'--bgImageUrl':'url('+bgImageUrl+')'}" class="my-background-img"/>
        <q-page v-if="initialized" padding class="q-px-md q-pb-xl" style="padding-top: 3.5em">
            <div class="q-mx-auto " style="width: 97%; border-radius: 0px">
                <div class="row q-col-gutter-x-md justify-center">
                    <!--LEFT-->
                    <div class="column col-md-3 col-xs-12">
                        <q-img
                            class="q-mb-sm"
                            style="border-radius: 4px"
                            :src="novel.images.vertical?
                                    novel.images.vertical.url:
                                    require('src/assets/placeholder.jpg')"
                        />
                        <q-btn dense class="q-mb-sm" color="secondary" text-color="white">
                            REPORT A PROBLEM
                            <q-icon class="q-pl-sm" name="construction" size="1.5em"/>
                        </q-btn>
                    </div>
                    <!--RIGHT-->
                    <div class="column col-md-9 col-xs-12 q-pb-md">
                        <!--TITLE-->
                        <div style="width: 100%" class="q-px-md q-py-md ">
                            <p class="q-my-none text-white text-h3">
                                {{ novel.reservedNames[$i18n.locale] || novel.name }}
                            </p>
                        </div>
                        <!--INFOS-->
                        <div style="width: 100%" class="q-px-md q-pt-md ">
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <q-icon
                                        color="white"
                                        name="fas fa-info-circle"
                                        class="my-opacity-70"
                                        size="2.5em"
                                    />
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-secondary  text-h4"></p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"/>
                            <div class="row q-py-md ">
                                <div class="col-md-2 col-xs-12"><p
                                    class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">INTRO</p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1 text-justify">
                                        {{ novel.intros[$i18n.locale] }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"/>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                        WRITTEN BY
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ novel.writtenBy }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"/>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12"><p
                                    class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">VOLUMES NUM</p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ novel.volumesNum }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"/>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                        INTEGRATED
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ novel.integrated }}
                                    </p>
                                </div>
                            </div>
                        </div>
                        <!--File-->
                        <div style="width: 100%" class="q-px-md q-pt-md ">
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <q-icon
                                        color="white"
                                        name="fas fa-file-alt"
                                        size="2.5em"
                                        class="my-opacity-70"
                                    />
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-secondary  text-h4"></p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"/>
                            <div class="row q-py-md ">
                                <div class="col-md-2 col-xs-12"><p
                                    class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">FORMAT</p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1 text-justify">
                                        {{ novel.fileMeta.type }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"/>
                            <div class="row q-py-md ">
                                <div class="col-md-2 col-xs-12"><p
                                    class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">SIZE</p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1 text-justify">
                                        {{ novel.fileMeta.size }}
                                    </p>
                                </div>
                            </div>
                        </div>
                        <!--Address-->
                        <div style="width: 100%" class="q-px-md q-pt-md">
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <q-icon
                                        color="white"
                                        name="cloud_download"
                                        size="2.7em"
                                        class="my-opacity-70"
                                    />
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-white text-h2"></p>
                                </div>
                            </div>
                            <div
                                v-if="novel.sharingAddresses.aliCloud !== undefined &&
                             novel.sharingAddresses.aliCloud.url!==''"
                            >
                                <q-separator class="bg-white my-opacity-20"/>
                                <div class="row q-py-md">
                                    <div class="col-md-2 col-xs-12">
                                        <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                            ALI CLOUD
                                        </p>
                                    </div>
                                    <div class="col-md-10 col-xs-12 row">
                                        <div class="q-mr-lg">
                                            <a :href="novel.sharingAddresses.aliCloud.url" class=" row items-center">
                                                <p class="q-my-none text-secondary text-body1">
                                                    {{ novel.sharingAddresses.aliCloud.password }}
                                                </p>
                                                <q-icon name="fas fa-link" size="0.75em" color="secondary" class="q-mx-sm"/>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div
                                v-if="novel.sharingAddresses.baiduCloud !== undefined &&
                             novel.sharingAddresses.baiduCloud.url!==''"
                            >
                                <q-separator class="bg-white my-opacity-20"/>
                                <div class="row q-py-md">
                                    <div class="col-md-2 col-xs-12">
                                        <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                            BAIDU CLOUD
                                        </p>
                                    </div>
                                    <div class="col-md-10 col-xs-12 row">
                                        <div class="q-mr-lg">
                                            <a :href="novel.sharingAddresses.baiduCloud.url" class=" row items-center">
                                                <p class="q-my-none text-secondary text-body1">
                                                    {{ novel.sharingAddresses.baiduCloud.password }}
                                                </p>
                                                <q-icon name="fas fa-link" size="0.75em" color="secondary" class="q-mx-sm"/>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </q-page>
    </div>
</template>

<script>

export default {
    name: "NovelInfo",
    created() {
        if (this.readyToInitialize) this.selectNovel(this.$route.query.id)
    },
    data() {
        return {
            novel: null,
        }
    },
    methods: {
        foo() {
        },
        selectNovel(id) {
            for (const ip of this.ips) {
                for (const novel of ip.novels) {
                    if (novel.id === Number(id)) {
                        this.novel = novel
                        this.novel.region = ip.region
                        this.novel.writtenBy = ip.writtenBy
                    }
                }
            }
        }
    },
    computed: {
        readyToInitialize() {
            return this.$store.getters.ipsInitialized
        },
        ips() {
            return this.$store.state.ip.ips
        },
        initialized() {
            return this.novel !== null
        },
        showBgImage(){
            if(!this.initialized){
                return false
            }else {
                return this.novel.images.horizontal !== null && this.novel.images.horizontal !==undefined
            }
        },
        bgImageUrl(){
            if(!this.showBgImage){
                return null
            }else {
                return this.novel.images.horizontal.url
            }
        }
    },
    watch: {
        readyToInitialize() {
            if (this.readyToInitialize) {
                this.selectNovel(this.$route.query.id)
            }
        },

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
    border-left-color: $secondary
    border-width: 3px

.my-background-img
    position: absolute
    top: 0px
    width: 100%
    z-index: -1
    padding-top: 60%
    background-position-x: 50%
    background-repeat: no-repeat
    background-size: cover
    background-image: linear-gradient(to top, rgb(38, 38, 45), rgba(38, 38, 45, 0.4) 70%, rgba(38, 38, 45, 0.2)), var(--bgImageUrl)
</style>
