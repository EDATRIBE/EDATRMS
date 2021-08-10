<template>
    <q-page class="q-px-md q-pb-xl" style="padding-top: 3.5em" v-if="!LD">
        <q-scroll-observer @scroll="onScroll"/>
        <div class="q-mx-auto" style="width: 97%">
            <!--SEARCH-->
            <q-input
                dense dark class="text-h5 bg-dark-light q-mb-lg" style="width: 100%" standout=""
                v-model="searchBuffer"
                debounce="300"
                :autocomplete="false"
            >
                <template v-slot:append>
                    <q-spinner-grid
                        v-show="searching"
                        color="dark"
                    />
                </template>
            </q-input>
            <!--TABS-->
            <q-tabs
                style="width: 100%"
                v-model="tab"
                class="text-grey"
                align="justify"
                inline-label
                dense
                outside-arrows
            >
                <q-route-tab
                    ripple class="text-primary text-weight-medium" name="Animations" style="width: 50%"
                    to="/index/animations"
                >
                    <q-icon class="q-mr-xs" size="1.7em" name="movie"></q-icon>
                    {{ $t('ui.index.animations') }}
                </q-route-tab>
                <q-route-tab
                    ripple class="text-secondary text-weight-medium" name="Novels" style="width: 50%"
                    to="/index/novels"
                >
                    <q-icon class="q-mr-xs" size="1.7em" name="import_contacts"></q-icon>
                    {{ $t('ui.index.novels') }}
                </q-route-tab>
                <q-route-tab
                    ripple class="text-accent text-weight-medium" name="IPsAndTags" style="width: 50%"
                    v-if="currentUser&&currentUser.staff"
                    to="/index/ips_and_tags"
                >
                    <q-icon class="q-mr-xs" size="1.7em" name="source"></q-icon>
                    {{ $t('ui.index.ips') }}
                    <span class="q-mx-sm">|</span>
                    <q-icon class="q-mr-xs" size="1.2em" name="fas fa-hashtag"></q-icon>
                    {{ $t('ui.index.tags') }}
                </q-route-tab>
            </q-tabs>
            <keep-alive>
                <router-view/>
            </keep-alive>
        </div>

        <q-page-sticky expand position="top" class="bg-dark q-px-md q-py-sm" v-show="scrollInfo.position>112">
            <q-toolbar style="width: 97%" class="q-px-none">
                <q-input
                    dense dark class="text-h5 bg-dark-light" style="width: 100%" standout=""
                    v-model="searchBuffer"
                    debounce="300"
                    :autocomplete="false"
                >
                    <template v-slot:append>
                        <q-spinner-grid
                            v-show="searching"
                            color="dark"
                        />
                    </template>
                </q-input>
            </q-toolbar>
        </q-page-sticky>
    </q-page>
</template>

<script>

import IndexAnimations from "src/layout_pages/Index/IndexAnimations";
export default {
    name: "Index",
    activated() {
        if (this.$route.query.tab) {
            this.tab = this.$route.query.tab
        }
        if (this.$route.query.search) {
            this.searchBuffer = this.$route.query.search
        }
    },
    data() {
        return {
            LD: true,
            scrollInfo: {},
            searchBuffer: '',
            tab: 'Animations',
        }
    },
    methods: {
        foo() {
        },
        onScroll(info) {
            this.scrollInfo = info
        }
    },
    created() {
        this.LD = false
    },
    computed: {
        currentUser() {
            return this.$store.state.account.user
        },
        ips() {
            return this.$store.state.ip.ips
        },
        searching() {
            return this.$store.state.ip.loading
        }
    },
    watch: {
        searchBuffer() {
            this.$store.dispatch('searchKeywords',this.searchBuffer)
        },
        ips() {
            this.$store.dispatch('searchKeywords',this.searchBuffer)
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
</style>
