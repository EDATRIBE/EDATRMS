<template>
    <q-page padding class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em" v-if="initialized">
        <div class="q-mx-auto" style="width: 97%">
            <div class="column full-width">

                <!--Title-->
                <div style="width: 100%" class="q-pl-md bl">
                    <div class="row q-pb-md">
                        <p class="q-my-none text-primary text-h4 ">EDIT VIDEO</p>
                    </div>
                </div>

                <!--Fields-->
                <div style="width: 100%" class="q-pl-md bl">
                    <!--animationName-->
                    <div class="row items-center q-py-sm">
                        <div class="col-md-2 col-xs-12">
                            <p class="q-my-none text-grey text-body1 text-weight-medium">BELONG TO</p>
                        </div>
                        <div class="col-md-10 col-xs-12">
                            <q-input
                                readonly
                                dense dark bg-color="dark-light" standout=""
                                v-model="animationNameI18n"
                            >
                            </q-input>
                        </div>
                    </div>
                    <q-separator color="grey-7" class="q-my-sm"></q-separator>
                    <!--Name-->
                    <div class="row items-center q-py-sm">
                        <div class="col-md-2 col-xs-12">
                            <p class="q-my-none text-grey text-body1 text-weight-medium">FILE NAME</p>
                        </div>
                        <div class="col-md-10 col-xs-12">
                            <q-input
                                dense dark class="bg-dark-light" standout=""
                                v-model="videoEditBuffer.data.fileMeta.name"
                            >
                            </q-input>
                        </div>
                    </div>
                    <!--type-->
                    <div class="row items-center q-py-sm">
                        <div class="col-md-2 col-xs-12">
                            <p class="q-my-none text-grey text-body1 text-weight-medium">FILE TYPE</p>
                        </div>
                        <div class="col-md-10 col-xs-12">
                            <q-select
                                class="bg-dark-light"
                                dark
                                dense
                                options-dense
                                options-selected-class="text-primary"
                                standout=""
                                v-model="videoEditBuffer.data.fileMeta.type"
                                hide-bottom-space
                                :options="typeModels"
                                emit-value
                                map-options
                            >
                            </q-select>
                        </div>
                    </div>
                    <!--size-->
                    <div class="row items-center q-py-sm">
                        <div class="col-md-2 col-xs-12">
                            <p class="q-my-none text-grey text-body1 text-weight-medium">FILE SIZE</p>
                        </div>
                        <div class="col-md-10 col-xs-12">
                            <q-input
                                dense dark class="bg-dark-light" standout=""
                                v-model="videoEditBuffer.data.fileMeta.size"
                            >
                            </q-input>
                        </div>
                    </div>
                    <!--qualtiy-->
                    <div class="row items-center q-py-sm">
                        <div class="col-md-2 col-xs-12">
                            <p class="q-my-none text-grey text-body1 text-weight-medium">FILE QUALITY</p>
                        </div>
                        <div class="col-md-10 col-xs-12">
                            <q-select
                                class="bg-dark-light"
                                dark
                                dense
                                options-dense
                                options-selected-class="text-primary"
                                standout=""
                                v-model="videoEditBuffer.data.fileMeta.quality"
                                hide-bottom-space
                                :options="qualityModels"
                                emit-value
                                map-options
                            >
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
                                v-model="videoEditBuffer.data.comment"
                            >
                            </q-input>
                        </div>
                    </div>
                </div>
                <!--Actions-->
                <div style="width: 100%" class="q-pl-md">
                    <div class="row justify-end q-py-md">
                        <q-btn
                            class="q-ml-md" dense flat color="primary"
                            @click="$router.go(-1)"
                        >
                            cancel
                        </q-btn>
                        <q-btn
                            class="q-ml-md" dense flat color="primary"
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
    name: "videoEdit",
    created() {
        if (this.readyToInitialize) this.initBuffer(this.$route.query.video_id)
    },
    data() {
        return {
            animation: null,
            videoEditBuffer: {
                data:{
                    animationId: null,
                    fileMeta: {
                        name: '',
                        type: '',
                        size: ''
                    },
                    comment:''
                }
            }
        }
    },
    methods: {
        foo() {
        },
        initBuffer(videoId) {
            for (const ip of this.ips) {
                for (const animation of ip.animations) {
                    for (const video of animation.videos) {
                        if (video.id === Number(videoId)){
                            this.animation = animation
                            this.initVideoEditBuffer(video)
                        }
                    }
                }
            }
        },
        initVideoEditBuffer(video) {
            this.videoEditBuffer.data.id = video.id
            this.videoEditBuffer.data.fileMeta.name = video.fileMeta.name
            this.videoEditBuffer.data.fileMeta.type = video.fileMeta.type
            this.videoEditBuffer.data.fileMeta.size = video.fileMeta.size
            this.videoEditBuffer.data.fileMeta.quality = video.fileMeta.quality
            this.videoEditBuffer.data.comment = video.comment
            this.videoEditBuffer.loading = false
        },
        commitEdit() {
            this.videoEditBuffer.data.animationId = this.animation.id
            this.$axios.post('api/video/edit', this.videoEditBuffer.data).then((response) => {
                let rd = response.data
                if (rd.code === 'success') {
                    this.$q.notify({type: 'success', message: this.$t("messages.success")})
                    this.$store.dispatch('getIPs').then(() => {
                        this.$router.push('/index/ips_and_tags')
                    })
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
        readyToInitialize() {
            return this.$store.getters.ipsInitialized
        },
        ips() {
            return this.$store.state.ip.ips
        },
        initialized(){
            return this.animation!==null
        },
        animationNameI18n(){
            return this.animation.reservedNames[this.$i18n.locale] || this.animation.name
        },
        typeModels() {
            return [
                {
                    label: 'MP4',
                    value: 'MP4'
                },
                {
                    label: 'MKV',
                    value: 'MKV'
                },
                {
                    label: 'AV1',
                    value: 'AV1'
                },
                {
                    label: 'OGG',
                    value: 'OGG'
                }
            ]
        },
        qualityModels() {
            return [
                {
                    label: '1080P',
                    value: '1080P'
                },
                {
                    label: '960P',
                    value: '960P'
                },
                {
                    label: '720P',
                    value: '720P'
                },
                {
                    label: '640P',
                    value: '640P'
                },
                {
                    label: '360p',
                    value: '360p'
                },
            ]
        }
    },
    watch: {
        readyToInitialize() {
            if (this.readyToInitialize) {
                console.log('readyToInitialize,this.ips:')
                console.log(this.ips)
                this.initBuffer(this.$route.query.video_id)
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
    border-left-color: $primary
    border-width: 3px
</style>
