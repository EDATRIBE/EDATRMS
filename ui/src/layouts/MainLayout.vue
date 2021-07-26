<template>
    <q-layout view="hHh lpr fFf">
        <q-header class="bg-dark q-px-md" reveal :reveal-offset="0">
            <q-toolbar style="width: 95%" class="q-py-md q-px-none q-mx-auto items-center">
                <q-icon name="fas fa-atom" size="2.35em"/>
                <div class="text-h4 q-ml-sm" v-if="$q.screen.gt.sm">EDATRMS</div>
                <q-space/>

                <nav-items v-if="$q.screen.gt.sm"/>
                <q-separator vertical color="grey" inset="true" class="q-ml-md" v-if="$q.screen.gt.sm"/>

                <q-btn-dropdown dense flat no-caps class="text-body1 q-ml-md" dropdown-icon="translate"
                                no-icon-animation content-class="bg-dark-light">
                    <div class="column q-pa-sm">
                        <q-btn
                            align="left" flat dense no-caps class="text-body1 text-white"
                            @click="$i18n.locale='en'"
                        >
                            English
                        </q-btn>
                        <q-btn
                            align="left" flat dense no-caps class="text-body1 text-white"
                            @click="$i18n.locale='cn'"
                        >
                            简体中文
                        </q-btn>
                    </div>
                </q-btn-dropdown>

                <q-separator vertical color="grey" inset="true" class="q-ml-md" v-if="!$q.screen.gt.sm"/>
                <nav-items v-if="!$q.screen.gt.sm"/>

                <q-separator vertical color="grey" inset="true" class="q-ml-md" v-if="$q.screen.gt.sm"/>
                <div v-if="$q.screen.gt.sm">
                    <q-btn
                        round outline class="q-ml-md"
                        size="0.78em" icon="mdi-badge-account-horizontal-outline"
                        v-if="currentUser === null"
                        @click="accountDrawer = !accountDrawer"
                    />
                    <q-avatar
                        size="2.35em" v-ripple class="cursor-pointer q-ml-md"
                        v-if="currentUser !== null"
                    >
                        <img @click="accountDrawer = !accountDrawer"
                             :src="currentUser.avatar?currentUser.avatar.url:GenAvatar(currentUser.name)">
                    </q-avatar>
                </div>
            </q-toolbar>
        </q-header>
        <!--UserLoginAndProfile-->
        <q-drawer
            side="right"
            v-model="accountDrawer"
            :width="350"
            dark
            overlay
            content-class="bg-dark"
            bordered
            class="q-pa-none full-height"
            :breakpoint="10000"
        >
            <q-scroll-area class="fit q-px-lg">
                <!--SignIn-->
                <sign-in v-if="currentUser === null"></sign-in>
                <!--Profile-->
                <profile v-if="currentUser !== null"></profile>
            </q-scroll-area>
        </q-drawer>
        <q-page-container>
            <keep-alive include="Index">
                <router-view/>
            </keep-alive>
        </q-page-container>
        <div class="bg-dark-deep q-ma-none q-pa-none" style="width: 100%; height: 300px">
        </div>
    </q-layout>
</template>

<script>
import SignIn from "layouts/SignIn";
import Profile from "layouts/Profile";
import NavItems from "layouts/NavItems";

import {GenAvatar} from "src/utilities/GenAvatar";

export default {
    name: 'MainLayout',
    components: {
        SignIn,
        Profile,
        NavItems
    },
    created() {
        this.$store.dispatch('getUser').then(() => {})
        this.$store.dispatch('getTags')
        this.$store.dispatch('getIPs').then(() => {})
        this.$store.dispatch('getAnnouncements').then(() => {})
    },
    data() {
        return {
            accountDrawer: false
        }
    },
    methods: {
        GenAvatar: GenAvatar,
        foo() {
        },
    },
    computed: {
        currentUser() {
            return this.$store.state.account.user
        }
    }
}
</script>

<style lang="scss">
.filepond--drop-label {
    color: white;
}

.filepond--panel-root {
    background-color: #373C41;
}

.q-markdown--link {
    font-weight: 500;
    text-decoration: none;
    outline: 0;
    border-bottom: 1px dotted currentColor;
    text-align: center;
    transition: opacity 0.2s;
    color: white;
}

/*.q-markdown--code-wrapper {*/
/*  width: 100%;*/
/*  min-width: 0;*/
/*  background: #282D33;*/
/*}*/

/*.q-markdown code, .q-markdown pre {*/
/*  font-family: Consolas, Monaco, Andale Mono, Ubuntu Mono, monospace;*/
/*  background: #282D33;*/
/*  color: white;*/
/*}*/

/*.token.operator {*/
/*  color: white;*/
/*}*/

/*.q-markdown--line-numbers {*/
/*  padding: 5px;*/
/*  text-align: right;*/
/*  background: #282D33;*/
/*  color: white;*/
/*}*/

.q-markdown--table {
    border-color: #282D33;
    background: #282D33;
}

.q-markdown--table thead {
    background: #282D33;
}

.q-markdown--table thead tr th {
    padding: 8px;
    border-width: 1px;
    border-style: solid;
    background: #282D33;
}

.q-markdown--table tbody {
    background: #282D33;
}

.q-markdown--table tbody td, .q-markdown--table tbody th {
    padding: 8px;
    border-width: 1px;
    border-style: solid;
}

.q-markdown--table tbody tr:nth-child(odd) {
    background: #282D33;
}

.q-input .text-negative {
    color: $red !important
}

.q-field--error .q-field__bottom {
    color: $red !important;
    color: $red !important
}


</style>
