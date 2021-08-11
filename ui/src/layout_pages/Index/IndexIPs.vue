<template>
    <div class="q-pt-sm ">
        <IPDeleteDialog
            :id.sync="ipDeleteBuffer.id"
            :is-deleting.sync="ipDeleteBuffer.isDeleting"
        />
        <AnimationDeleteDialog
            :id.sync="animationDeleteBuffer.id"
            :is-deleting.sync="animationDeleteBuffer.isDeleting"
        />
        <video-delete-dialog
            :id.sync="videoDeleteBuffer.id"
            :is-deleting.sync="videoDeleteBuffer.isDeleting"
        />
        <caption-delete-dialog
            :id.sync="captionDeleteBuffer.id"
            :is-deleting.sync="captionDeleteBuffer.isDeleting"
        />
        <novel-delete-dialog
            :id.sync="novelDeleteBuffer.id"
            :is-deleting.sync="novelDeleteBuffer.isDeleting"
        />
        <div class="q-col-gutter-y-sm" v-if="initialized">
            <!--Tools-->
            <div @mouseleave="toolbarExpanded=false">
                <q-expansion-item
                    v-model="toolbarExpanded"
                    id="tool"
                    dense
                    dark
                    expand-icon-toggle
                    header-class="bl q-pa-none "
                    expand-icon-class="q-pr-sm text-accent"
                    expand-icon="filter_alt"
                    expanded-icon="filter_alt"
                    :duration="200"
                >
                    <!--ToolsHeader-->
                    <template v-slot:header>
                        <div class="row  items-center text-body1 full-width ">
                            <q-btn-toggle
                                text-color="grey-7"
                                size="0.75em"
                                unelevated
                                class="no-border-radius bg-dark-light"
                                v-model="filterBuffer.order"
                                toggle-color="accent"
                                toggle-text-color="dark"
                                :options="orderOptions"
                            />
                            <q-space></q-space>
                            <q-icon
                                name="fas fa-plus" color="accent" size="1.25em" class="q-mx-sm cursor-pointer"
                                @click="$router.push('/ip/create')"
                            />
                        </div>
                    </template>

                    <!--ToolsContent-->
                    <div class="q-pt-sm">
                        <!--region-->
                        <q-item dense dark class="q-pa-none">
                            <multiple-choice
                                class="text-body1"
                                :options="regionOptions"
                                v-model="filterBuffer.region"
                                text-class="text-grey-7"
                                b-g-class="bg-dark-light"
                                active-text-class="text-dark"
                                active-b-g-class="bg-accent"
                            />
                        </q-item>
