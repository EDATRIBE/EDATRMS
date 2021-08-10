<template>
    <q-page class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
        <div class="q-mx-auto" style="width: 97%" v-if="initialized">
            <div
                class="row q-mb-md q-px-lg q-py-lg bg-dark-light" style="border-radius: 0px; position: relative"
                :class="{'no-wrap': $q.screen.gt.sm}"
            >
                <div>
                    <q-avatar size="150px" class="q-mr-md q-mt-sm">
                        <img
                            :src="user.avatar?user.avatar.url:GenAvatar(user.name)"
                        />
                    </q-avatar>
                </div>
                <div style="width: 100%">
                    <div class="row items-end">
                        <div class="text-white text-h4 text-weight-medium q-mr-sm">
                            {{ user.name }}
                        </div>
                        <div class="row text-weight-medium">
                            <q-chip
                                v-for="(roleId,i) in user.roleIds" :key="user.id+'role'+i"
                                size="0.9em"
                                :icon="idRoleDict[roleId].style.icon"
                                :text-color="idRoleDict[roleId].style.color"
                                color="dark"
                                square
                                class="q-mr-sm q-ml-none">
                                {{
                                    (idRoleDict[roleId].reservedNames[$i18n.locale] || idRoleDict[roleId].name).toUpperCase()
                                }}
                            </q-chip>

                            <q-chip size="0.9em" icon="face" color="dark" text-color="red-7" square
                                    class="q-mr-sm q-ml-none">LEADER
                            </q-chip>

                            <q-chip size="0.9em" icon="subtitles" color="dark" text-color="primary" square
                                    class="q-mr-sm q-ml-none">CAPTION CORRECTOR
                            </q-chip>
                            <q-chip size="0.9em" icon="subtitles" color="dark" text-color="primary" square
                                    class="q-mr-sm q-ml-none">CAPTION INSPECTOR
                            </q-chip>
                            <q-chip size="0.9em" icon="subtitles" color="dark" text-color="primary" square
                                    class="q-mr-sm q-ml-none">CAPTION CHECKER
                            </q-chip>
                            <q-chip size="0.9em" icon="local_shipping" color="dark" text-color="primary" square
                                    class="q-mr-sm q-ml-none">ANIMATION PORTER
                            </q-chip>
                            <q-chip size="0.9em" icon="local_shipping" color="dark" text-color="secondary" square
                                    class="q-mr-sm q-ml-none">NOVEL PORTER
                            </q-chip>
                            <q-chip size="0.9em" icon="emoji_emotions" color="dark" text-color="yellow-6" square
                                    class="q-mr-sm q-ml-none">MASCOT
                            </q-chip>
                            <q-chip size="0.9em" icon="emoji_food_beverage" color="dark" text-color="white" square
                                    class="q-mr-sm q-ml-none">RETIRED
                            </q-chip>
                            <q-chip size="0.9em" icon="settings" color="dark" text-color="purple-14" square
                                    class="q-mr-sm q-ml-none">TECH SUPPORT
                            </q-chip>
                            <q-chip size="0.9em" icon="calculate" color="dark" text-color="purple-14" square
                                    class="q-mr-sm q-ml-none">ACCOUNTING
                            </q-chip>
                            <q-chip size="0.9em" icon="history_edu" color="dark" text-color="purple-14" square
                                    class="q-mr-sm q-ml-none">EDITOR
                            </q-chip>
                        </div>
                    </div>
                    <q-separator class="q-mt-sm" color="grey-7"></q-separator>
                    <div class="row q-pt-sm text-white text-justify text-body1">
                        <div>
                            <q-icon size="0.9em" class="q-mr-sm" name="fas fa-envelope"></q-icon>
                        </div>
                        <div class="text-justify">
                            {{ user.email || '保密' }}
                        </div>
                    </div>
                    <div class="row q-pt-sm text-white text-justify text-body1">
                        <div>
                            <q-icon size="0.9em" class="q-mr-sm" name="fab fa-qq"></q-icon>
                        </div>
                        <div class="text-justify">
                            {{ user.qq || '保密' }}
                        </div>
                    </div>
                    <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
                        <div class="q-pa-none">
                            <q-icon size="0.9em" class="q-mr-sm" name="fas fa-info"></q-icon>
                        </div>
                        <div class="text-justify">
                            {{ user.intro || '这个人很懒，什么也没写' }}
                        </div>
                    </div>
                </div>
            </div>

            <!--Content-->
            <div class="row q-col-gutter-x-sm q-col-gutter-y-lg" v-if="initialized">
                <div class="col-md-2 col-sm-3 col-xs-6 col-lg-2 col-xl-2"
                     v-for="(animation,i) in animations"
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
                            <div class="full-width" style="overflow: hidden; position: relative; border-radius: 3px">
                                <q-img
                                    :src="animation.images.vertical?
                                    animation.images.vertical.url:
                                    require('assets/1.jpg')"
                                    class="mhs"
                                >
                                </q-img>
                                <q-chip
                                    dense
                                    class="absolute q-ma-none q-pa-md text-weight-medium shadow-5" color="primary"
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

        </div>
    </q-page>
</template>

<script>

import {GenAvatar} from "src/utilities/GenAvatar";
export default {
    name: "ContributorInfo",
    created() {
        if (this.readyToInitialize) this.initPage(this.$route.query.user_id)
    },
    data() {
        return {
            user: null,
            animations: []
        }
    },
    methods: {
        GenAvatar: GenAvatar,
        initPage(userId){
            this.user = this.idUserDict[userId]
            for (const animationId of this.user.animationIds) {
                this.animations.push(this.idAnimationDict[animationId])
            }
        }
    },
    computed: {
        readyToInitialize() {
            return this.$store.getters.ipsInitialized &&
                this.$store.getters.usersInitialized &&
                this.$store.getters.rolesInitialized
        },
        initialized() {
            return this.user!=null && this.animations.length>0
        },
        idAnimationDict() {
            return this.$store.getters.idAnimationDict
        },
        idUserDict() {
            return this.$store.getters.idUserDict
        },
        idRoleDict() {
            return this.$store.getters.idRoleDict
        },
    },
    watch: {
        readyToInitialize() {
            if (this.readyToInitialize) {
                this.initPage(this.$route.query.user_id)
            }
        }
    }
}
</script>

<style lang="sass"  scoped>

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
</style>
