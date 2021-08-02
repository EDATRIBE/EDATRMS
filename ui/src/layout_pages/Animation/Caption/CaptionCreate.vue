<template>
    <q-page padding class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em" v-if="initialized">
        <div class="q-mx-auto" style="width: 97%">
            <div class="column full-width">

                <!--Title-->
                <div style="width: 100%" class="q-pl-md bl">
                    <div class="row q-pb-md">
                        <p class="q-my-none text-primary text-h4 ">NEW CAPTION</p>
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
                                options-selected-class="text-primary"
                                standout=""
                                v-model="captionCreateBuffer.data.integrated"
                                hide-bottom-space
                                :options="integratedModels"
                                emit-value
                                map-options
                            >
                            </q-select>
                        </div>
                    </div>
                    <!--state-->
                    <div class="row items-center q-py-sm">
                        <div class="col-md-2 col-xs-12">
                            <p class="q-my-none text-grey text-body1 text-weight-medium">STATE</p>
                        </div>
                        <div class="col-md-10 col-xs-12">
                            <q-select
                                class="bg-dark-light"
                                dark
                                dense
                                options-dense
                                options-selected-class="text-primary"
                                standout=""
                                v-model="captionCreateBuffer.data.state"
                                hide-bottom-space
                                :options="stateModels"
                                emit-value
                                map-options
                            >
                            </q-select>
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
                                v-model="captionCreateBuffer.data.releasedAt"
                                :rules="[v => /(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})/.test(v) || 'wrong time']"
                            >
                                <template v-slot:prepend>
                                    <q-icon name="event" class="cursor-pointer">
                                        <q-popup-proxy transition-show="scale" transition-hide="scale">
                                            <q-date color="primary" v-model="captionCreateBuffer.data.releasedAt" mask="YYYY-MM-DD HH:mm">
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
                                            <q-time color="primary" v-model="captionCreateBuffer.data.releasedAt" mask="YYYY-MM-DD HH:mm" format24h>
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
                    <q-separator color="grey-7" class="q-my-sm"></q-separator>
                    <!--Name-->
                    <div class="row items-center q-py-sm">
                        <div class="col-md-2 col-xs-12">
                            <p class="q-my-none text-grey text-body1 text-weight-medium">FILE NAME</p>
                        </div>
                        <div class="col-md-10 col-xs-12">
                            <q-input
                                dense dark class="bg-dark-light" standout=""
                                v-model="captionCreateBuffer.data.fileMeta.name"
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
                                v-model="captionCreateBuffer.data.fileMeta.type"
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
                                v-model="captionCreateBuffer.data.fileMeta.size"
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
                                v-model="captionCreateBuffer.data.comment"
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
                            @click="commitCreate"
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
    name: "CaptionCreate",
    created() {
        if (this.readyToInitialize) this.selectAnimation(this.$route.query.animation_id)
    },
    data() {
        return {
            animation: null,
            captionCreateBuffer: {
                data:{
                    animationId: null,
                    integrated: '',
                    state: '',
                    releasedAt: '',
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
        selectAnimation(id) {
            for (const ip of this.ips) {
                for (const animation of ip.animations) {
                    if (animation.id === Number(id)){
                        this.animation = animation
                    }
                }
            }
        },
        commitCreate() {
            this.captionCreateBuffer.data.animationId = this.animation.id
            this.$axios.post('api/caption/create', this.captionCreateBuffer.data).then((response) => {
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
        stateModels() {
            return [
                {
                    label: '_i18n_TODO',
                    value: 'TODO'
                },
                {
                    label: '_i18n_DOING',
                    value: 'DOING'
                },
                {
                    label: '_i18n_DONE',
                    value: 'DONE'
                },
            ]
        },
        typeModels() {
            return [
                {
                    label: '_i18n_SRT',
                    value: 'SRT'
                },
                {
                    label: '_i18n_ASS',
                    value: 'ASS'
                },
                {
                    label: '_i18n_VTT',
                    value: 'VTT'
                },
                {
                    label: '_i18n_SUP',
                    value: 'SUP'
                },
                {
                    label: '_i18n_SSA',
                    value: 'SSA'
                },
            ]
        }
    },
    watch: {
        readyToInitialize() {
            console.log('caption/create:animation_id='+this.$route.query.animation_id)
            if (this.readyToInitialize) {
                this.selectAnimation(this.$route.query.animation_id)
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