<!--                        &lt;!&ndash;animationType&ndash;&gt;-->
<!--                        <q-item dense dark class="q-pa-none  q-mt-sm">-->
<!--                            <multiple-choice-->
<!--                                class="text-body1"-->
<!--                                :options="animationTypeOptions"-->
<!--                                v-model="filterBuffer.animationType"-->
<!--                                text-class="text-grey-7"-->
<!--                                b-g-class="bg-dark-light"-->
<!--                                active-text-class="text-dark"-->
<!--                                active-b-g-class="bg-accent"-->
<!--                            />-->
<!--                        </q-item>-->
                        <!--tagId-->
                        <q-item dense dark class="q-pa-none q-mt-sm">
                            <multiple-choice
                                class="text-body1"
                                :options="tagOptions"
                                v-model="filterBuffer.tagId"
                                text-class="text-grey-7"
                                b-g-class="bg-dark-light"
                                active-text-class="text-dark"
                                active-b-g-class="bg-accent"
                            />
                        </q-item>
                    </div>

                </q-expansion-item>
            </div>
            <!--Content-->
            <div v-for="(ip,i) in filterResultIPs.slice((pageNum-1)*pageLen,pageNum*pageLen)" :key="i+ip.id+ip.name">
                <!--IPS-->
                <q-expansion-item
                    dense
                    dark
                    expand-icon-toggle
                    class="bg-dark-light bl"
                    header-class="bl q-pa-none bg-dark-light"
                    expand-icon-class="q-px-sm text-accent"
                    :duration="200"
                >
                    <!--IPHeader-->
                    <template v-slot:header>
                        <div class="row no-wrap q-pl-md  items-center text-body1 full-width text-weight-medium">
                            <q-icon name="source" color="accent" size="1.3em" class="q-mr-md"></q-icon>
                            {{ ip.reservedNames[$i18n.locale] || ip.name }}
                            <div class="row q-mx-sm">
                                <q-chip
                                    size="0.7em" square dense text-color="dark" color="accent"
                                    class="q-py-none text-weight-medium"
                                >
                                    {{ ip.region }}
                                </q-chip>
                                <q-chip
                                    v-for="(tagId,i) in ip.tagIds" :key="i+tagId+'tagId'"
                                    size="0.7em" square dense text-color="dark" color="accent"
                                    class="q-py-none text-weight-medium"
                                >
                                    {{ idTagDict[tagId].reservedNames[$i18n.locale] || idTagDict[tagId].name }}
                                </q-chip>
                            </div>
                            <q-space></q-space>
                            <q-btn
                                flat color="accent" icon="add"
                                @click="$router.push({
                                  path: '/animation/create',
                                  query: {
                                    ip_id: ip.id
                                  }
                                })"
                            >
                                animation
                            </q-btn>
                            <q-btn
                                flat color="accent" icon="add"
                                @click="$router.push({
                                  path: '/novel/create',
                                  query: {
                                    ip_id: ip.id
                                  }
                                })"
                            >
                                novel
                            </q-btn>
                            <q-btn
                                flat color="accent"
                                @click="$router.push({
                                  path: '/ip/edit',
                                  query: {
                                    id: ip.id
                                  }
                                })"
                            >
                                edit
                            </q-btn>
                            <q-btn
                                flat color="red"
                                @click="ipDeleteBuffer.id=ip.id;ipDeleteBuffer.isDeleting=true"
                            >
                                delete
                            </q-btn>
                        </div>
                    </template>

                    <!--IPContent-->
                    <div class="q-pl-lg q-py-sm"><!--DONT SET MARGIN!-->
                        <div class="q-col-gutter-y-sm"><!--DONT SET MARGIN!-->
                            <!--Animations-->
                            <div v-for="(animation,i) in ip.animations" :key="i+animation.id+animation.name">
                                <!--DONT SET MARGIN!-->
                                <q-expansion-item
                                    dense
                                    dark
                                    expand-icon-toggle
                                    class="bg-dark-light bl1"
                                    header-class="bl q-pa-none bg-dark-light"
                                    expand-icon-class="q-px-sm text-primary"
                                    :duration="200"
                                >
                                    <!--AnimationsHeader-->
                                    <template v-slot:header>
                                        <div class="row q-pl-md  items-center text-body1 full-width text-weight-medium">
                                            <q-icon name="movie" color="primary" size="1.3em" class="q-mr-md"></q-icon>
                                            {{ animation.reservedNames[$i18n.locale] || animation.name }}
                                            <q-icon
                                                @click="$router.push({path:'/animation/info',query:{id:animation.id}})"
                                                size="0.75em" color="primary" class="cursor-pointer q-ml-sm"
                                                name="fas fa-link"
                                            />
                                            <div class="row q-mx-sm">
                                                <q-chip outline
                                                        size="0.7em" square dense text-color="dark" color="primary"
                                                        class="q-py-none text-weight-medium"
                                                >
                                                    {{ animation.type }}
                                                </q-chip>
                                                <q-chip outline
                                                        size="0.7em" square dense text-color="dark" color="primary"
                                                        class="q-py-none text-weight-medium"
                                                >
                                                    {{ animation.episodesNum }} EPS
                                                </q-chip>
                                            </div>
                                            <q-space></q-space>
                                            <q-btn
                                                @click="$router.push({path:'/animation/video/create',query:{animation_id:animation.id}})"
                                                icon="add" flat color="primary"
                                            >
                                                video
                                            </q-btn>
                                            <q-btn
                                                @click="$router.push({path:'/animation/caption/create',query:{animation_id:animation.id}})"
                                                icon="add" flat color="primary"
                                            >
                                                caption
                                            </q-btn>
                                            <q-btn
                                                flat color="primary"
                                                @click="$router.push({
                                                    path: '/animation/edit',
                                                    query: {
                                                        id: animation.id
                                                    }
                                                })"
                                            >
                                                edit
                                            </q-btn>
                                            <q-btn
                                                flat color="red"
                                                @click="animationDeleteBuffer.id=animation.id; animationDeleteBuffer.isDeleting=true"
                                            >
                                                delete
                                            </q-btn>
                                        </div>
                                    </template>

                                    <!--AnimationsContent-->
                                    <div class="q-pl-lg q-py-xs"><!--DONT SET MARGIN!-->
                                        <div class="q-col-gutter-y-xs"><!--DONT SET MARGIN!-->
                                            <!--AnimationsVideo-->
                                            <div v-for="(video,i) in animation.videos"
                                                 :key="i+animation.name+video.id">
                                                <q-item
                                                    dense dark class="bg-dark-light q-pa-none bl1"
                                                    style="padding-right: 39.3px"
                                                >
                                                    <div
                                                        class="row q-pl-md items-center text-body1 full-width text-weight-medium">
                                                        <q-icon name="fas fa-film" color="primary" size="1.3em"
                                                                class="q-mr-md"></q-icon>
                                                        {{ video.fileMeta.name || 'video' }}
                                                        <div class="row q-mx-sm">
                                                            <q-chip outline
                                                                    size="0.7em" square dense text-color="dark"
                                                                    color="primary" class="q-py-none text-weight-medium"
                                                            >
                                                                {{ video.fileMeta.type }}
                                                            </q-chip>
                                                            <q-chip outline
                                                                    size="0.7em" square dense text-color="dark"
                                                                    color="primary" class="q-py-none text-weight-medium"
                                                            >
                                                                {{ video.fileMeta.quality }}
                                                            </q-chip>
                                                        </div>
                                                        <q-space></q-space>
                                                        <q-btn
                                                            flat color="primary"
                                                            @click="$router.push({
                                                              path: '/animation/video/edit',
                                                              query: {
                                                                video_id: video.id
                                                              }
                                                            })"
                                                        >
                                                            edit
                                                        </q-btn>
                                                        <q-btn
                                                            flat color="red"
                                                            @click="videoDeleteBuffer.id=video.id; videoDeleteBuffer.isDeleting=true"
                                                        >
                                                            delete
                                                        </q-btn>
                                                    </div>
                                                </q-item>
                                            </div>

                                            <!--AnimationsCaption-->
                                            <div v-for="(caption,i) in animation.captions"
                                                 :key="i+'cap'+animation.id+'captionId'+caption.id">
                                                <q-item
                                                    dense dark class="bg-dark-light q-pa-none bl1"
                                                    style="padding-right: 39.3px"
                                                >
                                                    <div
                                                        class="row q-pl-md items-center text-body1 full-width text-weight-medium">
                                                        <q-icon name="fas fa-closed-captioning" color="primary"
                                                                size="1.3em"
                                                                class="q-mr-md"></q-icon>
                                                        {{ caption.fileMeta.name || 'caption' }}
                                                        <div class="row q-mx-sm">
                                                            <q-chip outline
                                                                    size="0.7em" square dense text-color="dark"
                                                                    color="primary" class="q-py-none text-weight-medium"
                                                            >
                                                                {{ caption.state }}
                                                            </q-chip>
                                                            <q-chip outline
                                                                    size="0.7em" square dense color="primary"
                                                                    class="q-py-none text-weight-medium"
                                                            >
                                                                {{ caption.fileMeta.type }}
                                                            </q-chip>
                                                        </div>
                                                        <q-space></q-space>
                                                        <q-btn
                                                            flat color="primary"
                                                            @click="$router.push({
                                                              path: '/animation/caption/edit',
                                                              query: {
                                                                caption_id: caption.id
                                                              }
                                                            })"
                                                        >
                                                            edit
                                                        </q-btn>
                                                        <q-btn
                                                            flat color="red"
                                                            @click="captionDeleteBuffer.id=caption.id; captionDeleteBuffer.isDeleting=true"
                                                        >
                                                            delete
                                                        </q-btn>
                                                    </div>
                                                </q-item>
                                            </div>
                                        </div>
                                    </div>
                                </q-expansion-item>
                            </div>

                            <!--Novel-->
                            <div v-for="(novel,i) in ip.novels"
                                 :key="i+novel.id+novel.name"
                            >
                                <q-item
                                    dense dark class="bg-dark-light q-pa-none bl2" style="padding-right: 39.3px"
                                >
                                    <div class="row q-pl-md items-center text-body1 full-width ">
                                        <q-icon
                                            name="import_contacts" color="secondary" size="1.3em"
                                            class="q-mr-md"
                                        >
                                        </q-icon>
                                        {{ novel.reservedNames[$i18n.locale] || novel.name }}
                                        <q-icon
                                            @click="$router.push({path:'/novel/info',query:{id:novel.id}})"
                                            size="0.75em" color="secondary" class="cursor-pointer q-ml-sm"
                                            name="fas fa-link"
                                        />
                                        <div class="row q-mx-sm">
                                            <q-chip outline
                                                    size="0.7em" square dense text-color="dark" color="secondary"
                                                    class="q-py-none text-weight-medium"
                                            >
                                                {{ novel.integrated ? 'INTEGRATED' : 'UNINTEGRATED' }}
                                            </q-chip>
                                            <q-chip outline
                                                    size="0.7em" square dense color="secondary"
                                                    class="q-py-none text-weight-medium"
                                            >
                                                {{ novel.fileMeta.type }}
                                            </q-chip>
                                        </div>
                                        <q-space></q-space>
                                        <q-btn
                                            flat color="secondary"
                                            @click="$router.push({
                                                path: '/novel/edit',
                                                query: {
                                                    id: novel.id
                                                }
                                            })"
                                        >
                                            edit
                                        </q-btn>
                                        <q-btn
                                            flat color="red"
                                            @click="novelDeleteBuffer.id=novel.id; novelDeleteBuffer.isDeleting=true"
                                        >
                                            delete
                                        </q-btn>
                                    </div>
                                </q-item>
                            </div>
                        </div>
                    </div>

                </q-expansion-item>
            </div>
        </div>
        <!--pagination-->
        <div class="full-width row justify-center q-my-sm">
