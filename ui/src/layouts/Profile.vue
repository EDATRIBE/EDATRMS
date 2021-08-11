<template>
    <div class="q-py-xl" style="width: 100%; padding-top: 6em">
        <!--Common-->
        <div v-if="!userEditBuffer.isEditing">
            <div class="row justify-center">
                <q-avatar size="250px" class="cursor-pointer " v-if="currentUser !== null">
                    <img contain :src="currentUser.avatar?currentUser.avatar.url:GenAvatar(currentUser.name)">
                </q-avatar>
            </div>
            <div
                class="row q-pt-md  items-center  text-h5 text-weight-medium"
            >
                {{ currentUser.name }}
            </div>
            <q-separator class="q-mt-sm" color="white"></q-separator>
            <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
                <div>
                    <q-icon size="1.2em" class="q-mr-sm" name="email"></q-icon>
                </div>
                <div class="text-justify">
                    {{ currentUser.email || '[Secret ~]' }}
                </div>
            </div>
            <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
                <div>
                    <q-icon size="1.1em" class="q-mr-sm" name="fab fa-qq"></q-icon>
                </div>
                <div class="text-justify">
                    {{ currentUser.qq || '[Secret ~]'}}
                </div>
            </div>
            <div class="row no-wrap q-pt-sm text-white text-justify text-body1">
                <div>
                    <q-icon size="1.1em" class="q-mr-sm" name="fas fa-info"></q-icon>
                </div>
                <div class="text-justify">
                    {{ currentUser.intro || '[ He/She didn\'t write anything ~ ]'}}
                </div>
            </div>
            <q-separator class="q-mt-sm" color="white"></q-separator>
            <div class="row q-mt-md justify-center">
                <q-btn
                    class="full-width text-weight-bold" color="white" text-color="dark"
                    @click="userEditBuffer.isEditing=true;readonly=true"
                >
                    EDIT PROFILE
                </q-btn>
            </div>
            <div class="row q-mt-md justify-center">
                <q-btn
                    class="full-width text-weight-bold" color="white" text-color="dark"
                    @click="signOut"
                >
                    SIGN OUT
                </q-btn>
            </div>
        </div>
        <!--Editing-->
        <div v-else>
            <div class="row justify-center">
                <file-pond
                    style="width: 250px"
                    name="file_pond_file"
                    ref="avatarPond"
                    class="cursor-pointer"
                    label-idle="DROP OR CLICK"
                    accepted-file-types="image/jpeg, image/png"
                    :files="userEditBuffer.avatarImage"
                    :server="userEditBuffer.server"
                    @init="handleFilePondInit"
                    allowImageCrop="true"
                    imageCropAspectRatio="1:1"
                    stylePanelLayout="compact circle"
                />
            </div>
            <div class="row q-pt-xs  items-center  text-white text-h5 text-weight-medium">
                <q-field
                    dense
                    dark
                    class="bg-dark-light"
                    style="width: 100%"
                    :value="userEditBuffer.data.name"
                    clear-icon="close"
                    standout=""
                    label="Name"
                    readonly
                >
                    <template v-slot:control>
                        <div class="self-center full-width no-outline" tabindex="0">{{ userEditBuffer.data.name }}</div>
                    </template>
                    <template v-slot:prepend>
                        <q-icon size="0.8em" name="fas fa-user"/>
                    </template>
                </q-field>
            </div>
            <q-separator class="q-mt-sm" color="white"></q-separator>
            <div class="row q-pt-sm text-white text-justify text-body1">
                <q-input
                    dense
                    dark
                    class="bg-dark-light"
                    style="width: 100%"
                    v-model="userEditBuffer.data.password"
                    clear-icon="close"
                    standout=""
                    label="New Password"
                >
                    <template v-slot:prepend>
                        <q-icon size="0.8em" name="fas fa-key"/>
                    </template>
                </q-input>
                <q-input
                    dense
                    dark
                    class="bg-dark-light q-mt-sm"
                    style="width: 100%"
                    v-model="userEditBuffer.data.confirmPassword"
                    clear-icon="close"
                    standout=""
                    label="Confirm Password"
                >
                    <template v-slot:prepend>
                        <q-icon size="0.8em" name="fas fa-key"/>
                    </template>
                </q-input>
            </div>
            <q-separator class="q-mt-sm" color="white"></q-separator>
            <div class="row q-pt-sm text-white text-justify text-body1">
                <q-input
                    dense
                    dark
                    class="bg-dark-light"
                    style="width: 100%"
                    v-model="userEditBuffer.data.email"
                    clear-icon="close"
                    standout=""
                    label="Email"
                >
                    <template v-slot:prepend>
                        <q-icon size="0.8em" name="fas fa-envelope"/>
                    </template>
                </q-input>
                <q-input
                    dense
                    dark
                    class="bg-dark-light q-mt-sm"
                    style="width: 100%"
                    v-model="userEditBuffer.data.qq"
                    clear-icon="close"
                    standout=""
                    label="QQ"
                >
                    <template v-slot:prepend>
                        <q-icon size="0.8em" name="fab fa-qq"/>
                    </template>
                </q-input>
                <q-input
                    dense
                    dark
                    autogrow
                    class="bg-dark-light q-mt-sm"
                    style="width: 100%"
                    v-model="userEditBuffer.data.intro"
                    clear-icon="close"
                    standout=""
                    label="Intro"
                >
                    <template v-slot:prepend>
                        <q-icon size="0.8em" name="fas fa-info"/>
                    </template>
                </q-input>
            </div>
            <q-separator class="q-mt-sm" color="white"></q-separator>
            <div class="row q-mt-sm justify-center">
                <q-btn
                    class="full-width text-weight-bold" color="white" text-color="dark"
                    @click="userEditBuffer.isEditing=false;initUserEditBufferData()"
                >
                    Cancel
                </q-btn>
                <q-btn
                    class="full-width text-weight-bold q-mt-sm" color="white" text-color="dark"
                    @click="commitEdit"
                >
                    Commit
                </q-btn>
            </div>
        </div>
    </div>
