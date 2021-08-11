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
                expand-icon-class="q-pr-sm text-secondary"
                expand-icon="filter_alt"
                expanded-icon="filter_alt"
            >
                <!--ToolsHeader-->
                <template v-slot:header>
                    <div class="row items-center text-body1 full-width ">
                        <q-btn-toggle
                            text-color="grey-7" size="0.75em" unelevated
                            class="no-border-radius bg-dark-light" toggle-color="secondary" toggle-text-color="dark"
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
                            active-b-g-class="bg-secondary"
                        />
                    </q-item>

                    <!--type-->
                    <q-item dense dark class="q-pa-none  q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="novelTypeOptions"
                            v-model="filterBuffer.novelType"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-secondary"
                        />
                    </q-item>

                    <!--integrated-->
                    <q-item dense dark class="q-pa-none  q-mt-sm">
                        <multiple-choice
                            class="text-body1"
                            :options="integratedOptions"
                            v-model="filterBuffer.integrated"
                            text-class="text-grey-7"
                            b-g-class="bg-dark-light"
                            active-text-class="text-dark"
                            active-b-g-class="bg-secondary"
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
                            active-b-g-class="bg-secondary"
                        />
                    </q-item>
                </div>
            </q-expansion-item>
        </div>

        <!--Content-->
        <div class="row q-col-gutter-x-sm q-col-gutter-y-lg">
            <div class="col-md-2 col-sm-3 col-xs-6 col-lg-2 col-xl-2"
                 v-for="(novel,i) in filterResultNovels.slice((pageNum-1)*pageLen,pageNum*pageLen)"
                 :key="i+novel.id+novel.name"
            >
                <q-card
                    dark
                    class="bg-dark cursor-pointer my-card"
                    flat style="border-radius: 3px"
                    @click="$router.push({path:'/novel/info',query:{id:novel.id}})"
                >
                    <q-responsive :ratio="2/3">
                        <div class="full-width" style="overflow: hidden; position: relative;border-radius: 3px">
                            <q-img
                                :src="novel.images.vertical?
                                    novel.images.vertical.url:
                                    require('src/assets/placeholder.jpg')"
                                class="mhs"
                            >
                            </q-img>
                            <q-chip
                                dense
                                class="absolute q-ma-none q-pa-md text-weight-medium shadow-1" color="secondary"
                                text-color="white"
                                style="right: 0px; top:0px;  opacity: .9; border-radius: 0px 0px 0px 12px;">
                                {{ novel.fileMeta.type }}
                            </q-chip>
                        </div>
                    </q-responsive>
                    <q-card-section class="q-py-xs q-px-none text-body1 text-weight-bold ov my-section">
                        <span class="mhc">{{ novel.reservedNames[$i18n.locale] || novel.name }}</span>
                    </q-card-section>
                </q-card>
            </div>
        </div>

        <!--pagination-->
        <div class="full-width row justify-center q-py-lg">
            <q-pagination
                v-model="pageNum"
                color="secondary"
                active-color="secondary"
                active-text-color="dark"
                :max="Math.ceil(filterResultNovels.length/pageLen)"
                :max-pages="10"
                boundary-links
            />
        </div>
    </div>
</template>

<script>
import MultipleChoice from "components/MultipleChoice";

export default {
    name: "IndexNovels",
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
                novelType: 'ALL',
                integrated: 'ALL',
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
        filterResultNovels() {
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


                let filterResultNovels = []
                for (const ip of filterResultIPs) {
                    for (const novel of ip.novels) {
                        filterResultNovels.push(novel)
                    }
                }

                const novelTypeFilter = (novel) => {
                    if (this.filterBuffer.novelType === 'ALL') {
                        return true
                    } else {
                        if (novel.fileMeta.type === this.filterBuffer.novelType) {
                            return true
                        } else {
                            return false
                        }
                    }
                }
                filterResultNovels = filterResultNovels.filter(novelTypeFilter)

                const integratedFilter = (novel) => {
                    if (this.filterBuffer.integrated === 'ALL') {
                        return true
                    } else {
                        if (novel.integrated === this.filterBuffer.integrated) {
                            return true
                        } else {
                            return false
                        }
                    }
                }
                filterResultNovels = filterResultNovels.filter(integratedFilter)

                const compareNovelByUpdatedAt = (aniA, aniB) => {
                    const dA = new Date(aniA.updatedAt)
                    const dB = new Date(aniB.updatedAt)
                    return dA < dB ? 1:-1
                }

                const compareNovelByName= (aniA, aniB) => {
                    if (this.$i18n.locale == 'en'){
                        return (aniA.reservedNames[this.$i18n.locale] || aniA.name) >
                        (aniB.reservedNames[this.$i18n.locale] || aniB.name)? 1:-1
                    }else if(this.$i18n.locale == 'cn'){
                        return (aniA.reservedNames[this.$i18n.locale] || aniA.name).localeCompare(
                            (aniB.reservedNames[this.$i18n.locale] || aniB.name),'zh'
                        )
                    }
                }

                if (this.filterBuffer.order==='date'){
                    filterResultNovels.sort(compareNovelByUpdatedAt)
                }else if (this.filterBuffer.order==='alphabet'){
                    filterResultNovels.sort(compareNovelByName)
                }

                return filterResultNovels
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
        novelTypeOptions() {
            return [
                {label: 'ALL', value: 'ALL'},
                {label: 'TXT', value: 'TXT'},
                {label: 'PDF', value: 'PDF'},
                {label: 'EPUB', value: 'EPUB'}
            ]
        },
        integratedOptions() {
            return [
                {label: 'ALL', value: 'ALL'},
                {label: 'INTEGRATED', value: true},
                {label: 'UNINTEGRATED', value: false}
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
    border-bottom-color: $secondary
    border-width: 2px

.bt
    border-top: solid
    border-top-color: $secondary
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
    color: $secondary
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
//    novel: 1s forwards
//    novel-name: flipInX
//    -webkit-novel-name: flipInX

</style>