<!--            <q-pagination-->
<!--                v-model="pageNum"-->
<!--                :max="Math.ceil(filterResultIPs.length/pageLen)"-->
<!--                color="accent"-->
<!--                input-->
<!--                input-class="text-accent text-weight-medium"-->
<!--            />-->
            <q-pagination
                v-model="pageNum"
                color="accent"
                active-color="accent"
                active-text-color="dark"
                :max="Math.ceil(filterResultIPs.length/pageLen)"
                :max-pages="10"
                boundary-links
                unelevated
            />
        </div>
    </div>
</template>

<script>
import IPDeleteDialog from "src/layout_pages/IP/IPDeleteDialog";
import AnimationDeleteDialog from "src/layout_pages/Animation/AnimationDeleteDialog";
import VideoDeleteDialog from "src/layout_pages/Animation/Video/VideoDeleteDialog";
import CaptionDeleteDialog from "src/layout_pages/Animation/Caption/CaptionDeleteDialog";
import NovelDeleteDialog from "src/layout_pages/Novel/NovelDeleteDialog";
import MultipleChoice from "components/MultipleChoice";

export default {
    name: "IndexIPs",
    components: {
        NovelDeleteDialog,
        CaptionDeleteDialog,
        VideoDeleteDialog,
        AnimationDeleteDialog,
        IPDeleteDialog,
        MultipleChoice
    },
    data() {
        return {
            toolbarExpanded: false,
            pageNum: 1,
            pageLen: 10,
            filterBuffer:{
                tagId: -1,
                order: 'date',
                region: 'ALL',
                animationType: 'ALL'
            },
            ipDeleteBuffer: {
                id: null,
                isDeleting: false
            },
            animationDeleteBuffer: {
                id: null,
                isDeleting: false
            },
            videoDeleteBuffer: {
                id: null,
                isDeleting: false
            },
            captionDeleteBuffer: {
                id: null,
                isDeleting: false
            },
            novelDeleteBuffer: {
                id: null,
                isDeleting: false
            }
        }
    },
    methods: {
        foo(i) {
            console.log(i)
        },
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
        idTagDict() {
            return this.$store.getters.idTagDict
        },
        filterResultIPs() {
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
                // const animationTypeFilter = (ip) => {
                //     if (this.filterBuffer.animationType === 'ALL') {
                //         return true
                //     } else {
                //         for (const animation of ip.animations) {
                //             if (animation.type === this.filterBuffer.animationType){
                //                 return true
                //             }
                //         }
                //         return false
                //     }
                // }
                // filterResultIPs = filterResultIPs.filter(animationTypeFilter)

                const compareIPByUpdatedAt = (ipA, ipB) => {
                    const dA = new Date(ipA.updatedAt)
                    const dB = new Date(ipB.updatedAt)
                    return dA < dB ? 1:-1
                }

                const compareIPByName= (ipA, ipB) => {
                    if (this.$i18n.locale == 'en'){
                        return (ipA.reservedNames[this.$i18n.locale] || ipA.name) >
                        (ipB.reservedNames[this.$i18n.locale] || ipB.name)? 1:-1
                    }else if(this.$i18n.locale == 'cn'){
                        return (ipA.reservedNames[this.$i18n.locale] || ipA.name).localeCompare(
                            (ipB.reservedNames[this.$i18n.locale] || ipB.name),'zh'
                        )
                    }
                }

                if (this.filterBuffer.order==='date'){
                    filterResultIPs.sort(compareIPByUpdatedAt)
                }else if (this.filterBuffer.order==='alphabet'){
                    filterResultIPs.sort(compareIPByName)
                }

                return filterResultIPs
            }
        },
        orderOptions(){
            return [
                {label:'date', icon: 'fas fa-sort-numeric-down-alt', value: 'date'},
                {label:'alphabet', icon: 'fas fa-sort-alpha-down', value: 'alphabet'}
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
                {label:'ALL',value: 'ALL'},
                {label:'TV',value: 'TV'},
                {label:'MOVIE',  value: 'MOVIE'},
                {label:'SP',value: 'SP'},
                {label:'OVA',value: 'OVA'},
                {label:'OAD',  value: 'OAD'}
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
        }
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
.bl
    border-left: solid
    border-left-color: $accent
    border-width: 2px

.bl1
    border-left: solid
    border-left-color: $primary
    border-width: 2px

.bl2
    border-left: solid
    border-left-color: $secondary
    border-width: 2px

.bl3
    border-left: solid
    border-left-color: white
    border-width: 2px

.bt
    border-top: solid
    border-top-color: $accent
    border-top-width: 2px

.bb
    border-bottom: solid
    border-bottom-color: $accent
    border-width: 2px
//border-bottom: solid
//border-bottom-color: $accent
//border-bottom-width: 2px
</style>