</template>

<script>

import {GenAvatar} from "src/utilities/GenAvatar";


export default {
    name: "Profile",
    mounted() {
        this.initUserEditBufferData()
    },
    data() {
        return {
            userEditBuffer: {
                isEditing: false,
                avatarImage: [],
                data: {},
                server: {
                    url: '/api',
                    process: '/storage/file/filepond/upload',
                    revert: null,
                    restore: null,
                    load: '/storage/file/filepond/load/',
                    fetch: null
                },
            }
        }
    },
    methods: {
        GenAvatar: GenAvatar,
        foo() {
            this.$q.notify({
                type: 'success',
                message: `New profile was submitted successfully.`
            })
            this.$q.notify({
                type: 'failure',
                message: `New profile was submitted successfully.`
            })
        },
        handleFilePondInit() {
            if (this.currentUser.avatar!==null) {
                this.userEditBuffer.avatarImage = [{
                    source: this.currentUser.avatar.id,
                    options: {
                        type: 'local'
                    }
                }]
            }
            console.log('FilePond has initialized');
        },
        initUserEditBufferData() {
            this.userEditBuffer.data = {
                name: this.currentUser.name,
                password: '',
                confirmPassword: '',
                email: this.currentUser.email,
                qq: this.currentUser.qq,
                intro: this.currentUser.intro,
                avatarId: this.currentUser.avatar ? this.currentUser.avatar.id : null
            }
        },
        commitEdit() {
            const currentAvatarList = this.$refs.avatarPond.getFiles()
            if (currentAvatarList.length === 0) {
                delete this.userEditBuffer.data.avatarId
            } else {
                if (currentAvatarList[0].status === 5 || currentAvatarList[0].status === 2) {
                    this.userEditBuffer.data.avatarId = Number(currentAvatarList[0].serverId)
                }
            }
            if (this.userEditBuffer.data.password !== this.userEditBuffer.data.confirmPassword) {
                console.log('密码不一致')
            } else {
                delete this.userEditBuffer.data.confirmPassword
                if (this.userEditBuffer.data.password === '') {
                    delete this.userEditBuffer.data.password
                }
            }
            console.log(this.userEditBuffer.data)

            delete this.userEditBuffer.data.name

            this.$axios.post('api/account/edit', this.userEditBuffer.data).then((response) => {
                let rd = response.data
                if (rd.code === 'success') {
                    console.log('rd.data.user')
                    console.log(rd.data.user)
                    this.$store.commit('setCurrentUser', rd.data.user)
                    this.$q.notify({
                        type: 'success',
                        message: `New profile was submitted successfully.`
                    })
                    this.initUserEditBufferData()
                    this.userEditBuffer.isEditing = false
                } else {
                    console.log(response)
                }
            }).catch((error) => {
                console.log(error)
            })

        },
        signOut() {
            this.$axios.get('api/account/logout').then((response) => {
                const rd = response.data
                console.log('return data:')
                console.log(rd)
                if (rd.code === 'success') {
                    this.$store.commit('setCurrentUser', null)
                    console.log('user:')
                    console.log(this.currentUser)
                }
                this.$q.notify({
                    type: 'success',
                    message: `Sign out successfully.`
                })
            }).catch(function (error) {
                console.log(error)
            })
        }
    },
    computed: {
        currentUser() {
            return this.$store.state.account.user
        }
    }
}
</script>
