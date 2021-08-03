<template>
    <q-page v-if="initialized" padding class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
        <div class="q-mx-auto " style="width: 97%; border-radius: 0px">
            <div class="row q-col-gutter-x-md justify-center">
                <!--LEFT-->
                <div class="column col-md-3 col-xs-12">
                    <q-img
                        class="shadow-2"
                        style="border-radius: 4px"
                        :src="novel.images.vertical.url"
                        v-if="novel.images.vertical!==undefined"
                    />
                    <q-btn dense class=" q-mt-md shadow-2" color="secondary" text-color="white">
                        REPORT A PROBLEM
                        <q-icon class="q-pl-sm" name="construction" size="1.5em"/>
                    </q-btn>
                </div>
                <!--RIGHT-->
                <div class="column col-md-9 col-xs-12 q-pb-md">
                    <!--TITLE-->
                    <div style="width: 100%" class="q-px-md q-pb-md bl">
                        <p class="q-my-none text-secondary  text-h4">
                            {{ novel.reservedNames[$i18n.locale] || novel.name }}
                        </p>
                    </div>
                    <!--INFOS-->
                    <div style="width: 100%" class="q-px-md q-pt-md bl">
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <q-icon color="secondary" name="fas fa-info-circle" size="2.5em"></q-icon>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-secondary  text-h4"></p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 30%"/>
                        <div class="row q-py-md ">
                            <div class="col-md-2 col-xs-12"><p
                                class="q-my-none text-grey text-body1 text-weight-medium">INTRO</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1 text-justify">
                                    {{ novel.intros[$i18n.locale] }}
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
                                    {{ novel.writtenBy }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 20%"></q-separator>
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12"><p
                                class="q-my-none text-grey text-body1 text-weight-medium">VOLUMES NUM</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1">
                                    {{ novel.volumesNum }}
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
                                    {{ novel.integrated }}
                                </p>
                            </div>
                        </div>
                    </div>
                    <!--File-->
                    <div style="width: 100%" class="q-px-md q-pt-md bl">
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <q-icon color="secondary" name="fas fa-file-alt" size="2.5em"></q-icon>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-secondary  text-h4"></p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 30%"/>
                        <div class="row q-py-md ">
                            <div class="col-md-2 col-xs-12"><p
                                class="q-my-none text-grey text-body1 text-weight-medium">FORMAT</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1 text-justify">
                                    {{ novel.fileMeta.type }}
                                </p>
                            </div>
                        </div>
                        <q-separator color="grey" style="opacity: 30%"/>
                        <div class="row q-py-md ">
                            <div class="col-md-2 col-xs-12"><p
                                class="q-my-none text-grey text-body1 text-weight-medium">SIZE</p>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-body1 text-justify">
                                    {{ novel.fileMeta.size }}
                                </p>
                            </div>
                        </div>
                    </div>
                    <!--Address-->
                    <div style="width: 100%" class="q-px-md q-pt-md bl">
                        <div class="row q-py-md">
                            <div class="col-md-2 col-xs-12">
                                <q-icon color="secondary" name="cloud_download" size="2.7em"></q-icon>
                            </div>
                            <div class="col-md-10 col-xs-12">
                                <p class="q-my-none text-white text-white text-h2"></p>
                            </div>
                        </div>
                        <div
                            v-if="novel.sharingAddresses.aliCloud !== undefined &&
                             novel.sharingAddresses.aliCloud.url!==''"
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
                                        <a :href="novel.sharingAddresses.aliCloud.url">
                                            <p class="q-my-none text-secondary text-body1">
                                                {{ novel.sharingAddresses.aliCloud.password }}
                                            </p>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div
                            v-if="novel.sharingAddresses.baiduCloud !== undefined &&
                             novel.sharingAddresses.baiduCloud.url!==''"
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
                                        <a :href="novel.sharingAddresses.baiduCloud.url">
                                            <p class="q-my-none text-secondary text-body1">
                                                {{ novel.sharingAddresses.baiduCloud.password }}
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
</style>
