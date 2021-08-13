<template>
    <div>
        <div v-if="showBgImage" :style="{'--bgImageUrl':'url('+bgImageUrl+')'}" class="my-background-img"/>
        <q-page v-if="initialized" padding class="q-px-md q-pb-xl" style="padding-top: 3.5em; ">
            <div class="q-mx-auto" style="width: 97%; border-radius: 0px">
                <div class="row q-col-gutter-x-md justify-center">
                    <!--LEFT-->
                    <div class="column col-md-3 col-xs-12">
                        <q-img
                            class="q-mb-sm"
                            style="border-radius: 4px; min-height: 450px"
                            :src="animation.images.vertical?
                                    animation.images.vertical.url:
                                    require('src/assets/placeholder.jpg')"
                        >
                            <template v-slot:error>
                                <div class="absolute-full flex flex-center bg-white text-primary" style="z-index: 1">
                                    Cannot load image !
                                </div>
                            </template>
                        </q-img>
                        <q-btn dense class="q-mb-sm" color="primary" text-color="white">
                            REPORT A PROBLEM
                            <q-icon class="q-pl-sm" name="construction" size="1.5em"/>
                        </q-btn>
                    </div>
                    <!--RIGHT-->
                    <div class="column col-md-9 col-xs-12 q-pb-md">
                        <!--TITLE-->
                        <div style="width: 100%" class="q-px-md q-py-md">
                            <p class="q-my-none text-white text-h3">
                                {{ animation.reservedNames[$i18n.locale] || animation.name }}
                            </p>
                        </div>
                        <!--INFOS-->
                        <div style="width: 100%" class="q-px-md q-pt-md">
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
                                    <p class="q-my-none text-primary  text-h4"></p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"/>
                            <div class="row q-py-md ">
                                <div class="col-md-2 col-xs-12"><p
                                    class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">INTRO</p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1 text-justify">
                                        {{ animation.intros[$i18n.locale] }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12"><p
                                    class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">TYPE</p>
                                </div>
                                <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">
                                    {{ animation.type }}</p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12"><p
                                    class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">EPS NUM</p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ animation.episodesNum }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                        PRODUCED BY
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ animation.producedBy }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                        WRITTEN BY
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ animation.writtenBy }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                        RELEASED AT
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ animation.releasedAt }}
                                    </p>
                                </div>
                            </div>
                        </div>
                        <!--VIDEOS-->
                        <div style="width: 100%" class="q-px-md q-pt-md" v-for="(video,i) in animation.videos"
                             :key="'video'+i">
                            <div class="row q-py-md ">
                                <div class="col-md-2 col-xs-12">
                                    <q-icon color="grey" name="fas fa-film" size="2.5em"></q-icon>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-white text-h4"></p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12"><p
                                    class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">TYPE</p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ video.fileMeta.type }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"/>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12"><p
                                    class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">SIZE</p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ video.fileMeta.size }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"/>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12"><p
                                    class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">QUALITY</p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ video.fileMeta.quality }}
                                    </p>
                                </div>
                            </div>
                        </div>
                        <!--CPATIONS-->
                        <div style="width: 100%" class="q-px-md q-pt-md" v-for="(caption,i) in animation.captions"
                             :key="'caption'+i">
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <q-icon color="grey" name="fas fa-closed-captioning" size="2.7em"></q-icon>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-white text-h2"></p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"/>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">TYPE</p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ caption.fileMeta.type }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                        SIZE
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ caption.fileMeta.size }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                        INTEGRATED
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ caption.integrated }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                        STATE
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ caption.state }}
                                    </p>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md items-center">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                        CONTRIBUTORS
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12 row">
                                    <q-chip
                                        clickable
                                        square dense text-color="dark" color="primary"
                                        class="q-py-none q-ml-none q-mr-sm text-weight-medium"
                                        v-for="(userId,i) in caption.userIds" :key="'userid'+i"
                                        @click="$router.push({path:'/contributor/info',query:{user_id:userId}})"
                                    >
                                        {{ usersDict[userId]['name'] }}
                                    </q-chip>
                                </div>
                            </div>
                            <q-separator class="bg-white my-opacity-20"></q-separator>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                        RELEASED AT
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-body1">
                                        {{ caption.releasedAt }}
                                    </p>
                                </div>
                            </div>

                        </div>
                        <!--Address-->
                        <div style="width: 100%" class="q-px-md q-pt-md">
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <q-icon color="grey" name="cloud_download" size="2.7em"></q-icon>
                                </div>
                                <div class="col-md-10 col-xs-12">
                                    <p class="q-my-none text-white text-white text-h2"></p>
                                </div>
                            </div>
                            <div
                                v-if="animation.sharingAddresses.aliCloud !== undefined &&
                                            animation.sharingAddresses.aliCloud.url!==''"
                            >
                                <q-separator class="bg-white my-opacity-20"/>
                                <div class="row q-py-md">
                                    <div class="col-md-2 col-xs-12">
                                        <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                            ALI CLOUD
                                        </p>
                                    </div>
                                    <div class="col-md-10 col-xs-12">
                                        <div
                                            class="q-mr-lg row items-center cursor-pointer"
                                            @click="openLink(animation.sharingAddresses.aliCloud.url)"
                                        >
                                                <p class="q-my-none text-primary text-body1">
                                                    {{ animation.sharingAddresses.aliCloud.password }}
                                                </p>
                                                <q-icon name="fas fa-link" size="0.75em" color="primary" class="q-mx-sm"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div
                                v-if="animation.sharingAddresses.baiduCloud !== undefined &&
                                            animation.sharingAddresses.baiduCloud.url!==''"
                            >
                                <q-separator class="bg-white my-opacity-20"/>
                                <div class="row q-py-md">
                                    <div class="col-md-2 col-xs-12">
                                        <p class="q-my-none text-white my-opacity-70 text-body1 text-weight-medium">
                                            BAIDU CLOUD
                                        </p>
                                    </div>
                                    <div class="col-md-10 col-xs-12">
                                        <div
                                            class="q-mr-lg row items-center cursor-pointer"
                                            @click="openLink(animation.sharingAddresses.baiduCloud.url)"
                                        >
                                            <p class="q-my-none text-primary text-body1">
                                                {{ animation.sharingAddresses.baiduCloud.password }}
                                            </p>
                                            <q-icon name="fas fa-link" size="0.75em" color="primary" class="q-mx-sm"/>
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
    name: "AnimationInfo",
    created() {
        if (this.readyToInitialize) this.selectAnimation(this.$route.query.id)
    },
    data() {
        return {
            animation: null,
        }
    },
    methods: {
        foo(url) {
            window.open(url,'_blank')
        },
        openLink(url){
            window.open(url,'_blank')
        },
        selectAnimation(id) {
            for (const ip of this.ips) {
                for (const animation of ip.animations) {
                    if (animation.id === Number(id)) {
                        this.animation = animation
                        this.animation.region = ip.region
                        this.animation.writtenBy = ip.writtenBy
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
        usersDict() {
            return this.$store.getters.idUserDict
        },
        initialized() {
            return this.animation !== null
        },
        showBgImage() {
            if (!this.initialized) {
                return false
            } else {
                return this.animation.images.horizontal !== null && this.animation.images.horizontal !== undefined
            }
        },
        bgImageUrl() {
            if (!this.showBgImage) {
                return null
            } else {
                return this.animation.images.horizontal.url
            }
        }
    },
    watch: {
        readyToInitialize() {
            if (this.readyToInitialize) {
                this.selectAnimation(this.$route.query.id)
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
    border-left-color: $primary
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
    background-repeat: no-repeat
    background-image: linear-gradient(to top, rgb(38, 38, 45), rgba(38, 38, 45, 0.4) 70%, rgba(38, 38, 45, 0.2)), var(--bgImageUrl)
</style>
