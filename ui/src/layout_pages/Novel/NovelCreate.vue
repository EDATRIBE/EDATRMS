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
                            :server="novelCreateBuffer.server"
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
                            :server="novelCreateBuffer.server"
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
                        <p class="q-my-none text-secondary  text-h4">
                            NEW NOVEL
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
                        <q-separator color="grey-7" class="q-my-sm"></q-separator>
                        <!--Name-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">NAME</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class="bg-dark-light" standout=""
                                    v-model="novelCreateBuffer.data.name"
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
                                    v-model="novelCreateBuffer.data.reservedNames.cn"
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
                                    v-model="novelCreateBuffer.data.reservedNames.en"
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
                                    v-model="novelCreateBuffer.data.reservedNames.jp"
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
                                    v-model="novelCreateBuffer.data.reservedNames.rm"
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
                                    v-model="novelCreateBuffer.data.reservedNames.misc"
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
                                    v-model="novelCreateBuffer.data.intros.en"
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
                                    v-model="novelCreateBuffer.data.intros.cn"
                                >
                                </q-input>
                            </div>
                        </div>
                        <q-separator color="grey-7" class="q-my-sm"></q-separator>
                        <!--VOLUMES-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">VOLUMES NUM</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="novelCreateBuffer.data.volumesNum"
                                >
                                </q-input>
                            </div>
                        </div>
                        <!--integrated-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">INTEGRATED</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-select
                                    class="bg-dark-light"
                                    dark
                                    dense
                                    options-dense
                                    options-selected-class="text-secondary"
                                    standout=""
                                    v-model="novelCreateBuffer.data.integrated"
                                    hide-bottom-space
                                    :options="integratedModels"
                                    emit-value
                                    map-options
                                >
                                </q-select>
                            </div>
                        </div>
                        <q-separator color="grey-7" class="q-my-sm"></q-separator>
                        <!--filename-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">FILE NAME</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="novelCreateBuffer.data.fileMeta.name"
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
                                    options-selected-class="text-secondary"
                                    standout=""
                                    v-model="novelCreateBuffer.data.fileMeta.type"
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
                                    v-model="novelCreateBuffer.data.fileMeta.size"
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
                                    v-model="novelCreateBuffer.data.sharingAddresses.baiduCloud.url"
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
                                    v-model="novelCreateBuffer.data.sharingAddresses.baiduCloud.password"
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
                                    v-model="novelCreateBuffer.data.sharingAddresses.aliCloud.url"
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
                                    v-model="novelCreateBuffer.data.sharingAddresses.aliCloud.password"
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
                                    v-model="novelCreateBuffer.data.comment"
                                >
                                </q-input>
                            </div>
                        </div>
                    </div>

                    <!--Actions-->
                    <div style="width: 100%" class="q-pl-md">
                        <div class="row justify-end q-py-md">
                            <q-btn
                                class="q-ml-md" dense flat color="secondary"
                                @click="$router.go(-1)"
                            >
                                cancel
                            </q-btn>
                            <q-btn
                                class="q-ml-md" dense flat color="secondary"
                                @click="commitCreate"
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
    name: "NovelCreate",
    created() {
        if (this.readyToInitialize) this.selectIP(this.$route.query.ip_id)
    },
    data() {
        return {
            ip: null,
            label:'Drag & Drop a 16:9 image or <span class=\"filepond--label-action\"> Browse </span>',
            novelCreateBuffer: {
                data:{
                    ipId: null,
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
                    volumesNum: null,
                    integrated: null,
                    fileMeta: {
                        name: '',
                        type: '',
                        size: '',
                    },
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
        foo() {
        },
        selectIP(id) {
            for (const ip of this.ips) {
                if (ip.id === Number(id)){
                    this.ip=ip
                }
            }
        },
        commitCreate(){
            this.novelCreateBuffer.data.ipId = this.ip.id
            const verticalImageList = this.$refs.verticalPond.getFiles()
            if (verticalImageList.length === 0) {
                delete this.novelCreateBuffer.data.imageIds.vertical
            } else {
                if (verticalImageList[0].status === 5 || verticalImageList[0].status === 2) {
                    this.novelCreateBuffer.data.imageIds.vertical = Number(verticalImageList[0].serverId)
                }
            }
            const horizontalImageList = this.$refs.horizontalPond.getFiles()
            if (horizontalImageList.length === 0) {
                delete this.novelCreateBuffer.data.imageIds.horizontal
            } else {
                if (horizontalImageList[0].status === 5 || horizontalImageList[0].status === 2) {
                    this.novelCreateBuffer.data.imageIds.horizontal = Number(horizontalImageList[0].serverId)
                }
            }
            this.$axios.post('api/novel/create', this.novelCreateBuffer.data).then((response) => {
                let rd = response.data
                if (rd.code === 'success') {
                    this.$q.notify({type: 'success', message: this.$t("messages.success")})
                    this.$store.dispatch('getIPs').then(() => {
                        this.$router.push('/index/ips_and_tags')
                    })
                } else {
                    console.log('post success but exec fail,error is:')
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
            return this.ip!==null
        },
        ipNameI18n(){
            return this.ip.reservedNames[this.$i18n.locale] || this.ip.name
        },
        integratedModels() {
            return [
                {
                    label: '_i18n_TRUE',
                    value: true
                },
                {
                    label: '_i18n_FALSE',
                    value: false
                }
            ]
        },
        typeModels() {
            return [
                {
                    label: 'TXT',
                    value: 'TXT'
                },
                {
                    label: 'PDF',
                    value: 'PDF'
                },
                {
                    label: 'EPUB',
                    value: 'EPUB'
                }
            ]
        }
    },
    watch: {
        readyToInitialize() {
            console.log('novel/create:ip_id='+this.$route.query.ip_id)
            if (this.readyToInitialize) {
                this.selectIP(this.$route.query.ip_id)
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
</style>
