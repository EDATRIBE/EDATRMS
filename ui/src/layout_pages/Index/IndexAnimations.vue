<template>
    <div class="q-pt-sm">

        <!--Tools-->
        <div @mouseleave="toolbarExpanded=false">
            <q-expansion-item
                v-model="toolbarExpanded"
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
                            v-model="filterBuffer.order"
                            :options="orderOptions"
                        />
                    </div>
                </template>
                <!--ToolsContent-->
                <div class="q-pt-sm q-pb-sm bb">
                    <!--region-->
                    <q-item dense dark class="q-pa-none ">
                        <multiple-choice
                            class="text-body1"
                            :options="regionOptions"
                            v-model="filterBuffer.region"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>

                    <!--type-->
                    <q-item dense dark class="q-pa-none  q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="animationTypeOptions"
                            v-model="filterBuffer.animationType"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>

                    <!--releasedAt-->
                    <q-item dense dark class="q-pa-none  q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="releasedAtOptions"
                            v-model="filterBuffer.releasedAt"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>
                    <!--videoType-->
                    <q-item dense dark class="q-pa-none  q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="videoTypeOptions"
                            v-model="filterBuffer.videoType"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>
                    <!--quality-->
                    <q-item dense dark class="q-pa-none  q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="qualityOptions"
                            v-model="filterBuffer.quality"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>
                    <!--captionType-->
                    <q-item dense dark class="q-pa-none  q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="captionTypeOptions"
                            v-model="filterBuffer.captionType"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>
                    <!--captionState-->
                    <q-item dense dark class="q-pa-none  q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="captionStateOptions"
                            v-model="filterBuffer.captionState"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-primary"
                        />
                    </q-item>
                    <!--tagId-->
                    <q-item dense dark class="q-pa-none q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="tagOptions"
                            v-model="filterBuffer.tagId"
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
        <div class="row q-col-gutter-x-sm q-col-gutter-y-lg" v-if="initialized">
            <div class="col-md-2 col-sm-3 col-xs-6 col-lg-2 col-xl-2"
                 v-for="(animation,i) in filterResultAnimations.slice((pageNum-1)*pageLen,pageNum*pageLen)"
                 :key="i+animation.id+animation.name"
            >
                <q-card
                    dark flat
                    class="bg-dark cursor-pointer my-card"
                    @click="$router.push({path:'/animation/info',query:{id:animation.id}})"
                >
                    <!--                    <q-img :src="require('assets/aaa.jpg')" class="my-img">-->
                    <!--                        <div class="absolute-full text-subtitle2 flex flex-center my-text">-->
                    <!--                            <q-icon class="shadow-3 mhc" size="4em" name="fas fa-link"></q-icon>-->
                    <!--                        </div>-->
                    <!--                        <q-chip-->
                    <!--                            dense-->
                    <!--                            class="absolute q-ma-none text-weight-medium shadow-5" color="primary"-->
                    <!--                            style="right: 0px; top:0px;  opacity: .9; border-radius: 0px 0px 0px 12px;">-->
                    <!--                            {{i%2?'EPS':'MOVIE'}}-->
                    <!--                        </q-chip>-->
                    <!--                    </q-img>-->
                    <q-responsive :ratio="2/3">
                        <div class="full-width" style="overflow: hidden; position: relative; ">
                            <q-img
                                :src="animation.images.vertical?
                                    animation.images.vertical.url:
                                    require('src/assets/placeholder.jpg')"
                                class="mhs"
                            >
                            </q-img>
                            <q-chip
                                dense
                                class="absolute q-ma-none q-pa-md text-weight-medium shadow-1" color="primary"
                                text-color="white"
                                style="right: 0px; top:0px;  opacity: .9; border-radius: 0px 0px 0px 12px;">
                                {{ animation.type }}
                            </q-chip>
                        </div>
                    </q-responsive>
                    <q-card-section class="q-py-xs q-px-none text-body1 text-weight-bold ov my-section">
                        <span class="mhc">{{ animation.reservedNames[$i18n.locale] || animation.name }}</span>
                    </q-card-section>
                </q-card>
            </div>
        </div>

        <!--pagination-->
        <div
            class="full-width row justify-center q-py-lg"
            v-if="$q.screen.gt.sm"
        >
            <q-pagination
                v-model="pageNum"
                color="primary"
                active-color="primary"
                active-text-color="dark"
                :max="Math.ceil(filterResultAnimations.length/pageLen)"
                :max-pages="10"
                boundary-links
                unelevated
            />
        </div>

        <!--pagination-->
        <div
            class="full-width row justify-center q-py-lg"
            v-if="!$q.screen.gt.sm"
        >
            <q-pagination
                v-model="pageNum"
                :max="Math.ceil(filterResultAnimations.length/pageLen)"
                color="primary"
                input
                input-class="text-primary text-weight-medium"
            />
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
            toolbarExpanded: false,
            pageNum: 1,
            pageLen: 24,
            filterBuffer: {
                tagId: -1,
                order: 'date',
                region: 'ALL',
                animationType: 'ALL',
                releasedAt: 'ALL',
                quality: 'ALL',
                videoType: 'ALL',
                captionType: 'ALL',
                captionState: 'ALL'
            }
        }
    },
    computed: {
        initialized() {
            return this.$store.getters.ipsInitialized && this.$store.getters.tagsInitialized
        },
        searchResultIPs() {
            return this.$store.state.ip.searchResults
        },
        tags() {
            return this.$store.state.tag.tags
        },
        filterResultAnimations() {
            if (!this.searchResultIPs) {
                return []
            } else {

                let filterResultIPs = this.searchResultIPs
                const regionFilter = (ip) => {
                    if (this.filterBuffer.region === 'ALL') {
                        return true
                    } else {
                        return ip.region === this.filterBuffer.region
                    }
                }
                filterResultIPs = filterResultIPs.filter(regionFilter)
                const tagFilter = (ip) => {
                    if (this.filterBuffer.tagId === -1) {
                        return true
                    } else {
                        return ip.tagIds.includes(this.filterBuffer.tagId)
                    }
                }
                filterResultIPs = filterResultIPs.filter(tagFilter)


                let filterResultAnimations = []
                for (const ip of filterResultIPs) {
                    for (const animation of ip.animations) {
                        filterResultAnimations.push(animation)
                    }
                }

                const animationTypeFilter = (animation) => {
                    if (this.filterBuffer.animationType === 'ALL') {
                        return true
                    } else {
                        if (animation.type === this.filterBuffer.animationType) {
                            return true
                        } else {
                            return false
                        }
                    }
                }
                filterResultAnimations = filterResultAnimations.filter(animationTypeFilter)

                const releasedAtFilter = (animation) => {
                    if (this.filterBuffer.releasedAt === 'ALL') {
                        return true
                    } else {
                        const releasedAt = new Date(animation.releasedAt)
                        const lb = new Date(this.filterBuffer.releasedAt, 0, 0)
                        const rb = new Date(Number(this.filterBuffer.releasedAt) + 10, 0, 0)
                        if (lb <= releasedAt && releasedAt < rb) {
                            return true
                        } else {
                            return false
                        }
                    }
                }
                filterResultAnimations = filterResultAnimations.filter(releasedAtFilter)

                const videoTypeFilter = (animation) => {
                    if (this.filterBuffer.videoType === 'ALL') {
                        return true
                    } else {
                        for (const video of animation.videos) {
                            if (video.fileMeta.type === this.filterBuffer.videoType) {
                                return true
                            }
                        }
                        return false
                    }
                }
                filterResultAnimations = filterResultAnimations.filter(videoTypeFilter)

                const qualityFilter = (animation) => {
                    if (this.filterBuffer.quality === 'ALL') {
                        return true
                    } else {
                        for (const video of animation.videos) {
                            if (video.fileMeta.quality === this.filterBuffer.quality) {
                                return true
                            }
                        }
                        return false
                    }
                }
                filterResultAnimations = filterResultAnimations.filter(qualityFilter)

                const captionTypeFilter = (animation) => {
                    if (this.filterBuffer.captionType === 'ALL') {
                        return true
                    } else {
                        for (const caption of animation.captions) {
                            if (caption.fileMeta.type === this.filterBuffer.captionType) {
                                return true
                            }
                        }
                        return false
                    }
                }
                filterResultAnimations = filterResultAnimations.filter(captionTypeFilter)

                const captionStateFilter = (animation) => {
                    if (this.filterBuffer.captionState === 'ALL') {
                        return true
                    } else {
                        for (const caption of animation.captions) {
                            if (caption.state === this.filterBuffer.captionState) {
                                return true
                            }
                        }
                        return false
                    }
                }
                filterResultAnimations = filterResultAnimations.filter(captionStateFilter)

                const compareAnimationByUpdatedAt = (aniA, aniB) => {
                    const dA = new Date(aniA.updatedAt)
                    const dB = new Date(aniB.updatedAt)
                    return dA < dB ? 1 : -1
                }

                const compareAnimationByName = (aniA, aniB) => {
                    if (this.$i18n.locale == 'en') {
                        return (aniA.reservedNames[this.$i18n.locale] || aniA.name) >
                        (aniB.reservedNames[this.$i18n.locale] || aniB.name) ? 1 : -1
                    } else if (this.$i18n.locale == 'cn') {
                        return (aniA.reservedNames[this.$i18n.locale] || aniA.name).localeCompare(
                            (aniB.reservedNames[this.$i18n.locale] || aniB.name), 'zh'
                        )
                    }
                }

                if (this.filterBuffer.order === 'date') {
                    filterResultAnimations.sort(compareAnimationByUpdatedAt)
                } else if (this.filterBuffer.order === 'alphabet') {
                    filterResultAnimations.sort(compareAnimationByName)
                }

                return filterResultAnimations
            }
        },
        orderOptions() {
            return [
                {label: 'date', icon: 'fas fa-sort-numeric-down-alt', value: 'date'},
                {label: 'alphabet', icon: 'fas fa-sort-alpha-down', value: 'alphabet'}
            ]
        },
        regionOptions() {
            return [
                {label: 'ALL', value: 'ALL'},
                {label: 'CN', value: 'CN'},
                {label: 'JP', value: 'JP'},
                {label: 'OTHER', value: 'OTHER'},
            ]
        },
        animationTypeOptions() {
            return [
                {label: 'ALL', value: 'ALL'},
                {label: 'TV', value: 'TV'},
                {label: 'MOVIE', value: 'MOVIE'},
                {label: 'SP', value: 'SP'},
                {label: 'OVA', value: 'OVA'},
                {label: 'OAD', value: 'OAD'}
            ]
        },
        releasedAtOptions() {
            return [
                {label: 'ALL', value: 'ALL'},
                {label: '1960s', value: 1600},
                {label: '1970s', value: 1700},
                {label: '1980s', value: 1800},
                {label: '1990s', value: 1900},
                {label: '2000s', value: 2000},
                {label: '2010s', value: 2010},
                {label: '2020s', value: 2020}
            ]
        },
        qualityOptions() {
            return [
                {label: 'ALL', value: 'ALL'},
                {label: '360P', value: '360P'},
                {label: '640P', value: '640P'},
                {label: '720P', value: '720P'},
                {label: '960P', value: '960P'},
                {label: '1080P', value: '1080P'}
            ]
        },
        videoTypeOptions() {
            return [
                {label: 'ALL', value: 'ALL'},
                {label: 'MP4', value: 'MP4'},
                {label: 'MKV', value: 'MKV'},
                {label: 'AV1', value: 'AV1'},
                {label: 'OGG', value: 'OGG'}
            ]
        },
        captionTypeOptions() {
            return [
                {label: 'ALL', value: 'ALL'},
                {label: 'SRT', value: 'SRT'},
                {label: 'ASS', value: 'ASS'},
                {label: 'VTT', value: 'VTT'},
                {label: 'SUP', value: 'SUP'},
                {label: 'SSA', value: 'SSA'}
            ]
        },
        captionStateOptions() {
            return [
                {label: 'ALL', value: 'ALL'},
                {label: 'SUBTITLE: TODO', value: 'TODO'},
                {label: 'SUBTITLE: DOING', value: 'DOING'},
                {label: 'SUBTITLE: DONE', value: 'DONE'}
            ]
        },
        tagOptions() {
            if (!this.tags) {
                return []
            } else {
                const tagOptions = []
                tagOptions.push(
                    {
                        label: 'ALL',
                        value: -1
                    }
                )
                for (const tag of this.tags) {
                    tagOptions.push(
                        {
                            label: tag.reservedNames[this.$i18n.locale] || tag.name,
                            value: tag.id
                        }
                    )
                }
                return tagOptions
            }
        },
    },
    watch: {
        pageNum() {
            window.scrollTo(0, 0)
            // const element = document.getElementById("tool");
            // element.scrollIntoView();
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

.my-section .mhc
    color: white
    transition: .3s

.my-section:hover .mhc
    color: $primary
    transition: .3s

.my-card .mhs
    -webkit-filter: brightness(.99)
    filter: brightness(.99)
    transform: translateZ(0) scale(1)
    transition: transform .4s ease 0s

.my-card:hover .mhs
    -webkit-filter: brightness(1)
    filter: brightness(1)
    transform: translateZ(0) scale(1.3)

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
