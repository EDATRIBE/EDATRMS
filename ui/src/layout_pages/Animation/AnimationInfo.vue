<template>
    <q-page v-if="initialized" padding class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
        <div class="q-mx-auto " style="width: 97%; border-radius: 0px">
            <div class="row q-col-gutter-x-md justify-center">
                <!--LEFT-->
                <div class="column col-md-3 col-xs-12">
                    <q-img
                        class="shadow-2 q-mb-md"
                        style="border-radius: 4px"
                        :src="animation.images.vertical.url"
                        v-if="animation.images.vertical!==undefined"
                    />
                    <q-btn dense class="q-mb-md shadow-2" color="primary" text-color="white">
                        REPORT A PROBLEM
                        <q-icon class="q-pl-sm" name="construction" size="1.5em"/>
                    </q-btn>
                </div>
                <!--RIGHT-->
                <div class="column col-md-9 col-xs-12 q-pb-md">
                    <!--TITLE-->
                    <div style="width: 100%" class="q-px-md q-pb-md bl">
                        <p class="q-my-none text-primary  text-h4">
                            {{ animation.reservedNames[$i18n.locale] || animation.name }}
                        </p>
                    </div>
                    <!--INFOS-->
                    <div style="width: 100%" class="q-px-md q-pt-md bl">
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <q-icon color="primary" name="fas fa-info-circle" size="2.5em"></q-icon>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-primary  text-h4"></p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 30%"/>
                        <div class="row q-py-md ">
                            <div class="col-md-2 col-xs-12"><p
                                class="q-my-none text-grey text-body1 text-weight-medium">INTRO</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1 text-justify">
                                    {{ animation.intros[$i18n.locale] }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12"><p
                                class="q-my-none text-grey text-body1 text-weight-medium">TYPE</p>
                            </div>
                            <div class="col-md-10 col-xs-12"><p class="q-my-none text-white text-body1">
                                {{ animation.type }}</p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12"><p
                                class="q-my-none text-grey text-body1 text-weight-medium">EPS NUM</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ animation.episodesNum }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">
                                    PRODUCED BY
                                </p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ animation.producedBy }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">
                                    WRITTEN BY
                                </p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ animation.writtenBy }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">
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
                    <div style="width: 100%" class="q-px-md q-pt-md bl" v-for="(video,i) in animation.videos"
                         :key="'video'+i">
                        <div class="row q-py-md ">
                            <div class="col-md-2 col-xs-12">
                                <q-icon color="primary" name="fas fa-film" size="2.5em"></q-icon>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-white text-h4"></p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12"><p
                                class="q-my-none text-grey text-body1 text-weight-medium">TYPE</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ video.fileMeta.type }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"/>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12"><p
                                class="q-my-none text-grey text-body1 text-weight-medium">SIZE</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ video.fileMeta.size }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"/>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12"><p
                                class="q-my-none text-grey text-body1 text-weight-medium">QUALITY</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ video.fileMeta.quality }}
                                </p>
                            </div>
                        </div>
                    </div>
                    <!--CPATIONS-->
                    <div style="width: 100%" class="q-px-md q-pt-md bl" v-for="(caption,i) in animation.captions"
                         :key="'caption'+i">
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <q-icon color="primary" name="fas fa-closed-captioning" size="2.7em"></q-icon>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-white text-h2"></p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"/>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">TYPE</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ caption.fileMeta.type }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">
                                    SIZE
                                </p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ caption.fileMeta.size }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">
                                    INTEGRATED
                                </p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ caption.integrated }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">
                                    STATE
                                </p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ caption.state }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">
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
                    <div style="width: 100%" class="q-px-md q-pt-md bl">
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <q-icon color="primary" name="cloud_download" size="2.7em"></q-icon>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-white text-h2"></p>
                            </div>
                        </div>
                        <div
                            v-if="animation.sharingAddresses.aliCloud !== undefined &&
                             animation.sharingAddresses.aliCloud.url!==''"
                        >
                            <q-separator color="grey" style="opacity: 20%"/>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-grey text-body1 text-weight-medium">
                                        ALI CLOUD
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12 row">
                                    <div class="q-mr-lg">
                                        <a :href="animation.sharingAddresses.aliCloud.url">
                                            <p class="q-my-none text-primary text-body1">
                                                {{ animation.sharingAddresses.aliCloud.password }}
                                            </p>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div
                            v-if="animation.sharingAddresses.baiduCloud !== undefined &&
                             animation.sharingAddresses.baiduCloud.url!==''"
                        >
                            <q-separator color="grey" style="opacity: 20%"/>
                            <div class="row q-py-md">
                                <div class="col-md-2 col-xs-12">
                                    <p class="q-my-none text-grey text-body1 text-weight-medium">
                                        BAIDU CLOUD
                                    </p>
                                </div>
                                <div class="col-md-10 col-xs-12 row">
                                    <div class="q-mr-lg">
                                        <a :href="animation.sharingAddresses.baiduCloud.url">
                                            <p class="q-my-none text-primary text-body1">
                                                {{ animation.sharingAddresses.baiduCloud.password }}
                                            </p>
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
        foo() {
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
        initialized() {
            return this.animation !== null
        },
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
</style>
