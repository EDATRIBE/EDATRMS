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
            <div>
                <q-expansion-item
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
                    <!--Header-->
                    <template v-slot:header>
                        <div class="row  items-center text-body1 full-width ">
                            <q-btn-toggle
                                text-color="grey-7"
                                size="0.75em"
                                unelevated
                                class="no-border-radius bg-dark-light"
                                v-model="model"
                                toggle-color="accent"
                                toggle-text-color="dark"
                                :options="[
                                  {label:'date', icon: 'fas fa-sort-numeric-down-alt', value: 'one'},
                                  {label:'alphabet', icon: 'fas fa-sort-alpha-down', value: 'two'}
                                ]"
                            />
                            <q-space></q-space>
                            <q-icon
                                name="fas fa-plus" color="accent" size="1.25em" class="q-mx-sm cursor-pointer"
                                @click="$router.push('/ip/create')"
                            />
                        </div>
                    </template>

                </q-expansion-item>
            </div>
            <!--Content-->
            <div v-for="(ip,i) in searchResultIPs.slice((pageNum-1)*pageLen,pageNum*pageLen)" :key="i+'ip'+ip.id">
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
                                    size="0.7em" square dense text-color="dark" color="accent" class="q-py-none text-weight-medium"
                                >
                                    {{ ip.region }}
                                </q-chip>
                                <q-chip
                                    v-for="(tagId,i) in ip.tagIds" :key="i+'tag'"
                                    size="0.7em" square dense text-color="dark" color="accent" class="q-py-none text-weight-medium"
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
                            <div v-for="(animation,i) in ip.animations" :key="i+'ani'+ip.id+animation.id">
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
                                                    size="0.7em" square dense text-color="dark" color="primary" class="q-py-none text-weight-medium"
                                                >
                                                    {{ animation.type }}
                                                </q-chip>
                                                <q-chip outline
                                                    size="0.7em" square dense text-color="dark" color="primary" class="q-py-none text-weight-medium"
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
                                                 :key="i+'vid'+animation.id+video.id">
                                                <q-item
                                                    dense dark class="bg-dark-light q-pa-none bl1"
                                                    style="padding-right: 39.3px"
                                                >
                                                    <div class="row q-pl-md items-center text-body1 full-width text-weight-medium">
                                                        <q-icon name="fas fa-film" color="primary" size="1.3em"
                                                                class="q-mr-md"></q-icon>
                                                        {{ video.fileMeta.name || 'video' }}
                                                        <div class="row q-mx-sm">
                                                            <q-chip outline
                                                                size="0.7em" square dense text-color="dark" color="primary" class="q-py-none text-weight-medium"
                                                            >
                                                                {{ video.fileMeta.type }}
                                                            </q-chip>
                                                            <q-chip outline
                                                                size="0.7em" square dense text-color="dark" color="primary" class="q-py-none text-weight-medium"
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
                                                 :key="i+'cap'+animation.id+caption.id">
                                                <q-item
                                                    dense dark class="bg-dark-light q-pa-none bl1"
                                                    style="padding-right: 39.3px"
                                                >
                                                    <div class="row q-pl-md items-center text-body1 full-width text-weight-medium">
                                                        <q-icon name="fas fa-closed-captioning" color="primary"
                                                                size="1.3em"
                                                                class="q-mr-md"></q-icon>
                                                        {{ caption.fileMeta.name || 'caption'  }}
                                                        <div class="row q-mx-sm">
                                                            <q-chip outline
                                                                size="0.7em" square dense text-color="dark" color="primary" class="q-py-none text-weight-medium"
                                                            >
                                                                {{ caption.state }}
                                                            </q-chip>
                                                            <q-chip outline
                                                                size="0.7em" square dense color="primary" class="q-py-none text-weight-medium"
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
                            <div v-for="(novel,i) in ip.novels" :key="i+'nov'+ip.id+novel.id">
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
                                                    size="0.7em" square dense text-color="dark" color="secondary" class="q-py-none text-weight-medium"
                                            >
                                                {{ novel.integrated?'INTEGRATED':'UNINTEGRATED' }}
                                            </q-chip>
                                            <q-chip outline
                                                    size="0.7em" square dense color="secondary" class="q-py-none text-weight-medium"
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
        <div class="full-width row justify-center q-my-xs">
            <q-pagination
                v-model="pageNum"
                :max="Math.ceil(searchResultIPs.length/pageLen)"
                color="accent"
                input
                input-class="text-accent text-weight-medium"
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

export default {
    name: "IndexIPs",
    components: {NovelDeleteDialog, CaptionDeleteDialog, VideoDeleteDialog, AnimationDeleteDialog, IPDeleteDialog},
    data() {
        return {
            model: '',
            pageNum: 1,
            pageLen: 10,
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
        searchResultIPs() {
            return this.$store.state.ip.ips
        },
        initialized() {
            return this.$store.getters.ipsInitialized
        },
        idTagDict() {
            return this.$store.getters.idTagDict
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

//border-bottom: solid
//border-bottom-color: $accent
//border-bottom-width: 2px
</style>
