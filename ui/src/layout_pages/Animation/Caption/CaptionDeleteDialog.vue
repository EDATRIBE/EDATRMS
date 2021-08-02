<template>
    <q-dialog v-model="show">
        <div
            class="bg-dark column q-pa-lg " style="width: 60vw; max-width: 60vw;"
            v-if="initialized"
        >
            <div style="width: 100%" class="q-pl-md bl">
                <div class="row q-pb-md">
                    <p class="q-my-none text-red text-h4 ">DELETE VIDEO</p>
                </div>
                <div class="row q-pb-md">
                    <p class="q-my-none text-body1 text-white ">
                        Please input
                        <span class="text-red text-weight-bold">{{ this.captionName}}</span>
                        to confirm this operation.
                    </p>
                </div>
                <div class="row items-center q-py-sm">
                    <div class="col-md-12 col-xs-12">
                        <q-input
                            hide-bottom-space
                            bg-color="dark-light"
                            dense dark class="" standout=""
                            v-model="confirmation"
                            :lazy-rules="true"
                            :rules="[()=> isValid||'Wrong Confirmation']"
                        >
                        </q-input>
                    </div>
                </div>
            </div>
            <div style="width: 100%" class="q-pl-md">
                <div class="row justify-end">
                    <q-btn class="q-ml-md" dense flat color="red" v-close-popup>cancel</q-btn>
                    <q-btn
                        class="q-ml-md" dense flat color="red"
                        :disable="!isValid"
                        @click="commitCaptionDelete(caption.id)"
                    >
                        commit
                    </q-btn>
                </div>
            </div>
        </div>
    </q-dialog>
</template>

<script>
export default {
    name: "CaptionDeleteDialog",
    props: {
        id: Number,
        isDeleting: Boolean,
    },
    data() {
        return {
            show: false,
            confirmation: '',
            loading: false,
        }
    },
    methods: {
        commitCaptionDelete(id) {
            let data = {id: id}
            this.$axios.post('api/caption/delete', data).then((response) => {
                let rd = response.data
                if (rd.code === 'success') {
                    this.$q.notify({type: 'success', message: this.$t("messages.success")})
                    this.$store.dispatch('getIPs').then(()=>{
                        this.show = false
                    })
                } else {
                    console.log(response)
                    this.$q.notify({type: 'failure', message: this.$t("messages.failure")})
                }
            }).catch((error) => {
                console.log(error)
            })
        }
    },
    watch: {
        isDeleting() {
            this.show = this.isDeleting
        },
        show() {
            if (this.show === false) {//clear state
                this.$emit('update:id', null)
                this.confirmation= ''
            }
            this.$emit('update:isDeleting', this.show)
        }
    },
    computed: {
        isValid(){
            return this.confirmation === this.captionName
        },
        initialized() {
            return this.caption !== null
        },
        ips() {
            return this.$store.state.ip.ips
        },
        caption() {
            if (this.ips === null) {
                return null
            }
            for (const ip of this.ips) {
                for (const animation of ip.animations) {
                    for (const caption of animation.captions) {
                        if (caption.id === this.id){
                            return caption
                        }
                    }
                }
            }
            return null
        },
        captionName() {
            if(this.caption===null){
                return null
            }else if (this.caption.fileMeta.name===''){
                return 'caption'
            }else {
                return this.caption.fileMeta.name
            }
        }
    }
}
</script>

<style lang="sass" scoped>
.bl
    border-left: solid
    border-left-color: $red
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
    border-top-color: $red
    border-top-width: 2px
//border-bottom: solid
//border-bottom-color: $red
//border-bottom-width: 2px
</style>
