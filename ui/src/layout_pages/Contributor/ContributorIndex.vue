<template>
    <q-page class="bg-dark q-px-md q-pb-xl" style="padding-top: 3.5em">
        <div class="q-mx-auto" style="width: 97%" v-if="initialized">
            <div
                class="row q-mb-md q-px-lg q-py-md bg-dark-light items-center"
                style="border-radius: 0px; position: relative;"
                :class="{'no-wrap': $q.screen.gt.sm}"
                v-for="(user,i) in users" :key="i+user.name"
            >
                <div
                    @click="$router.push({path:'/contributor/info',query:{user_id:user.id}})"
                >
                    <q-chip
                        v-show="user.animationIds.length>0"
                        dense
                        class="absolute q-ma-none q-pa-sm text-weight-medium cursor-pointer" color="white"
                        text-color="dark"
                        style="right: 20px; top:0px;  opacity: 1; border-radius: 0px 0px 7px 7px"
                    >
                        相关作品
                        <q-icon size=".9em" class="q-ml-sm" name="fas fa-link"/>
                    </q-chip>
                </div>
                <div>
                    <q-avatar size="140px" class="q-mr-lg">
                        <img
                            :src="user.avatar?user.avatar.url:GenAvatar(user.name)"
                        />
                    </q-avatar>
                </div>
                <div style="width: 100%" class="q-pr-md">
                    <div class="row items-end">
                        <div class="text-white text-h4 text-weight-medium q-mr-md">
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
                                    idRoleDict[roleId].reservedNames[$i18n.locale] || idRoleDict[roleId].name
                                }}
                            </q-chip>
                        </div>
                    </div>
                    <q-separator class="q-mt-sm" color="grey-7"></q-separator>
                    <div class="row q-pt-sm text-white text-justify text-body1">
                        <div>
                            <q-icon size="0.9em" class="q-mr-sm" name="fas fa-envelope"></q-icon>
                        </div>
                        <div class="text-justify">
                            {{ user.email || '[Secret ~]' }}
                        </div>
                    </div>
                    <div class="row q-pt-sm text-white text-justify text-body1">
                        <div>
                            <q-icon size="0.9em" class="q-mr-sm" name="fab fa-qq"></q-icon>
                        </div>
                        <div class="text-justify">
                            {{ user.qq || '[ Secret ~]' }}
                        </div>
                    </div>
                    <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
                        <div class="q-pa-none">
                            <q-icon size="0.9em" class="q-mr-sm" name="fas fa-info"></q-icon>
                        </div>
                        <div class="text-justify">
                            {{ user.intro || '[ He/She didn\'t write anything ~ ]' }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </q-page>
</template>

<script>
import {GenAvatar} from "src/utilities/GenAvatar";

export default {
    name: "ContributorIndex",
    data() {
        return {
            x: 'edit'
        }
    },
    methods: {
        GenAvatar: GenAvatar,
    },
    computed: {
        initialized() {
            return this.$store.getters.usersInitialized && this.$store.getters.rolesInitialized
        },
        users() {
            const cmp = (user1,user2)=>{
                if (user1.roleIds.length ===user2.roleIds.length){
                    return user1.id > user2.id ? 1:-1
                }
                else {
                    return user1.roleIds.length < user2.roleIds.length ? 1:-1
                }

            }
            const users = this.$store.state.user.users
            return users.sort(cmp)
        },
        idRoleDict() {
            return this.$store.getters.idRoleDict
        },
    }
}
</script>

<style lang="sass" scoped>
.bd-gold
    border: solid deeppink 1px

.bl
    border-left: solid
    border-left-color: $primary
    border-width: 2px


.ribbon
    width: 130px

    overflow: hidden
    white-space: nowrap
    /* top left corner */
    position: absolute
    top: 22px
    right: -32px
    /* for 45 deg rotation */
    -webkit-transform: rotate(45deg)
    -moz-transform: rotate(45deg)
    -ms-transform: rotate(45deg)
    -o-transform: rotate(45deg)
    transform: rotate(45deg)
    /* for creating shadow */
    //-webkit-box-shadow: 0 0 10px #888
    //-moz-box-shadow: 0 0 10px #888
    //box-shadow: 0 0 10px #888

.ribbon a
    border: 1px solid #faa
    color: #fff
    display: block
    font: bold 100% 'Helvetica Neue', Helvetica, Arial, sans-serif
    margin: 1px 0
    padding: 10px 50px
    text-align: center
    text-decoration: none
    /* for creating shadow */
    text-shadow: 0 0 5px #444

.silk-ribbon6
    display: inline-block
    text-align: center
    width: 200px
    height: 40px
    line-height: 40px
    position: absolute
    top: 30px
    right: -50px
    z-index: 2
    overflow: hidden
    transform: rotate(45deg)
    -ms-transform: rotate(45deg)
    -moz-transform: rotate(45deg)
    -webkit-transform: rotate(45deg)
    -o-transform: rotate(45deg)
    border: 1px dashed
    box-shadow: 0 0 0 3px white ,0px 21px 5px -18px rgba(0,0,0,0.6)
    background: white


</style>
