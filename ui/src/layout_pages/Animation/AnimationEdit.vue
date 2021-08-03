<template >
    <q-page v-if="initialized" padding class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
        <div class="q-mx-auto" style="width: 97%">
            <div class="row q-col-gutter-x-md justify-center">
                <!--LEFT-->
                <div class="column col-md-3 col-xs-12 q-pb-md">
                    <div>
                        <file-pond
                            name="file_pond_file"
                            ref="verticalPond"
                            class="full-width"
                            :label-idle="label"
                            accepted-file-types="image/jpeg, image/png"
                            :files="animationEditBuffer.verticalImage"
                            :server="animationEditBuffer.server"
                            @init="handleVerticalPondInit"
                            allowImageCrop="true"
                            allowImageTransform="true"
                            imageCropAspectRatio="2:3"
                            stylePanelLayout="compact"
                            credits="false"
                            imagePreviewMaxHeight="9999"
                        />
                    </div>
                    <div>
                        <file-pond
                            name="file_pond_file"
                            ref="horizontalPond"
                            class="full-width"
                            :label-idle="label"
                            accepted-file-types="image/jpeg, image/png"
                            :files="animationEditBuffer.horizontalImage"
                            :server="animationEditBuffer.server"
                            @init="handleHorizontalPondInit"
                            allowImageCrop="true"
                            imageCropAspectRatio="16:9"
                            stylePanelLayout="compact"
                            imagePreviewMaxHeight="9999"
                            credits="false"
                        />
                    </div>
                </div>
                <!--RIGHT-->
                <div class="column col-md-9 col-xs-12 q-pb-md">
                    <!--TITLE-->
                    <div style="width: 100%" class="q-px-md q-pb-md bl">
                        <p class="q-my-none text-primary  text-h4">
                            Edit ANIMATION
                        </p>
                    </div>
                    <!--Fields-->
                    <div style="width: 100%" class="q-pl-md bl">
                        <!--IPName-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">BELONG TO</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    readonly
                                    dense dark bg-color="dark-light" standout=""
                                    v-model="ipNameI18n"
                                >
                                </q-input>
                            </div>
                        </div>
                        <!--Name-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">NAME</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class="bg-dark-light" standout=""
                                    v-model="animationEditBuffer.data.name"
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
                                    v-model="animationEditBuffer.data.reservedNames.cn"
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
                                    v-model="animationEditBuffer.data.reservedNames.en"
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
                                    v-model="animationEditBuffer.data.reservedNames.jp"
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
                                    v-model="animationEditBuffer.data.reservedNames.rm"
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
                                    v-model="animationEditBuffer.data.reservedNames.misc"
                                >
                                </q-input>
                            </div>
                        </div>
                        <q-separator color="grey-7" class="q-my-sm"></q-separator>
                        <!--enintro-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">INTRO-EN</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout="" autogrow
                                    v-model="animationEditBuffer.data.intros.en"
                                >
                                </q-input>
                            </div>
                        </div>
                        <!--cnintro-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">INTRO-CN</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout="" autogrow
                                    v-model="animationEditBuffer.data.intros.cn"
                                >
                                </q-input>
                            </div>
                        </div>
                        <q-separator color="grey-7" class="q-my-sm"></q-separator>
                        <!--producedBy-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">PRODUCED BY</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="animationEditBuffer.data.producedBy"
                                >
                                </q-input>
                            </div>
                        </div>
                        <!--releasedAt-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">RELEASED AT</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    hide-bottom-space
                                    dense dark bg-color="dark-light"  standout=""
                                    v-model="animationEditBuffer.data.releasedAt"
                                    :rules="[v => /(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})/.test(v) || 'wrong time']"
                                >
                                    <template v-slot:prepend>
                                        <q-icon name="event" class="cursor-pointer">
                                            <q-popup-proxy transition-show="scale" transition-hide="scale">
                                                <q-date color="primary" v-model="animationEditBuffer.data.releasedAt" mask="YYYY-MM-DD HH:mm">
                                                    <div class="row items-center justify-end">
                                                        <q-btn v-close-popup label="Close" color="primary" flat />
                                                    </div>
                                                </q-date>
                                            </q-popup-proxy>
                                        </q-icon>
                                    </template>

                                    <template v-slot:append>
                                        <q-icon name="access_time" class="cursor-pointer">
                                            <q-popup-proxy transition-show="scale" transition-hide="scale">
                                                <q-time color="primary" v-model="animationEditBuffer.data.releasedAt" mask="YYYY-MM-DD HH:mm" format24h>
                                                    <div class="row items-center justify-end">
                                                        <q-btn v-close-popup label="Close" color="primary" flat />
                                                    </div>
                                                </q-time>
                                            </q-popup-proxy>
                                        </q-icon>
                                    </template>
                                </q-input>
                            </div>
                        </div>
                        <!--type-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">TYPE</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-select
                                    class="bg-dark-light"
                                    dark
                                    dense
                                    options-dense
                                    options-selected-class="text-accent"
                                    standout=""
                                    v-model="animationEditBuffer.data.type"
                                    hide-bottom-space
                                    :options="typeModels"
                                    emit-value
                                    map-options
                                >
                                </q-select>
                            </div>
                        </div>
                        <!--epnum-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">EPS NUM</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="animationEditBuffer.data.episodesNum"
                                >
                                </q-input>
                            </div>
                        </div>
                        <q-separator color="grey-7" class="q-my-sm"></q-separator>
                        <!--baidu-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">URL-BAIDU</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="animationEditBuffer.data.sharingAddresses.baiduCloud.url"
                                >
                                </q-input>
                            </div>
                        </div>
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">PASSWORD-BAIDU</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="animationEditBuffer.data.sharingAddresses.baiduCloud.password"
                                >
                                </q-input>
                            </div>
                        </div>
                        <q-separator color="grey-7" class="q-my-sm"></q-separator>
                        <!--ali-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">URL-ALI</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="animationEditBuffer.data.sharingAddresses.aliCloud.url"
                                >
                                </q-input>
                            </div>
                        </div>
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">PASSWORD-ALI</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="animationEditBuffer.data.sharingAddresses.aliCloud.password"
                                >
                                </q-input>
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
                                    v-model="animationEditBuffer.data.comment"
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
        </div>
    </q-page>
