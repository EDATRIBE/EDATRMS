<template>
    <div>
        <TagDeleteDialog
            :id.sync="tagDeleteBuffer.id"
            :is-deleting.sync="tagDeleteBuffer.isDeleting"
        />
        <!--add tag-->
        <q-dialog v-model="tagCreateBuffer.isCreating">
            <div class="bg-dark column q-pa-lg " style="width: 60vw; max-width: 60vw;">
                <div style="width: 100%" class="q-pl-md bl">
                    <div class="row q-pb-md">
                        <p class="q-my-none text-accent text-h4 ">NEW TAG</p>
                    </div>
                </div>
                <div style="width: 100%" class="q-pl-md bl">
                    <div class="row items-center q-py-sm">
                        <div class="col-md-2 col-xs-12">
                            <p class="q-my-none text-grey text-body1 text-weight-medium">NAME</p>
                        </div>
                        <div class="col-md-10 col-xs-12">
                            <q-input
                                dense dark class=" bg-dark-light" standout=""
                                v-model="tagCreateBuffer.data.name"
                                hide-bottom-space
                            >
                            </q-input>
                        </div>
                    </div>
                    <div class="row items-center q-py-sm">
                        <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">
                            NAME-EN</p>
                        </div>
                        <div class="col-md-10 col-xs-12">
                            <q-input
                                dense dark class=" bg-dark-light" standout=""
                                v-model="tagCreateBuffer.data.reservedNames.en"
                            >
                            </q-input>
                        </div>
                    </div>
                    <div class="row items-center q-py-sm">
                        <div class="col-md-2 col-xs-12"><p class="q-my-none text-grey text-body1 text-weight-medium">
                            NAME-CN</p>
                        </div>
                        <div class="col-md-10 col-xs-12">
                            <q-input
                                dense dark class=" bg-dark-light" standout=""
                                v-model="tagCreateBuffer.data.reservedNames.cn"
                            >
                            </q-input>
                        </div>
                    </div>
                </div>
                <div style="width: 100%" class="q-pl-md">
                    <div class="row justify-end">
                        <q-btn class="q-ml-md" dense flat color="accent" v-close-popup>cancel</q-btn>
                        <q-btn
                            class="q-ml-md" dense flat color="accent"
                            @click="commitCreate"
                        >
                            commit
                        </q-btn>
                    </div>
                </div>
            </div>
        </q-dialog>
        <!--content-->
        <div class="q-col-gutter-y-sm">
            <div>
                <div
                    class="row q-pt-md q-pb-sm q-px-md bg-dark-light bt"
                    v-if="initialized"
                >
                    <q-chip
                        v-for="(tag,i) in tags" :key="'tag'+i"
                        class="q-mr-sm q-mb-sm q-ml-none q-mt-none text-weight-medium"
                        dense
                        square
                        color="accent"
                        removable
                        @remove="tagDeleteBuffer.id=tag.id; tagDeleteBuffer.isDeleting=true"
                        clickable
                    >
                        <q-icon class="q-mx-xs" name="fas fa-tags" color="dark"></q-icon>
                        {{ tag.reservedNames[$i18n.locale] || tag.name }}
                    </q-chip>
                    <q-chip
                        class="q-mr-sm q-mb-sm q-ml-none q-mt-none text-weight-medium"
                        text-color="dark"
                        dense
                        square
                        color="accent"
                        clickable
                        outline
                        @click="tagCreateBuffer.isCreating = true"
                    >
                        <q-icon size="1.1em" class="q-mr-xs" name="fas fa-plus" color="accent"></q-icon>
                        New
                    </q-chip>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import TagDeleteDialog from "src/layout_pages/Index/TagDeleteDialog";
export default {
    name: "IndexTags",
    components: {TagDeleteDialog},
    created() {
    },
    data() {
        return {
            LD: true,
            tagCreateBuffer: {
                isCreating: false,
                data: {
                    name: '',
                    reservedNames: {
                        en: '',
                        cn: ''
                    }
                },
            },
            tagDeleteBuffer: {
                id: null,
                isDeleting: false
            },
            text: 'false'
        }
    },
    methods: {
        foo() {
        },
        initTagCreateBufferData() {
            this.tagCreateBuffer.data = {
                name: '',
                reservedNames: {
                    en: '',
                    cn: ''
                }
            }
        },
        commitCreate() {
            this.$axios.post('api/tag/create', this.tagCreateBuffer.data).then((response) => {
                let rd = response.data
                if (rd.code === 'success') {
                    this.$q.notify({type: 'success', message: this.$t("messages.success")})
                    this.$store.dispatch('getTags')
                    this.initTagCreateBufferData()
                    this.tagCreateBuffer.isCreating = false
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
        tags() {
            return this.$store.state.tag.tags
        },
        initialized() {
            return this.$store.getters.tagsInitialized
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
    border-bottom-width: 2px

//border-bottom: solid
//border-bottom-color: $accent
//border-bottom-width: 2px
</style>
