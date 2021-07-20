<template >
    <q-page v-if="initialized" padding class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
        <div class="q-mx-auto" style="width: 95%">
            <div class="row q-col-gutter-x-lg justify-center">
                <!--LEFT-->
                <div class="column col-md-3 col-xs-12 q-pb-md">
                    <div>
                        <file-pond
                            name="file_pond_file"
                            ref="pond"
                            class="full-width"
                            :label-idle="label"
                            accepted-file-types="image/jpeg, image/png"
                            :files="animationCreateBuffer.avatarFile"
                            :server="animationCreateBuffer.server"
                            @init="handleFilePondInit"
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
                            ref="pond"
                            class="full-width"
                            :label-idle="label"
                            accepted-file-types="image/jpeg, image/png"
                            :files="animationCreateBuffer.avatarFile"
                            :server="animationCreateBuffer.server"
                            @init="handleFilePondInit"
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
                            NEW ANIMATION
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
                                    v-model="ipmodel"
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
                                    v-model="animationCreateBuffer.data.name"
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
                                    v-model="animationCreateBuffer.data.reservedNames.cn"
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
                                    v-model="animationCreateBuffer.data.reservedNames.en"
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
                                    v-model="animationCreateBuffer.data.reservedNames.jp"
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
                                    v-model="animationCreateBuffer.data.reservedNames.rm"
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
                                    v-model="animationCreateBuffer.data.reservedNames.misc"
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
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="animationCreateBuffer.data.intros.en"
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
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="animationCreateBuffer.data.intros.cn"
                                >
                                </q-input>
                            </div>
                        </div>
                        <q-separator color="grey-7" class="q-my-sm"></q-separator>
                        <!--cnintro-->
                        <div class="row items-center q-py-sm">
                            <div class="col-md-2 col-xs-12">
                                <p class="q-my-none text-grey text-body1 text-weight-medium">INTRO-CN</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <q-input
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="animationCreateBuffer.data.intros.cn"
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
                                    v-model="animationCreateBuffer.data.producedBy"
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
                                    v-model="animationCreateBuffer.data.releasedAt"
                                    :rules="[v => /(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})/.test(v) || 'wrong time']"
                                >
                                    <template v-slot:prepend>
                                        <q-icon name="event" class="cursor-pointer">
                                            <q-popup-proxy transition-show="scale" transition-hide="scale">
                                                <q-date color="primary" v-model="animationCreateBuffer.data.releasedAt" mask="YYYY-MM-DD HH:mm">
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
                                                <q-time color="primary" v-model="animationCreateBuffer.data.releasedAt" mask="YYYY-MM-DD HH:mm" format24h>
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
                                <q-input
                                    dense dark class=" bg-dark-light" standout=""
                                    v-model="animationCreateBuffer.data.type"
                                >
                                </q-input>
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
                                    v-model="animationCreateBuffer.data.episodesNum"
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
                                    v-model="animationCreateBuffer.data.comment"
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
// Import FilePond
import vueFilePond from 'vue-filepond';

// Import styles
import 'filepond/dist/filepond.min.css';
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css'
// Import the plugin code
import FilePondPluginImageCrop from 'filepond-plugin-image-crop';
import FilePondPluginImageExifOrientation from 'filepond-plugin-image-exif-orientation'
import FilePondPluginImagePreview from 'filepond-plugin-image-preview'
import FilePondPluginFileValidateSize from 'filepond-plugin-file-validate-size'
import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type'
import FilePondPluginImageTransform from 'filepond-plugin-image-transform'
import SignIn from "layouts/SignIn";

// Create FilePond component
const FilePond = vueFilePond(
    FilePondPluginImageExifOrientation,
    FilePondPluginImageCrop,
    FilePondPluginImagePreview,
    FilePondPluginFileValidateSize,
    FilePondPluginFileValidateType,
    FilePondPluginImageTransform
);

export default {
    name: "AnimationCreate",
    created() {
        if (this.readyToInitialize) this.selectIP(this.$route.query.ip_id)
    },
    data() {
        return {
            ip: null,
            label:'Drag & Drop a 16:9 image or <span class=\"filepond--label-action\"> Browse </span>',
            animationCreateBuffer: {
                avatarFile: [],
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
                        reversed:null
                    },
                    producedBy: '',
                    releasedAt: null,
                    writtenBy: '',
                    type: null,
                    episodesNum: null,
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
                if (ip.id === Number(this.$route.query.ip_id)){
                    this.ip=ip
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
        initialized(){
            return this.ip!==null
        },
        ipmodel(){
            return this.ip.reservedNames[this.$i18n.locale] || this.ip.name
        }
    },
    watch: {
        readyToInitialize() {
            console.log(this.$route.query.ip_id)
            if (this.readyToInitialize) {
                this.selectIP(this.$route.query.ipId)
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