</template>

<script>

export default {
    name: "AnimationEdit",
    created() {
        if (this.readyToInitialize) this.initPage()
    },
    data() {
        return {
            ip: null,
            label:'Drag & Drop a 16:9 image or <span class=\"filepond--label-action\"> Browse </span>',
            animationEditBuffer: {
                loading: true,
                verticalImage: [],
                horizontalImage: [],
                data:{
                    name: '',
                    reservedNames: {
                        en: '',
                        cn: '',
                        jp: '',
                        rm: '',
                        misc: ''
                    },
                    intros:{
                        en:'',
                        cn:'',
                    },
                    imageIds:{
                        vertical:null,
                        horizontal:null,
                    },
                    producedBy: '',
                    releasedAt: null,
                    writtenBy: '',
                    type: null,
                    episodesNum: null,
                    sharingAddresses: {
                        baiduCloud: {
                            url:'',
                            password:''
                        },
                        aliCloud: {
                            url:'',
                            password:''
                        }
                    },
                    comment:''
                },
                server: {
                    url: '/api',
                    process: '/storage/file/filepond/upload',
                    revert: null,
                    restore: null,
                    load: '/storage/file/filepond/load/',
                    fetch: null
                },
            }
        }
    },
    methods: {
        foo() {},
        initPage() {
            const animationId = this.$route.query.id
            for (const ip of this.ips) {
                for (const animation of ip.animations) {
                    if (animation.id === Number(animationId)) {
                        this.ip=ip
                        this.initAnimationEditBuffer(ip,animation)
                    }
                }
            }
        },
        initAnimationEditBuffer(ip,animation) {
            this.animationEditBuffer.data.id = animation.id
            this.animationEditBuffer.data.name = animation.name
            this.animationEditBuffer.data.reservedNames.en = animation.reservedNames.en
            this.animationEditBuffer.data.reservedNames.cn = animation.reservedNames.cn
            this.animationEditBuffer.data.reservedNames.jp = animation.reservedNames.jp
            this.animationEditBuffer.data.reservedNames.rm = animation.reservedNames.rm
            this.animationEditBuffer.data.reservedNames.misc = animation.reservedNames.misc
            this.animationEditBuffer.data.intros.en = animation.intros.en
            this.animationEditBuffer.data.intros.cn = animation.intros.cn
            this.animationEditBuffer.data.producedBy = animation.producedBy
            this.animationEditBuffer.data.releasedAt = animation.releasedAt
            this.animationEditBuffer.data.type = animation.type
            this.animationEditBuffer.data.episodesNum = animation.episodesNum
            this.animationEditBuffer.data.sharingAddresses.baiduCloud.url = animation.sharingAddresses.baiduCloud.url
            this.animationEditBuffer.data.sharingAddresses.baiduCloud.password = animation.sharingAddresses.baiduCloud.password
            this.animationEditBuffer.data.sharingAddresses.aliCloud.url = animation.sharingAddresses.aliCloud.url
            this.animationEditBuffer.data.sharingAddresses.aliCloud.password = animation.sharingAddresses.baiduCloud.password
            this.animationEditBuffer.data.comment = animation.comment
            this.animationEditBuffer.data.imageIds.vertical = animation.imageIds.vertical
            this.animationEditBuffer.data.imageIds.horizontal = animation.imageIds.horizontal
            this.animationEditBuffer.loading = false
        },
        handleVerticalPondInit(){
            if (this.animationEditBuffer.data.imageIds.vertical!==undefined) {
                this.animationEditBuffer.verticalImage = [{
                    source: this.animationEditBuffer.data.imageIds.vertical,
                    options: {
                        type: 'local'
                    }
                }]
            }
            console.log('VerticalPond has initialized');
        },
        handleHorizontalPondInit(){
            if (this.animationEditBuffer.data.imageIds.horizontal!==undefined) {
                this.animationEditBuffer.horizontalImage = [{
                    source: this.animationEditBuffer.data.imageIds.horizontal,
                    options: {
                        type: 'local'
                    }
                }]
            }
            console.log('HorizontalPond has initialized');
        },
        commitEdit(){
            const verticalImageList = this.$refs.verticalPond.getFiles()
            if (verticalImageList.length === 0) {
                delete this.animationEditBuffer.data.imageIds.vertical
            } else {
                if (verticalImageList[0].status === 5 || verticalImageList[0].status === 2) {
                    this.animationEditBuffer.data.imageIds.vertical = Number(verticalImageList[0].serverId)
                }
            }
            const horizontalImageList = this.$refs.horizontalPond.getFiles()
            if (horizontalImageList.length === 0) {
                delete this.animationEditBuffer.data.imageIds.horizontal
            } else {
                if (horizontalImageList[0].status === 5 || horizontalImageList[0].status === 2) {
                    this.animationEditBuffer.data.imageIds.horizontal = Number(horizontalImageList[0].serverId)
                }
            }
            this.$axios.post('api/animation/edit', this.animationEditBuffer.data).then((response) => {
                let rd = response.data
                if (rd.code === 'success') {
                    this.$q.notify({type: 'success', message: this.$t("messages.success")})
                    this.$store.dispatch('getIPs').then(() => {
                        this.$router.push('/index/ips_and_tags')
                    })
                } else {
                    console.log('post success bug exec fail,error is:')
                    console.log(response)
                    this.$q.notify({type: 'failure', message: this.$t("messages.failure")})
                }
            }).catch((error) => {
                console.log('post fail,error is:')
                console.log(error)
                this.$q.notify({type: 'failure', message: this.$t("messages.failure")})
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
            return !this.animationEditBuffer.loading
        },
        ipNameI18n(){
            return this.ip.reservedNames[this.$i18n.locale] || this.ip.name
        },
        typeModels() {
            return [
                {
                    label: '_i18n_tv',
                    value: 'TV'
                },
                {
                    label: '_i18n_movie',
                    value: 'MOVIE'
                },
                {
                    label: '_i18n_sp',
                    value: 'SP'
                },
                {
                    label: '_i18n_ova',
                    value: 'OVA'
                },
                {
                    label: '_i18n_oad',
                    value: 'OAD'
                },
            ]
        }
    },
    watch: {
        readyToInitialize() {
            console.log('animation/edit:ip_id='+this.$route.query.ip_id)
            if (this.readyToInitialize) {
                this.initPage()
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
